# streamlit/components/chart.py
"""
Componente: Gráfico interactivo.
"""

import streamlit as st
import plotly.express as px
import pandas as pd

def render_line(data, x_col, y_col, title="Gráfico"):
    if not data:
        st.warning("No hay datos para graficar")
        return
    df = pd.DataFrame(data)
    fig = px.line(df, x=x_col, y=y_col, title=title)
    st.plotly_chart(fig, use_container_width=True)