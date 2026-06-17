import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Mental Health in Tech',
    page_icon='📚',
    layout='wide',
    initial_sidebar_state='expanded'
)

@st.cache_data
def load_data():
    return pd.read_csv('./data/mental_health_burnout_tech_2026_cleaned.csv')

# Daten vorladen und in session_state ablegen
if "df" not in st.session_state:
    st.session_state["df"] = load_data()

# Navigation
landing = st.Page("pages/landing_page.py",    title="Übersicht", icon="🏠")
analyse   = st.Page("pages/analyse_page.py", title="Analyse",   icon="📊")

pg = st.navigation({
    "Allgemein": [landing],
    "Daten":     [analyse],
})

pg.run()