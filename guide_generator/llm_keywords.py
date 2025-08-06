import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_keywords_with_llm(token, region):
    prompt = f"""
You are an SEO expert. Suggest:
1. 10 LSI keywords for the topic '{token} crypto in {region}'
2. 10 long-tail keywords related to buying or learning about {token} in {region}
Output in plain bullet points.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content']
