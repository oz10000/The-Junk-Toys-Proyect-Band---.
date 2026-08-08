# streamlit/pages/exchanges.py
import streamlit as st
from config.exchanges import EXCHANGE_CONFIGS

def render():
    st.header("🏦 Exchanges Conectados")
    for ex_id, cfg in EXCHANGE_CONFIGS.items():
        status = "✅" if cfg.get('enabled', False) else "❌"
        st.write(f"{status} {cfg['name']} ({cfg['type']})")