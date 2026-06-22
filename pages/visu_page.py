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
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Verteilungen", "🔗 Korrelationen", "🟥 Kerndichte", "🔎 Exploration"])
    feature_cols = [col for col in df.columns if "score" in col and col != "phq9_score"]

    with tab1:
        st.subheader("Exploration der Verteilungen numerischer Features")
        st.markdown("""
                    In diesem Abschnitt kann die Verteilung der nummerischen Features untersucht werden. Wähle über das Dropdown-Menü ein Feature aus, um dessen Verteilung als Histogramm darzustellen. Mit dem Schieberegler kannst du die Anzahl der Intervalle (nbins) im Diagramm anpassen um die Detailliertheit der Darstellung zu steuern.
                    """)

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
        st.markdown("""
                    Die Korrelationsmatrix zeigt die paarweisen Korrelationen zwischen allen numerischen Features im Datensatz. Je höher der absolute Wert der Korrelation, desto stärker ist die Beziehung zwischen den beiden Features. Positive Werte deuten auf eine direkte Beziehung hin, während negative Werte auf eine inverse Beziehung hindeuten.
                    """)
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
        st.markdown("""
                    Diese Heatmap zeigt die Korrelationen aller numerischen Features mit dem PHQ-9 Score. Je höher die Korrelation, desto stärker ist der Zusammenhang zwischen dem Feature und dem PHQ-9 Score. Positive Werte deuten auf eine direkte Beziehung hin, während negative Werte auf eine inverse Beziehung hindeuten.
                    """)
        
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
        st.markdown("""
                    Diese Heatmap zeigt den durchschnittlichen PHQ-9 Score für verschiedene Kombinationen von Jobrollen und Senioritätsleveln. Je höher der Wert, desto höher ist der durchschnittliche PHQ-9 Score für diese Gruppe. Dadurch können potenzielle Risikogruppen identifiziert werden.
                    """)

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
        st.markdown("""
                    Eine Kerndichte-Schätzung (KDE) ermöglicht es, die Verteilung von Datenpunkten in einem kontinuierlichen Raum zu visualisieren. In diesem Abschnitt können zwei Features ausgewählt werden, um ihre gemeinsame Verteilung als Kontur- oder Flächendiagramm darzustellen. Je höher die Dichte in einem Bereich, desto mehr Datenpunkte befinden sich dort und desto dunkler ist die Darstellung.
                    """)
        
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
        st.markdown("""
                    In diesem Abschnitt können zwei Features ausgewählt werden, um ihre Beziehung zum PHQ-9 Score in einem Hexbin-Diagramm zu visualisieren. Je höher die durchschnittlichen PHQ-9 Scores in einem Bereich, desto dunkler ist die Farbe. Dadurch können potenzielle Zusammenhänge zwischen den Features und dem PHQ-9 Score identifiziert werden.
                    """)

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