# streamlit/pages/statistics.py
import streamlit as st
import pandas as pd

def render():
    st.header("📊 Estadísticas del Sistema")
    # Ejemplo de tablas
    st.subheader("Rendimiento por Activo")
    df = pd.DataFrame({
        'Activo': ['BTC', 'ETH', 'SOL'],
        'Win Rate': ['87%', '85%', '84%'],
        'Profit Factor': ['1.58', '1.49', '1.42']
    })
    st.table(df)
