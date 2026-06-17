import base64
import streamlit as st

@st.cache_data
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()