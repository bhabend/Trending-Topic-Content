import os
from datetime import datetime

def save_to_markdown(content, filename):
    output_dir = "generated_guides"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved guide to {filepath}")

def region_code_map(region):
    mapping = {
        "Worldwide": "",       # Leave empty or use 'world' based on API expectations
        "India": "IN",
        "USA": "US",
        "UK": "GB",
        "Canada": "CA",
        "Australia": "AU",
    }
    return mapping.get(region, "")
