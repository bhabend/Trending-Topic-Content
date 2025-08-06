import os
import requests
from dotenv import load_dotenv
load_dotenv()

def fetch_serp_data(token, region="in", lang="en"):
    params = {
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "engine": "google",
        "q": f"{token} crypto",
        "gl": region.lower(),
        "hl": lang.lower()
    }
    res = requests.get("https://serpapi.com/search", params=params)
    return res.json()

def extract_faqs_and_links(serp_data):
    faqs = [q['question'] for q in serp_data.get("related_questions", [])]
    links = [r['link'] for r in serp_data.get("organic_results", [])[:3]]
    return faqs, links
