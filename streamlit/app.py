# streamlit/app.py
import sys
import os

# ============================================================
# FORZAR RUTA PARA IMPORTAR MODULOS DESDE LA RAÍZ
# ============================================================
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
import pandas as pd
from datetime import datetime

# ============================================================
# IMPORTAR CONFIGURACIÓN
# ============================================================
try:
    from config import CONFIG
except ImportError:
    # Fallback: si no existe config/__init__.py, importar directamente
    from config.base import CONFIG

from application.use_cases.scan_market import ScanMarket
from infrastructure.exchanges import ExchangeFactory

# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================
st.set_page_config(
    page_title="🧸 JUNK TOYS Ω",
    page_icon="🧸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# ESTADO DE SESIÓN
# ============================================================
if 'initialized' not in st.session_state:
    st.session_state.exchange = ExchangeFactory.create('okx')
    st.session_state.scanner = ScanMarket()
    st.session_state.last_scan = None
    st.session_state.ranking = []
    st.session_state.optimal = None
    st.session_state.signals = []
    st.session_state.data_dict = {}
    st.session_state.initialized = True
    st.session_state.signal_history = []
    st.session_state.firm_signal_history = []

# ============================================================
# ESTILOS
# ============================================================
st.markdown("""
    <style>
        .reportview-container .main .block-container {
            background: linear-gradient(145deg, #fdf6e3 0%, #fce8b2 100%);
        }
        .sidebar .sidebar-content { background: #ffd700; }
        .stButton button {
            background-color: #ff6b6b;
            color: white;
            border-radius: 20px;
            border: 3px solid #ffd93d;
            font-weight: bold;
            font-size: 1.2rem;
            padding: 0.5rem 1.5rem;
        }
        .stButton button:hover {
            background-color: #ff4757;
            transform: scale(1.02);
        }
        .trade-card {
            background: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin: 10px 0;
            border-left: 5px solid #ffd700;
        }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# TÍTULO
# ============================================================
st.title("🧸🎉🧸 JUNK TOYS Ω 🧸🎉🧸")
st.subheader("🐻🐻🐻 Asistente de Ejecución Manual y Automática 🐻🐻🐻")
st.markdown("---")

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.image("https://img.icons8.com/emoji/96/000000/teddy-bear-emoji.png", width=80)
    st.header("⚙️ Configuración")
    st.caption(f"Versión: {CONFIG.version}")
    st.caption(f"Timeframe: {CONFIG.timeframe}")
    st.caption(f"Capital: ${CONFIG.initial_capital:,.2f}")

    st.markdown("---")
    st.header("🚀 Acciones")
    if st.button("🔄 Escanear Mercado", type="primary", use_container_width=True):
        with st.spinner("🔍 Escaneando activos..."):
            result = st.session_state.scanner.execute()
            st.session_state.ranking = result.get('ranking', [])
            st.session_state.optimal = result.get('optimal')
            st.session_state.signals = result.get('signals', [])
            st.session_state.data_dict = result.get('data', {})
            st.session_state.last_scan = datetime.now()
            for s in st.session_state.signals:
                if s.is_valid:
                    st.session_state.signal_history.append({
                        'timestamp': datetime.now(),
                        'symbol': s.symbol,
                        'direction': s.direction.value,
                        'score': s.score.value,
                        'is_valid': True
                    })
            if len(st.session_state.signal_history) > 100:
                st.session_state.signal_history = st.session_state.signal_history[-100:]
        st.rerun()

    st.markdown("---")
    st.header("📊 Estado")
    st.caption(f"Último escaneo: {st.session_state.last_scan.strftime('%H:%M:%S') if st.session_state.last_scan else 'Nunca'}")
    st.caption(f"Señales: {len(st.session_state.signals)}")
    st.caption(f"Activos: {len(CONFIG.universe)}")

# ============================================================
# PESTAÑAS
# ============================================================
tab_names = [
    "🎯 Trade Óptimo",
    "🏆 Ranking",
    "📈 Backtesting",
    "📊 BTC/ETH/SOL",
    "🧠 Optimización",
    "📈 Diagnóstico",
    "🏦 Exchanges & Wise",
    "🧸 Firm Signals Ω",
    "🤖 Bot Dashboard",
    "⚙️ Configuración"
]
tabs = st.tabs(tab_names)

# ============================================================
# CADA PESTAÑA LLAMA A SU RESPECTIVO RENDER
# ============================================================
with tabs[0]:
    try:
        from streamlit.pages.trade_optimal import render as render_trade_optimal
        render_trade_optimal(st.session_state.optimal)
    except ImportError:
        st.warning("Página 'Trade Óptimo' no disponible aún.")

with tabs[1]:
    try:
        from streamlit.pages.ranking import render as render_ranking
        render_ranking(st.session_state.ranking)
    except ImportError:
        st.warning("Página 'Ranking' no disponible aún.")

with tabs[2]:
    try:
        from streamlit.pages.backtesting import render as render_backtesting
        render_backtesting()
    except ImportError:
        st.warning("Página 'Backtesting' no disponible aún.")

with tabs[3]:
    try:
        from streamlit.pages.btc_eth_sol import render as render_btc_eth_sol
        render_btc_eth_sol(st.session_state.data_dict)
    except ImportError:
        st.warning("Página 'BTC/ETH/SOL' no disponible aún.")

with tabs[4]:
    try:
        from streamlit.pages.optimization import render as render_optimization
        render_optimization()
    except ImportError:
        st.warning("Página 'Optimización' no disponible aún.")

with tabs[5]:
    try:
        from streamlit.pages.diagnosis import render as render_diagnosis
        render_diagnosis(st.session_state.data_dict)
    except ImportError:
        st.warning("Página 'Diagnóstico' no disponible aún.")

with tabs[6]:
    try:
        from streamlit.pages.exchanges import render as render_exchanges
        render_exchanges()
    except ImportError:
        st.warning("Página 'Exchanges' no disponible aún.")

with tabs[7]:
    try:
        from streamlit.pages.firm_signals import render as render_firm_signals
        render_firm_signals(st.session_state.optimal)
    except ImportError:
        st.warning("Página 'Firm Signals Ω' no disponible aún.")

with tabs[8]:
    try:
        from streamlit.pages.bot_dashboard import render as render_bot
        render_bot()
    except ImportError:
        st.warning("Página 'Bot Dashboard' no disponible aún.")

with tabs[9]:
    try:
        from streamlit.pages.settings import render as render_settings
        render_settings()
    except ImportError:
        st.warning("Página 'Configuración' no disponible aún.")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption(f"🧸 JUNK TOYS Ω — v{CONFIG.version} 🧸🐻🎉")
st.caption("💜 Apoya el proyecto: Alias `walywasaby` (Prex) | USDT TRC20: `TCiRVXggAqDx6bhJH5KBdf8E4NcJ2voMf8`")
