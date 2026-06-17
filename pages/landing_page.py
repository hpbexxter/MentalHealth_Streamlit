import streamlit as st

from utils.utils import get_base64_encoded_image

df = st.session_state["df"]

st.title("Mental Health in der Tech-Branche")
st.dataframe(df.head())


st.markdown("""---""")
st.markdown("""### Hilfsangebote""")


encoded_116117 = get_base64_encoded_image("assets/logo_116117.svg")

col1, col2 = st.columns([1, 8])

with col1:
    st.markdown(f"""
        <a href="https://www.116117.de/de/psychotherapie.php" target="_blank">
            <img src="data:image/svg+xml;base64,{encoded_116117}" width="200"/>
        </a>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        **116117**: Unter der Nummer 116117 können Sie rund um die Uhr einen Termin bei einem Psychotherapeuten vereinbaren. 
        Es handelt sich um eine kostenlose Service-Hotline, die von der Kassenärztlichen Bundesvereinigung betrieben wird.
    """)

st.markdown("""---""")
st.markdown("""### Ressourcen & Downloads""")

encoded_github = get_base64_encoded_image("assets/github.png")
encoded_kaggle = get_base64_encoded_image("assets/kaggle.png")
encoded_csvIcon = get_base64_encoded_image("assets/csv.png")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; gap: 14px;">
            <a href="https://github.com/hpbexxter/MentalHealth_Streamlit" target="_blank">
                <img src="data:image/png;base64,{encoded_github}" width="100"
                    style="background-color: white; 
                    border-radius: 6px; 
                    padding: 4px;"/>
            </a>
            <span style="font-size: 0.85rem; color: #555;">Repository</span>
        </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; gap: 14px;">
            <a href="https://www.kaggle.com/datasets/mohankrishnathalla/mental-health-and-burnout-in-tech-workers-2026?resource=download" target="_blank">
                <img src="data:image/png;base64,{encoded_kaggle}" width="100"
                    style="background-color: white; 
                    border-radius: 6px; 
                    padding: 4px;"/>
            </a>
            <span style="font-size: 0.85rem; color: #555;">Kaggle Datensatz</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stDownloadButton"] button p {
    font-size: 5rem !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        [data-testid="stDownloadButton"] button {
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 6px;
            padding: 4px;
            width: 100px;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-left: 10px;
        }
        [data-testid="stDownloadButton"] button:hover {
            border-color: #aaa;
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

with col3:
    inner_col = st.columns([1, 1, 1])[1]  # zentrieren
    with inner_col:
        st.download_button(
            label="📊",
            data=df.to_csv(index=False),
            file_name="mental_health_burnout_tech_2026_cleaned.csv",
            mime="text/csv",
        )

        st.markdown(
            "<p style='text-align:center; font-size:0.85rem; color:#555;'>"
            "Bereinigter Datensatz (CSV)"
            "</p>",
            unsafe_allow_html=True
        )