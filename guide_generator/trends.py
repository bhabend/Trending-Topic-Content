from pytrends.request import TrendReq

def get_trending_tokens(region_code: str, seed_keyword="crypto", timeframe="now 7-d") -> list:
    pytrends = TrendReq()
    pytrends.build_payload([seed_keyword], geo=region_code, timeframe=timeframe)
    related = pytrends.related_queries()
    rising = related.get(seed_keyword, {}).get("rising", None)
    if rising is not None:
        return list(rising["query"].head(5))
    return []
