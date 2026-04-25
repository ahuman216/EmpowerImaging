"""
EmpowerImaging - Flask Application
Educational MRI scan viewer with visual anatomy lessons.
NOT a medical diagnostic tool.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from utils.mock_analysis import get_condition_data

# ✅ FIX 1: Proper Flask initialization for Vercel
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

app.secret_key = "empower-imaging-secret-key-change-in-production"

# ✅ FIX 2: Use /tmp for uploads on Vercel
UPLOAD_FOLDER = "/tmp/uploads"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ─────────────────────────────────────────────
# ROUTE 1: Upload Page
# ─────────────────────────────────────────────
@app.route("/", methods=["GET"])
@app.route("/upload", methods=["GET"])
def upload_get():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_post():
    file = request.files.get("mri_scan")

    if not file or file.filename == "":
        return render_template("upload.html", error="Please select an image file.")

    if not allowed_file(file.filename):
        return render_template("upload.html", error="Only JPG and PNG files are accepted.")

    filename = secure_filename(file.filename)
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(save_path)

    session["uploaded_filename"] = filename
    return redirect(url_for("visualization"))


# ─────────────────────────────────────────────
# ROUTE 2: Visualization Page
# ─────────────────────────────────────────────
@app.route("/visualization")
def visualization():
    filename = session.get("uploaded_filename")
    if not filename:
        return redirect(url_for("upload_get"))

    condition = get_condition_data()
    return render_template("visualization.html", filename=filename, condition=condition)


# ─────────────────────────────────────────────
# ROUTE 3: Next Steps
# ─────────────────────────────────────────────
@app.route("/next-steps")
def next_steps():
    filename = session.get("uploaded_filename")
    if not filename:
        return redirect(url_for("upload_get"))

    condition = get_condition_data()
    return render_template("next_steps.html", condition=condition)
