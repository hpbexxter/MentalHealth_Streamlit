import base64
import streamlit as st

@st.cache_data
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
    


def card(label, value, label_color="#aaa", content_color="#fff", bg_color="#1e1e2e"):
    st.markdown(f"""
    <div style="
        background-color: {bg_color};
        border-radius: 12px;
        padding: 1.5em;
        text-align: center;
        border: 1px solid #333;
    ">
        <p style="color: {label_color}; font-size: 0.9em; margin-bottom: 0.3em;">{label}</p>
        <p style="color: {content_color}; font-size: 2em; font-weight: bold; margin: 0;">{value}</p>
    </div>
    """, unsafe_allow_html=True)