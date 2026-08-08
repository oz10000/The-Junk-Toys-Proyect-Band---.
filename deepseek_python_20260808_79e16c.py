# streamlit/pages/bot_dashboard.py
"""
Página: Dashboard del Bot Automático.
"""

import streamlit as st
from datetime import datetime

def render():
    st.header("🤖 Bot Dashboard")

    st.info("El bot está en modo DEMO. No se ejecutan órdenes reales.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Estado", "🟢 Activo")
    col2.metric("Posiciones abiertas", "0")
    col3.metric("Último escaneo", datetime.now().strftime("%H:%M:%S"))

    st.markdown("---")
    st.subheader("📊 Estado del Bot")
    st.json({
        "exchange": "OKX",
        "mode": "demo",
        "scan_interval": "5 min",
        "max_positions": 3,
        "daily_trades": 0,
        "daily_limit": 10,
        "heartbeat": "OK",
        "health": "✅ Todos los sistemas operativos"
    })

    st.subheader("📋 Logs Recientes")
    st.code("""
[2026-08-08 14:32:01] 🔍 Escaneando mercado...
[2026-08-08 14:32:05] 📊 3 señales encontradas
[2026-08-08 14:32:06] ✅ Señal certificada: BTC/USDT LONG
[2026-08-08 14:32:07] ⏳ Simulando ejecución (modo demo)
    """)