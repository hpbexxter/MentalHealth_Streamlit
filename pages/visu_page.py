import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff


st.title("📈 Datenvisualisierung")

# Data
df = st.session_state.get("df", None)

if df is None:
    st.error("""
            ❌ Daten konnten nicht geladen werden. Bitte überprüfen Sie die Datenquelle und versuchen Sie es erneut.
            """)
else:
    # Tab Section
    tab1, tab2, tab3 = st.tabs(["Verteilungen", "Korrelationen", "Vergleiche"])

    with tab1:
        st.subheader("Verteilungen der Features")

        # Numerische Features aus dem Datensatz extrahieren
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    
        selected_col = st.selectbox("Feature auswählen", numeric_cols)

        # Anzahl der Intervalle für das Histogramm festlegen
        nbins = st.slider("Intervalle im Diagramm", min_value=10, max_value=100, value=50, step=10)

        # Histogramm mit Plotly Express erstellen und ausgeben
        fig = px.histogram(df, x=selected_col, nbins=nbins, title=f"Verteilung von {selected_col}")
        st.plotly_chart(fig)

    with tab2:
        st.subheader("Korrelationsmatrix")
        corr = df.select_dtypes(include='number').corr()

        fig = ff.create_annotated_heatmap(
            z=corr.values.round(2),
            x=list(corr.columns),
            y=list(corr.index),
            colorscale='RdBu',
            reversescale=True,
            showscale=True
        )

        for annotation in fig.layout.annotations:
            if float(annotation.text) > 0.7 or float(annotation.text) < -0.2:
                annotation.font.color = 'white'
            else:
                annotation.font.color = 'black'

        fig.update_layout(
            width=800,
            height=800,
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""---""")

        st.subheader("Heatmap der Korrelationen")
        phq_corr = df.select_dtypes(include='number').corr()[['phq9_score']].drop('phq9_score').sort_values('phq9_score')

        fig, ax = plt.subplots(figsize=(3, 5))
        sns.heatmap(
            phq_corr,
            annot=True,
            cmap="RdBu_r",
            center=0,
            vmin=-1,
            vmax=1,
            ax=ax
        )
        ax.set_title("Korrelationen mit PHQ-9")
        st.pyplot(fig)
        
    with tab3:
        st.subheader("Vergleiche zwischen Gruppen")
        st.write("Hier können Sie Vergleiche zwischen verschiedenen Gruppen innerhalb Ihrer Daten visualisieren. Wählen Sie ein Feature aus, um die entsprechenden Gruppenvergleiche anzuzeigen.")
    