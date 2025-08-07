import streamlit as st
from guide_generator.trends import get_trending_tokens
from guide_generator.serpapi_scraper import fetch_serp_data, extract_faqs_and_links
from guide_generator.llm_keywords import suggest_keywords_with_llm
from guide_generator.content_generator import generate_crypto_guide
from guide_generator.utils import save_to_markdown, region_code_map

# --- UI ---
st.set_page_config(layout="centered")
st.title("🪙 Localized Crypto Guide Generator")

# ✅ "Worldwide" added to region selection
region = st.selectbox("🌍 Select Region", ["Worldwide", "India", "USA", "UK", "Canada", "Australia"])
content_type = st.selectbox("📝 Content Type", ["Blog / Evergreen", "News / Trending"])
keyword = st.text_input("🔍 Broad keyword (default: crypto)", value="crypto")
timeframe = st.selectbox("📆 Timeframe", ["now 7-d", "today 3-m", "today 12-m"])

if st.button("Fetch Trending Tokens"):
    region_code = region_code_map(region)
    tokens = get_trending_tokens(region_code, seed_keyword=keyword, timeframe=timeframe)

    if tokens:
        st.success(f"Found trending tokens: {', '.join(tokens)}")
        selected_token = st.selectbox("🎯 Pick a token to generate guide", tokens)

        if selected_token:
            serp_data = fetch_serp_data(selected_token, region_code)
            faqs, sources = extract_faqs_and_links(serp_data)

            if content_type == "Blog / Evergreen":
                st.markdown("### 🔎 LLM Keyword Suggestions")
                st.text(suggest_keywords_with_llm(selected_token, region))

            st.markdown("### 📄 Generated Guide Preview")
            guide = generate_crypto_guide(selected_token, region, faqs, sources, content_type)
            st.markdown(guide)

            filename_base = f"{selected_token.lower().replace(' ', '_')}_{content_type.lower().replace('/', '').replace(' ', '_')}_{region.lower()}"
            save_to_markdown(guide, filename_base)

            st.download_button("⬇️ Download Markdown", data=guide, file_name=f"{filename_base}.md")
    else:
        st.warning("No trending tokens found for this region.")
