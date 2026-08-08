# streamlit/pages/backtesting.py
"""
Página: Backtesting — Simulación histórica.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from config.base import CONFIG
from application.use_cases.run_backtest import RunBacktest

def render():
    st.header("📈 Backtesting")

    col1, col2 = st.columns(2)
    with col1:
        days = st.number_input("Días a simular", min_value=30, max_value=365, value=180)
    with col2:
        run_btn = st.button("🚀 Ejecutar Backtest", type="primary")

    if run_btn:
        with st.spinner("Ejecutando backtest..."):
            try:
                use_case = RunBacktest()
                result = use_case.execute(CONFIG.universe[:5], days=days)
                if result:
                    st.success("✅ Backtest completado")

                    # Mostrar métricas
                    st.subheader("📊 Métricas del Backtest")
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Win Rate", f"{result.get('win_rate', 0)*100:.1f}%")
                    col2.metric("Profit Factor", f"{result.get('profit_factor', 0):.2f}")
                    col3.metric("Sharpe", f"{result.get('sharpe', 0):.2f}")
                    col4.metric("Drawdown", f"{result.get('max_dd', 0)*100:.1f}%")

                    # Curva de capital
                    if 'equity' in result:
                        df_equity = pd.DataFrame(result['equity'])
                        fig = px.line(df_equity, x='timestamp', y='equity', title="📈 Curva de Capital")
                        st.plotly_chart(fig, use_container_width=True)

                    # Lista de trades
                    if 'trades' in result and result['trades']:
                        st.subheader("📋 Últimos Trades")
                        df_trades = pd.DataFrame(result['trades']).tail(10)
                        st.dataframe(df_trades, use_container_width=True)

                        csv = df_trades.to_csv(index=False)
                        st.download_button("⬇️ Descargar trades (CSV)", data=csv, file_name="backtest_trades.csv")
            except Exception as e:
                st.error(f"Error en backtest: {e}")
    else:
        st.info("Configura los parámetros y presiona 'Ejecutar Backtest'.")