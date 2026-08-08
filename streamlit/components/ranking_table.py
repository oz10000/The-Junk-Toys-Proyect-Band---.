# streamlit/components/ranking_table.py
"""
Componente: Tabla de ranking.
"""

import streamlit as st
import pandas as pd
from utils.formatters import format_price

def render(ranking, title="Ranking"):
    if not ranking:
        st.info("No hay señales")
        return

    df = pd.DataFrame([{
        'Pos': i+1,
        'Activo': r['signal'].symbol,
        'Score': f"{r['signal'].score.value:.3f}",
        'ADX': f"{r['signal'].adx.value:.1f}",
        'KER': f"{r['signal'].ker.value:.2f}",
        'Confianza': f"{r['signal'].confidence*100:.1f}%",
        'Precio': format_price(r['signal'].entry_price.value),
    } for i, r in enumerate(ranking[:10])])

    st.dataframe(df, use_container_width=True, hide_index=True)
