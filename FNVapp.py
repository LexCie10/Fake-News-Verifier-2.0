
import pickle
import streamlit as st
import pandas as pd
import re
import tldextract


# load the file that contains the model (model.pkl)
with open("fnv_pipeline.pkl", 'rb') as f:
    pipeline = pickle.load(f)

# List of trusted sources
trusted_domains = ["bbc.com", "cnn.com", "aljazeera.com", "reuters.com", "nytimes.com", "washingtonpost.com", "bloomberg.com", "forbes.com", "theguardian.com", "channels.com", "arisenews.com"]

def extract_url_from_text(text):
    """Extracts a URL from the text if present."""
    url_pattern = r"https?://[^\s]+"  # Matches URLs starting with http:// or https://
    urls = re.findall(url_pattern, text)
    return urls[0] if urls else None  # Return the first URL found or None

def extract_domain(url):
    """Extracts the domain name from a URL."""
    if url:
        extracted = tldextract.extract(url)
        return f"{extracted.domain}.{extracted.suffix}" if extracted.suffix else extracted.domain
    return None


    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color:white;
        border-radius:10px;
        font-size:20px;
        height:3em;
        width:10em;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff6666;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        border: 2px solid #4A7DF5;
        border-radius: 10px;
    .stTextArea > div > div > input {
        border: 2px solid #4A7DF5;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Give the Streamlit app page a title
st.markdown("<h1 style='text-align: center; color: #4A7DF5;'>FAKE NEWS VERIFIER 2.0</h1>", unsafe_allow_html=True)
st.write("<h3 style='text-align: center;'>Enter news article title, content and source URL(Optional) here to verify if it's <b>Fake</b> or <b>Real</b>.</h3>", unsafe_allow_html=True)

# input fields for getting user values for X (title and text fields)
news_url = st.text_input("🔗 Enter the news source URL(Optional)")
title = st.text_input("Title", placeholder="Enter the news headline here...")
text = st.text_area("Content", placeholder="Paste the full news article here...")

# After the user pastes the title and text of his or her News article and the 'submit' button is clicked, make the prediction and store it
if st.button("Verify"):
    if title and text:

        # Combine title and text into a single feature
        combined_text = title + " " + text

        # Check if user provided a URL separately first
        if news_url:
            final_url = extract_domain(news_url)
        else:
            # If no user-provided URL, extract from text
            final_url = extract_url_from_text(combined_text)

        # Extract URL from text
        extracted_url = extract_url_from_text(combined_text)

        # Extract domain from the URL
        domain = extract_domain(extracted_url) if extracted_url else "unknown"

        # Auto-classify if from a trusted domain
        if domain in trusted_domains:
            st.subheader(f"✅ **Real News (Trusted Source: {domain})**")
        else:
            # Predict using the pipeline
            prediction = pipeline.predict([combined_text])[0]

            # Show result
            result = "✅ **Real News**" if prediction == 1 else "❌ **Fake News**"
            st.subheader(result)
    else:
        st.warning("⚠️ Please enter both the title and content to verify.")
