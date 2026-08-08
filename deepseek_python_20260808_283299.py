# streamlit/components/trade_card.py
"""
Componente: Tarjeta de señal.
"""

import streamlit as st
from utils.formatters import format_price

def render(signal):
    if signal is None:
        return

    st.markdown(f"""
    <div class="trade-card">
        <h3>📈 {signal.symbol} — {signal.direction.value}</h3>
        <p><b>Score:</b> {signal.score.value:.3f} | 
           <b>Confianza:</b> {signal.confidence*100:.1f}% | 
           <b>Régimen:</b> {signal.regime.value}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Entrada", format_price(signal.entry_price.value))
    col2.metric("SL", format_price(signal.sl_price.value))
    col3.metric("TP", format_price(signal.tp_price.value))