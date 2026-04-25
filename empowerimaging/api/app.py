"""
EmpowerImaging - Flask Application
Educational MRI scan viewer with visual anatomy lessons.
NOT a medical diagnostic tool.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from utils.mock_analysis import get_condition_data

app = Flask(__name__)
app.secret_key = "empower-imaging-secret-key-change-in-production"

template_folder="../templates",
static_folder="../static"


UPLOAD_FOLDER = os.path.join("static", "uploads")
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
    """Render the MRI upload form."""
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_post():
    """
    Handle uploaded MRI image.
    Saves file locally and stores filename in session.
    TODO (AI integration): Replace dummy analysis with real model inference here.
    """
    file = request.files.get("mri_scan")

    if not file or file.filename == "":
        return render_template("upload.html", error="Please select an image file.")

    if not allowed_file(file.filename):
        return render_template("upload.html", error="Only JPG and PNG files are accepted.")

    filename = secure_filename(file.filename)
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(save_path)

    # Store in session so subsequent pages can access it
    session["uploaded_filename"] = filename

    # TODO (AI integration): Trigger async model inference on `save_path` here
    # and store the result ID in session for retrieval on the visualization page.

    return redirect(url_for("visualization"))


# ─────────────────────────────────────────────
# ROUTE 2: Visualization Page
# ─────────────────────────────────────────────
@app.route("/visualization")
def visualization():
    """
    Show uploaded MRI with simulated heatmap overlay and educational content.
    TODO (AI integration): Replace `get_condition_data()` with real model output.
    """
    filename = session.get("uploaded_filename")
    if not filename:
        return redirect(url_for("upload_get"))

    # TODO (AI integration): Pass scan path to model; retrieve structured result.
    condition = get_condition_data()

    return render_template("visualization.html", filename=filename, condition=condition)


# ─────────────────────────────────────────────
# ROUTE 3: Questions & Next Steps Page
# ─────────────────────────────────────────────
@app.route("/next-steps")
def next_steps():
    """
    Display doctor questions, next steps, and urgent care guidance.
    Content is educational only — not personalised medical advice.
    """
    filename = session.get("uploaded_filename")
    if not filename:
        return redirect(url_for("upload_get"))

    # TODO (AI integration): Personalise questions/steps based on model output.
    condition = get_condition_data()

    return render_template("next_steps.html", condition=condition)


if __name__ == "__main__":
    app.run(debug=True)
