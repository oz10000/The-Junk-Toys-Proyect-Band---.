# streamlit/components/metric_card.py
"""
Componente: Tarjeta de métrica.
"""

import streamlit as st

def render(label, value, delta=None, delta_color="normal"):
    st.metric(label=label, value=value, delta=delta, delta_color=delta_color)