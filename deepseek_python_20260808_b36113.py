# streamlit/pages/btc_eth_sol.py
"""
Página: Análisis Independiente de Bitcoin, Ethereum y Solana.
"""

import streamlit as st
from domain.services.indicator_service import IndicatorService
from utils.formatters import format_price

def render(data_dict):
    st.header("📊 BTC / ETH / SOL — Análisis Independiente")

    symbols = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']
    results = {}

    for sym in symbols:
        df = data_dict.get(sym)
        if df is not None and not df.empty:
            adx = IndicatorService.compute_adx(df)
            regime = IndicatorService.compute_regime(df)
            score = IndicatorService.compute_pidelta_score(df)
            close = df['close'].iloc[-1]
            change_24h = (close - df['close'].iloc[-24]) / df['close'].iloc[-24] * 100 if len(df) > 24 else 0
            results[sym] = {
                'price': close,
                'change': change_24h,
                'adx': adx.value,
                'regime': regime.value,
                'score': score.value,
            }

    col1, col2, col3 = st.columns(3)

    with col1:
        if 'BTC/USDT' in results:
            btc = results['BTC/USDT']
            st.metric("₿ Bitcoin", format_price(btc['price']), delta=f"{btc['change']:.2f}%")
            st.write(f"ADX: {btc['adx']:.1f} | Régimen: {btc['regime']} | Score: {btc['score']:.3f}")

    with col2:
        if 'ETH/USDT' in results:
            eth = results['ETH/USDT']
            st.metric("⟠ Ethereum", format_price(eth['price']), delta=f"{eth['change']:.2f}%")
            st.write(f"ADX: {eth['adx']:.1f} | Régimen: {eth['regime']} | Score: {eth['score']:.3f}")

    with col3:
        if 'SOL/USDT' in results:
            sol = results['SOL/USDT']
            st.metric("◎ Solana", format_price(sol['price']), delta=f"{sol['change']:.2f}%")
            st.write(f"ADX: {sol['adx']:.1f} | Régimen: {sol['regime']} | Score: {sol['score']:.3f}")

    st.markdown("---")
    st.subheader("📊 Comparativa")
    if len(results) >= 2:
        # Fortaleza relativa
        strongest = max(results.items(), key=lambda x: x[1]['adx'])
        weakest = min(results.items(), key=lambda x: x[1]['adx'])
        st.success(f"💪 Más fuerte: {strongest[0]} (ADX: {strongest[1]['adx']:.1f})")
        st.warning(f"📉 Más débil: {weakest[0]} (ADX: {weakest[1]['adx']:.1f})")