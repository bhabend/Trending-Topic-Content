import os
import requests
from pytrends.request import TrendReq

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def map_country_to_code(region):
    mapping = {
        "India": "IN",
        "United States": "US",
        "United Kingdom": "GB",
        "Germany": "DE",
        "France": "FR",
        "Japan": "JP",
        "Brazil": "BR"
    }
    return mapping.get(region, None)

def get_trending_keywords(region, use_serpapi=True):
    if use_serpapi:
        return get_keywords_from_serpapi(region)
    else:
        return get_keywords_from_pytrends(region)

def get_keywords_from_serpapi(region):
    params = {
        "engine": "google_trends",
        "q": "crypto",
        "api_key": SERPAPI_KEY
    }

    if region != "Worldwide":
        region_code = map_country_to_code(region)
        if region_code:
            params["geo"] = region_code

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    try:
        trending = [trend["title"] for trend in data["trendingSearches"]]
    except KeyError:
        trending = []

    return trending[:10]

def get_keywords_from_pytrends(region):
    pytrends = TrendReq()
    if region == "Worldwide":
        pytrends.build_payload(kw_list=["crypto"])
        df = pytrends.trending_searches(pn='global')
    else:
        region_code = map_country_to_code(region)
        if region_code:
            pytrends.build_payload(kw_list=["crypto"], geo=region_code)
            df = pytrends.trending_searches()
        else:
            df = []

    return df.head(10)[0].tolist() if not df == [] else []
