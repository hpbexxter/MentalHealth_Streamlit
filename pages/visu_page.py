import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
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
    tab1, tab2, tab3, tab4 = st.tabs(["Verteilungen", "Korrelationen", "Kerndichte", "Vergleiche"])
    feature_cols = [col for col in df.columns if "score" in col and col != "phq9_score"]

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
        st.subheader("Korrelationsmatrix aller numerischen Features")
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

        st.subheader("Heatmap der Feature-Korrelationen mit PHQ-9")
        
        # Korrelationen mit PHQ-9 Score berechnen und sortieren
        phq_corr = df.select_dtypes(include='number').corr()[['phq9_score']].drop('phq9_score').sort_values('phq9_score', ascending=False)

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
        st.pyplot(fig)

        st.markdown("""---""")
        st.subheader("Durchschnittlicher PHQ-9 Score nach Jobrolle und Senioritätslevel")
        pivot = df.pivot_table(
        values="phq9_score",
        index="job_role",
        columns="seniority_level",
        aggfunc="mean"
        )

        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(
            pivot,
            annot=True,
            fmt=".1f",          
            cmap="Reds",
            vmin=0,
            vmax=27,
            ax=ax
        )
        st.pyplot(fig)
        
    with tab3:
        st.subheader("Kerndichte der Scores")
        
        selected_kde_first = st.selectbox("Erstes Feature", feature_cols, key="kde_first", index=0)
        selected_kde_second = st.selectbox("Zweites Feature", feature_cols, key="kde_second", index=1)

        samples = st.slider("Samples im Diagramm", min_value=100, max_value=len(df), value=10000, step=100)

        fig, ax = plt.subplots()
        sns.kdeplot(
            data=df.sample(samples),
            x=selected_kde_first,
            y=selected_kde_second,
            fill=True,
            cmap="Reds"
        )
        st.pyplot(fig)

    with tab4:

        st.subheader("Vergleich von Features")

        selected_hex_first = st.selectbox("Erstes Feature", feature_cols, key="hex_first", index=0)
        selected_hex_second = st.selectbox("Zweites Feature", feature_cols, key="hex_second", index=1)

        fig, ax = plt.subplots()
        hb = ax.hexbin(
            df[selected_hex_first],
            df[selected_hex_second],
            C=df["phq9_score"],
            reduce_C_function=np.mean,
            gridsize=30,
            cmap="RdYlGn_r"
        )
        plt.colorbar(hb, label="Ø PHQ-9")
        ax.set_xlabel(selected_hex_first)
        ax.set_ylabel(selected_hex_second)
        st.pyplot(fig)