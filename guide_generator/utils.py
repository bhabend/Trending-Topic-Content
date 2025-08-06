def save_to_markdown(content: str, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def region_code_map(region: str) -> str:
    mapping = {
        "India": "IN",
        "USA": "US",
        "UK": "GB",
        "Canada": "CA",
        "Australia": "AU"
    }
    return mapping.get(region, "IN")
