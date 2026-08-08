# streamlit/pages/diagnosis.py
"""
Página: Diagnóstico del mercado — Régimen, ADX, volatilidad.
"""

import streamlit as st
import pandas as pd
from domain.services.indicator_service import IndicatorService
from domain.services.diagnosis_service import DiagnosisService

def render(data_dict):
    st.header("📈 Diagnóstico del Mercado")

    if not data_dict:
        st.info("No hay datos disponibles. Escanea el mercado primero.")
        return

    # Diagnóstico global
    diagnosis = DiagnosisService()
    regimes = []
    adx_vals = []
    atr_vals = []

    for sym, df in data_dict.items():
        if df is not None and not df.empty:
            regime = diagnosis.get_regime(df)
            adx = IndicatorService.compute_adx(df)
            atr = IndicatorService.compute_atr(df)
            regimes.append(regime.value)
            adx_vals.append(adx.value)
            atr_vals.append(atr.pct)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📊 Régimen predominante", max(set(regimes), key=regimes.count) if regimes else "N/A")
    col2.metric("📉 ADX Promedio", f"{sum(adx_vals)/len(adx_vals):.1f}" if adx_vals else "N/A")
    col3.metric("📊 Volatilidad", f"{sum(atr_vals)/len(atr_vals):.2f}%" if atr_vals else "N/A")
    col4.metric("📊 Riesgo", "Moderado" if adx_vals and sum(adx_vals)/len(adx_vals) > 20 else "Alto")

    # Distribución de regímenes
    st.subheader("📊 Distribución de Regímenes")
    if regimes:
        df_regimes = pd.DataFrame({'Régimen': regimes})
        fig = px.pie(df_regimes, names='Régimen', title="Regímenes de Mercado")
        st.plotly_chart(fig, use_container_width=True)