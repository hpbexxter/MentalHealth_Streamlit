import streamlit as st
import plotly.express as px

from utils.utils import get_base64_encoded_image
from utils.utils import card

df = st.session_state["df"]

st.title("🧠 Mental Health in der Tech-Branche")
st.markdown("""
            Der vorliegende Datensatz befasst sich mit Angaben der psychischen
            Gesundheit von Mitarbeiter*innen in der Tech-Branche.\n
            Mit ca. 90.000 Datensätzen, Mitarbeiter*innen aus 10 verschiedenen Ländern und Branchen bietet er
            eine breite, internationale Grundlage für die Analyse von Burnout
            und psychischen Belastungen am Arbeitsplatz. Erfasst werden dabei
            klinisch etablierte Messinstrumente wie der PHQ-9 (zur Erfassung
            von Depressionssymptomen) die eine fundierte Einschätzung des psychischen
            Wohlbefindens ermöglichen. 
            
            Grundsätzlich wird versucht auf Basis von Berufsrolle und hierarchischer Position
            im Unternehmen depressive Symptome (PHQ-9) bei Tech-Beschäftigten
            vorherzusagen und zu bestimmen, welche Faktoren im Berufsalltag den stärksten Einfluss haben?
            
            **Wichtig:** Es handelt sich hierbei um einen synthetischen Datensatz, 
            ob die Daten auf realen Erhebungen basieren, ist nicht bekannt.
        """)
st.markdown("""---""")
st.subheader("📋 Projektübersicht")
st.markdown("""
            1. 🏠 **Übersicht** - Dashboard der App und allgemeine Infos
            2. 📊 **Analyse** - Analyse und Auswertung der vorliegenden Daten
            3. 📈 **Visualisierung** - Explorative Datenanalyse
            4. 🤖 **Maschine Learning** - Maschine Learning Modellierung und Vorhersage
            """)

st.markdown("""---""")
st.subheader("📚 Informationen zum Datensatz")
col1, col2, col3, col4 = st.columns(4)

with col1:
    card("Zeilen", len(df))
with col2:
    card("Features", len(df.columns))
with col3:
    card("Berufe", len(df["job_role"].value_counts()))
with col4:
    card("Branchen", len(df["industry"].value_counts()))

st.markdown("""\n""")

left, right = st.columns([1, 1])
with left:
    st.markdown(
        "<h4 style='text-align: center;'>Verteilung der Geschlechter</h4>",
        unsafe_allow_html=True
    )
    if "gender" in df.columns:
       

        gender_counts = (
            df["gender"]
            .value_counts()
            .reset_index()
        )

        gender_counts.columns = ["gender", "count"]

        fig_gender = px.pie(
            gender_counts,
            values="count",
            names="gender",
            hole=0.5
        )

        fig_gender.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            height=200
        )

        st.plotly_chart(
            fig_gender,
            use_container_width=True
        )

    else:
        st.info("Keine Gender-Spalte gefunden.")
with right:
    if "seniority_level" in df.columns:
        st.markdown(
            "<h4 style='text-align: center;'>Verteilung hierarchischer Positionen</h4>",
            unsafe_allow_html=True
        )

        seniority_level_counts = (
            df["seniority_level"]
            .value_counts()
            .reset_index()
        )

        seniority_level_counts.columns = ["seniority_level", "count"]

        fig_seniority_level = px.pie(
            seniority_level_counts,
            values="count",
            names="seniority_level",
            hole=0.5
        )

        fig_seniority_level.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            height=200
        )

        st.plotly_chart(
            fig_seniority_level,
            use_container_width=True
        )

    else:
        st.info("Keine Seniority-Level-Spalte gefunden.")


st.markdown("""---""")
st.subheader(" 🆘 Hilfsangebote")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(f"""
        <a href="https://www.116117.de/de/psychotherapie.php" target="_blank">
            <img src="data:image/svg+xml;base64,{get_base64_encoded_image("assets/logo_116117.svg")}" width="200"/>
        </a>
    """, unsafe_allow_html=True)
    st.markdown(""" \n""")
    st.markdown(f"""
        <a href="https://www.deutsche-depressionshilfe.de/" target="_blank">
            <img src="data:image/svg+xml;base64,{get_base64_encoded_image("assets/stiftung-deutsche-depressionshilfe-und-suizidpraevention-logo.svg")}" width="200"/>
        </a>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        **116117**: Unter der Nummer 116117 können Sie rund um die Uhr einen Termin beiPsychotherapeut\*innen vereinbaren. 
        Es handelt sich um eine kostenlose Service-Hotline, die von der Kassenärztlichen Bundesvereinigung betrieben wird.
        Über die Webseite können verfügbare Termine bei Psychotherapeut*innen in Ihrer Nähe eingesehen und gebucht werden.
    """)
    st.markdown(""" \n""")
    st.markdown("""
        **Deutsche Depressionshilfe**: Die Stiftung Deutsche Depressionshilfe bietet umfangreiche Informationen, Beratung und Unterstützung für Menschen, die von Depressionen betroffen sind, sowie für deren Angehörige.
    """)



st.markdown("""---""")
st.subheader("""⬇️ Ressourcen & Downloads""")

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


st.markdown("""---""")
st.markdown("""<span style="font-size: 0.85rem; color: #555a;">DataPy SoSe26 - Mental Health in Tech Project</span>""", unsafe_allow_html=True)