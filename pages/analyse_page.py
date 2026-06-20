import streamlit as st
import pandas as pd

st.title("Analyse")
st.write("Hier kommt der Seiteninhalt.")

# Data
df = st.session_state.get("df", None)

if df is None:
    st.error("""
            ❌ Daten konnten nicht geladen werden. Bitte überprüfen Sie die Datenquelle und versuchen Sie es erneut.
            """)
else:
    st.success(f"✅ Daten erfolgreich geladen. Datensatz enthält **{len(df)} Zeilen** und **{len(df.columns)} Spalten**.")

    # Tab Section
    tab1, tab2, tab3 = st.tabs(["🔢 Rohdaten", "📈 Statistiken", "🔎 Datenqualität"])

    with tab1:
        st.subheader("Vorschau der Daten")
        st.slider("Anzahl der angezeigten Zeilen", min_value=5, max_value=20, value=10, step=1, key="num_rows")
        st.dataframe(df.head(st.session_state.get("num_rows", 5)))

        st.markdown("""---""")
        st.subheader("Datentypen")

        # DataFrame mit den Datentypen der Spalten erstellen
        formated_df_dtypes = pd.DataFrame({
        "Feature": df.columns,
        "Datentyp": df.dtypes.values
        })
        # Ausgabe der Verteilung als Tabelle mit ausgeblendeten Index
        st.dataframe(formated_df_dtypes, hide_index=True)

    with tab2:
        st.subheader("Statistische Übersicht")
        st.dataframe(df.describe())

        st.subheader("Kategorische Variablen")
        categorical_cols = df.select_dtypes(include=["object", "category"]).columns
        if len(categorical_cols) > 0:
            # Ausgabe der Kategorien und deren Verteilung
            for col in categorical_cols:
                st.markdown(f"**{col}**")

                # Berechnung der Verteilung der Kategorien
                vc = df[col].value_counts().reset_index()
                vc.columns = [col, "Anzahl"]
                vc["Anteil (%)"] = (vc["Anzahl"] / vc["Anzahl"].sum() * 100).round(2)
                # Ausgabe der Verteilung als Tabelle mit ausgeblendeten Index
                st.dataframe(vc, hide_index=True)
        else:
            st.info("ℹ️ Es gibt keine kategorischen Variablen im Datensatz.")

    with tab3:
        st.subheader("Datenqualität")
        missing_values = df.isnull().sum()
        duplicate_rows = df.duplicated().sum()

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### Fehlende Werte")

            if missing_values.sum() > 0:
                st.warning(f"⚠️ Es gibt **{missing_values.sum()} fehlende Werte** in den Daten.")
                st.dataframe(missing_values[missing_values > 0], hide_index=True)
            else:
                st.success("✅ Es gibt keine fehlenden Werte in den Daten.")
                
        with col2:
            st.markdown("##### Doppelte Zeilen")
            if duplicate_rows > 0:
                st.warning(f"⚠️ Es gibt **{duplicate_rows} doppelte Zeilen** in den Daten.")
            else:
                st.success("✅ Es gibt keine doppelten Zeilen in den Daten.")