"""
utils/mock_analysis.py

Provides dummy condition data for EmpowerImaging.
All content is placeholder educational material.

TODO (AI integration):
  Replace `get_condition_data()` with a function that:
  1. Accepts a file path (the uploaded MRI scan)
  2. Calls your ML model / API (e.g. a fine-tuned vision model)
  3. Returns a dict matching the same schema used here
  This keeps all templates compatible without changes.
"""

import json
import os


def get_condition_data():
    """
    Load and return the first (demo) condition from conditions.json.

    TODO (AI integration): Accept model output and select / generate
    the matching condition record dynamically.
    """
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "conditions.json")
    with open(data_path, "r") as f:
        conditions = json.load(f)

    # For the demo, always return the first condition.
    # A real implementation would match based on model classification.
    return conditions[0]
