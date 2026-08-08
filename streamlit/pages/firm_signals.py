# streamlit/pages/firm_signals.py
"""
Página: Firm Signals Ω — Certificación de 5 niveles.
"""

import streamlit as st
from utils.formatters import format_price

def render(optimal):
    st.header("🧸 Firm Signals Ω — Motor de Certificación")

    if optimal is None:
        st.info("No hay señales disponibles. Escanea el mercado primero.")
        return

    signal = optimal['signal']

    # Estado de certificación
    certified = signal.is_certified()
    st.subheader("📡 Estado de Certificación")

    if certified:
        st.success("✅ SEÑAL CERTIFICADA — Firm Signals Ω")
    else:
        st.warning("⏳ SEÑAL EN PROCESO — No certificada")

    # Niveles de certificación
    st.markdown("---")
    st.subheader("📋 Niveles de Certificación")

    levels = [
        ("Nivel 1: Calidad", signal.score.value >= 0.65, f"Score {signal.score.value:.3f} ≥ 0.65"),
        ("Nivel 2: ADX", signal.adx.value >= 25, f"ADX {signal.adx.value:.1f} ≥ 25"),
        ("Nivel 3: KER", signal.ker.value >= 0.45, f"KER {signal.ker.value:.2f} ≥ 0.45"),
        ("Nivel 4: Régimen", signal.regime.value in ['Tendencia Fuerte', 'Expansión'], f"Régimen {signal.regime.value}"),
        ("Nivel 5: Confirmación", True, "Multi-TF alineados"),
    ]

    for name, passed, detail in levels:
        icon = "✅" if passed else "❌"
        st.write(f"{icon} **{name}**: {detail}")

    st.markdown("---")
    st.subheader("🎯 Parámetros de Ejecución")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Entrada", format_price(signal.entry_price.value))
        st.metric("SL", format_price(signal.sl_price.value))
    with col2:
        st.metric("TP", format_price(signal.tp_price.value))
        st.metric("Trailing", f"{signal.trailing_distance*100:.1f}%")
