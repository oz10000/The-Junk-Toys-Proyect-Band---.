# streamlit/pages/ranking.py
"""
Página: Ranking Completo — Top 10 Long y Short.
"""

import streamlit as st
import pandas as pd
from utils.formatters import format_price

def render(ranking):
    st.header("🏆 Ranking Completo")

    if not ranking:
        st.info("No hay señales válidas en este momento.")
        return

    # Separar Long y Short
    longs = [r for r in ranking if r['signal'].direction.value == 'Long']
    shorts = [r for r in ranking if r['signal'].direction.value == 'Short']

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🟢 Top Long")
        if longs:
            df_long = pd.DataFrame([{
                'Pos': i+1,
                'Activo': r['signal'].symbol,
                'Score': f"{r['signal'].score.value:.3f}",
                'ADX': f"{r['signal'].adx.value:.1f}",
                'KER': f"{r['signal'].ker.value:.2f}",
                'Confianza': f"{r['signal'].confidence*100:.1f}%",
                'Precio': format_price(r['signal'].entry_price.value),
            } for i, r in enumerate(longs[:10])])
            st.dataframe(df_long, use_container_width=True, hide_index=True)
        else:
            st.warning("No hay señales Long")

    with col2:
        st.subheader("🔴 Top Short")
        if shorts:
            df_short = pd.DataFrame([{
                'Pos': i+1,
                'Activo': r['signal'].symbol,
                'Score': f"{r['signal'].score.value:.3f}",
                'ADX': f"{r['signal'].adx.value:.1f}",
                'KER': f"{r['signal'].ker.value:.2f}",
                'Confianza': f"{r['signal'].confidence*100:.1f}%",
                'Precio': format_price(r['signal'].entry_price.value),
            } for i, r in enumerate(shorts[:10])])
            st.dataframe(df_short, use_container_width=True, hide_index=True)
        else:
            st.warning("No hay señales Short")

    # Detalles de cada señal
    st.markdown("---")
    st.subheader("📋 Detalles de las señales")
    for i, r in enumerate(ranking[:10]):
        s = r['signal']
        with st.expander(f"{i+1}. {s.symbol} — {s.direction.value} (Score: {s.score.value:.3f})"):
            st.json({
                "Score": s.score.value,
                "ADX": s.adx.value,
                "KER": s.ker.value,
                "ATR%": s.atr.pct,
                "Confianza": s.confidence,
                "Régimen": s.regime.value,
                "Entrada": s.entry_price.value,
                "SL": s.sl_price.value,
                "TP": s.tp_price.value,
                "Trailing": s.trailing_distance,
                "Break Even": s.break_even_trigger,
            })
