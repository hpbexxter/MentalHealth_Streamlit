import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


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
        nbins = st.slider("Intervalle im Diagramm", min_value=10, max_value=100, value=50, step=1)

        # Histogramm mit Plotly Express erstellen und ausgeben
        fig = px.histogram(df, x=selected_col, nbins=nbins, title=f"Verteilung von {selected_col}")
        st.plotly_chart(fig)

    with tab2:
        st.subheader("Korrelationen zwischen Features")
        st.write("Hier können Sie die Korrelationen zwischen den verschiedenen Features visualisieren. Wählen Sie zwei oder mehr Features aus, um die entsprechenden Korrelationen anzuzeigen.")

    with tab3:
        st.subheader("Vergleiche zwischen Gruppen")
        st.write("Hier können Sie Vergleiche zwischen verschiedenen Gruppen innerhalb Ihrer Daten visualisieren. Wählen Sie ein Feature aus, um die entsprechenden Gruppenvergleiche anzuzeigen.")
    