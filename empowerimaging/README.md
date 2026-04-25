# EmpowerImaging

An educational Flask web app that helps users understand MRI scans using visual anatomy lessons.

> ⚠️ **Not a medical device.** EmpowerImaging does not provide diagnoses. All content is general health education.

---

## Quick Start

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## Project Structure

```
empowerimaging/
├── app.py                   # Flask routes
├── requirements.txt
├── data/
│   └── conditions.json      # Dummy condition content
├── utils/
│   └── mock_analysis.py     # Placeholder for AI model integration
├── templates/
│   ├── upload.html
│   ├── visualization.html
│   └── next_steps.html
└── static/
    ├── css/styles.css
    └── uploads/             # Saved MRI images (session-scoped)
```

---

## AI Integration Points

Search the codebase for `TODO (AI integration)` comments. Key locations:

| File | What to replace |
|------|----------------|
| `app.py` → `upload_post()` | Trigger model inference after saving upload |
| `app.py` → `visualization()` | Pass model result to template instead of dummy data |
| `utils/mock_analysis.py` → `get_condition_data()` | Return real model output |
| `visualization.html` | Use model-returned coordinates for heatmap overlay |
| `next_steps.html` | Personalise questions based on model classification |

---

## Disclaimer

This application is for educational purposes only. It is not a medical device, does not provide clinical diagnoses, and should not be used as a substitute for professional medical advice.
