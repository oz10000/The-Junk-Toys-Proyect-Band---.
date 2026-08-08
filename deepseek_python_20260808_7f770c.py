# streamlit/pages/exchanges.py
"""
Página: Exchanges conectados y Wise Integration.
"""

import streamlit as st
from config.exchanges import EXCHANGE_CONFIGS
from infrastructure.exchanges import ExchangeFactory
from infrastructure.wise_integration import WiseIntegration

def render():
    st.header("🏦 Exchanges y Wise Integration")

    st.subheader("📊 Exchanges Conectados")
    for ex_id, cfg in EXCHANGE_CONFIGS.items():
        status = "✅" if cfg.get('enabled', False) else "❌"
        st.write(f"{status} **{cfg['name']}** ({cfg['type']}) — Prioridad {cfg.get('priority', 0)}")

    st.markdown("---")
    st.subheader("💱 Wise Integration — Monedas Soportadas")

    wise = WiseIntegration()
    df_wise = wise.get_wise_table()
    st.dataframe(df_wise, use_container_width=True)

    st.subheader("🔄 Conversor de Monedas Wise")
    col1, col2 = st.columns(2)
    with col1:
        from_cur = st.selectbox("Desde", wise.get_wise_supported_list(), index=0)
        amount = st.number_input("Cantidad", min_value=0.0, value=100.0)
    with col2:
        to_cur = st.selectbox("Hasta", wise.get_wise_supported_list(), index=1)
        if st.button("Calcular conversión"):
            result = wise.convert(amount, from_cur, to_cur)
            if result is not None:
                st.success(f"💰 {amount:.2f} {from_cur} = {result:.2f} {to_cur}")
            else:
                st.warning("No se pudo obtener la tasa de cambio")