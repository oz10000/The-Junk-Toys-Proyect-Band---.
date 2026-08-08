# streamlit/pages/settings.py
"""
Página: Configuración del sistema.
"""

import streamlit as st
from config.base import CONFIG
from config.assets import ASSETS
from config.exchanges import EXCHANGE_CONFIGS

def render():
    st.header("⚙️ Configuración del Sistema")

    st.subheader("📊 Parámetros Generales")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Timeframe:** {CONFIG.timeframe}")
        st.write(f"**Capital inicial:** ${CONFIG.initial_capital:,.2f}")
        st.write(f"**Comisión:** {CONFIG.commission*100:.2f}%")
    with col2:
        st.write(f"**Score mínimo:** {CONFIG.min_score}")
        st.write(f"**ADX umbral:** {CONFIG.adx_threshold}")
        st.write(f"**KER umbral:** {CONFIG.ker_threshold}")

    st.subheader("📊 Activos")
    st.write(f"**Activos configurados:** {len(ASSETS)}")
    st.code(", ".join(ASSETS))

    st.subheader("📊 Exchanges")
    for ex_id, cfg in EXCHANGE_CONFIGS.items():
        status = "✅" if cfg.get('enabled', False) else "❌"
        st.write(f"{status} {cfg['name']} ({cfg['type']})")

    st.subheader("📊 Riesgo")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Apalancamiento máx:** {CONFIG.max_leverage_global}x")
        st.write(f"**Riesgo por trade:** {CONFIG.risk_per_trade*100:.1f}%")
    with col2:
        st.write(f"**Máx posiciones:** {CONFIG.max_positions}")
        st.write(f"**Pérdida diaria máx:** {CONFIG.max_daily_loss_pct*100:.1f}%")