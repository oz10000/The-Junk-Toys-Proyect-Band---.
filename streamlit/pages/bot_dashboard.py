# streamlit/pages/bot_dashboard.py
import streamlit as st

def render():
    st.header("🤖 Bot Dashboard")
    st.info("Bot en modo demo. Conectado a OKX.")
    st.metric("Posiciones abiertas", "0")
    st.metric("Último escaneo", "Hace 2 min")
