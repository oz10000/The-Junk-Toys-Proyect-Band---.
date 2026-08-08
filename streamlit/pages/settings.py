# streamlit/pages/settings.py
import streamlit as st
from config.base import CONFIG

def render():
    st.header("⚙️ Configuración")
    st.json({
        "timeframe": CONFIG.timeframe,
        "min_score": CONFIG.min_score,
        "adx_threshold": CONFIG.adx_threshold,
        "max_leverage": CONFIG.max_leverage_global,
    })
