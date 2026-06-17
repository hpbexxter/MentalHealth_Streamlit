import streamlit as st

df = st.session_state["df"]

st.title("Übersicht")
st.dataframe(df.head())