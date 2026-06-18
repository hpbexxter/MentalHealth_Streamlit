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

# Load data into session state
if "df" not in st.session_state:
    st.session_state["df"] = load_data()

st.logo(
    "assets/navbar_logo.svg",
    size="large",
    )

# Navigation setup
landing = st.Page("pages/landing_page.py", title="Übersicht", icon="🏠")
analyse = st.Page("pages/analyse_page.py", title="Analyse",   icon="📊")
ml = st.Page("pages/maschine_learning_page.py", title="Maschine Learning", icon="🤖")
visu = st.Page("pages/visu_page.py", title="Visualisierung", icon="📈")


# Create navigation
pg = st.navigation({
    "Allgemein": [landing],
    "Daten & Analyse": [analyse, visu, ml],
})

# Run the app
pg.run()