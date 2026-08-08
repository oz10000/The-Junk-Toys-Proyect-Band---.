# streamlit/pages/trade_optimal.py
"""
Página: Trade Óptimo — Mejor señal actual con todos los parámetros.
"""

import streamlit as st
import pandas as pd
from utils.formatters import format_price, format_currency, format_pct

def render(optimal):
    st.header("🎯 Trade Óptimo")

    if optimal is None:
        st.info("No hay señales válidas en este momento. Presiona 'Escanear Mercado'.")
        return

    signal = optimal['signal']
    metrics = optimal.get('metrics', {})

    # Tarjeta principal
    st.markdown(f"""
    <div class="trade-card">
        <h3>📈 {signal.symbol} — {signal.direction.value}</h3>
        <p><b>Score:</b> {signal.score.value:.3f} | 
           <b>Confianza:</b> {signal.confidence*100:.1f}% | 
           <b>Régimen:</b> {signal.regime.value}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("📊 Entrada")
        st.metric("Precio", format_price(signal.entry_price.value))
        st.metric("Dirección", signal.direction.value)
        st.metric("Leverage", f"{metrics.get('leverage', 3)}x")

    with col2:
        st.subheader("🛑 Stop Loss")
        st.metric("Precio", format_price(signal.sl_price.value))
        sl_pct = (signal.sl_price.value / signal.entry_price.value - 1) * 100
        st.metric("Porcentaje", f"{sl_pct:.2f}%")
        st.metric("Risk/Reward", f"{signal.risk_reward_ratio():.2f}")

    with col3:
        st.subheader("🎯 Take Profit")
        st.metric("Precio", format_price(signal.tp_price.value))
        tp_pct = (signal.tp_price.value / signal.entry_price.value - 1) * 100
        st.metric("Porcentaje", f"{tp_pct:.2f}%")

    st.markdown("---")
    st.subheader("📋 Detalles adicionales")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write(f"**ADX:** {signal.adx.value:.1f}")
        st.write(f"**KER:** {signal.ker.value:.3f}")
        st.write(f"**ATR%:** {signal.atr.pct:.2f}%")
    with col_b:
        st.write(f"**Trailing:** {signal.trailing_distance*100:.1f}%")
        st.write(f"**Break Even:** {signal.break_even_trigger*100:.1f}%")
        st.write(f"**Tiempo máx:** {signal.max_hold_minutes} min")

    # Soportes y resistencias
    if signal.support_price or signal.resistance_price:
        st.markdown("---")
        st.subheader("📊 Soportes y Resistencias")
        c1, c2 = st.columns(2)
        with c1:
            if signal.support_price:
                st.metric("Soporte", format_price(signal.support_price.value))
        with c2:
            if signal.resistance_price:
                st.metric("Resistencia", format_price(signal.resistance_price.value))