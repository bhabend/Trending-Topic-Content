import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_crypto_guide(token, region, faqs, sources, content_type):
    if content_type == "News / Trending":
        prompt = f"""
Create a news-style crypto update for the token '{token}' in {region}.
Include the latest developments, why it's trending, and how it might affect the market.
Use these sources if needed: {', '.join(sources)}.
"""
    else:
        prompt = f"""
Write a crypto guide for '{token}' targeted at beginners in {region}.
Include:
1. Introduction and overview
2. Relevance in {region}
3. How to buy {token} in {region}
4. Local exchanges (if possible)
5. Answer the following FAQs: {', '.join(faqs)}
Use these sources if needed: {', '.join(sources)}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']
