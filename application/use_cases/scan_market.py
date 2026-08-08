# application/use_cases/scan_market.py
"""
Caso de uso: Escaneo de mercado y generación de ranking.
"""

from typing import List, Dict, Optional
from domain.services.signal_service import SignalService
from domain.services.ranking_service import RankingService
from infrastructure.exchanges import ExchangeFactory
from infrastructure.cache import FileCache
from config import CONFIG

class ScanMarket:
    """Escanea el mercado y genera ranking de señales."""

    def __init__(self):
        self.exchange = ExchangeFactory.create('okx')
        self.cache = FileCache(CONFIG.cache_dir)
        self.signal_service = SignalService()
        self.ranking_service = RankingService(self.signal_service)

    def execute(self, symbols: Optional[List[str]] = None) -> Dict:
        """
        Ejecuta el escaneo y retorna ranking.
        """
        if symbols is None:
            symbols = CONFIG.universe

        all_signals = []
        data_dict = {}

        for symbol in symbols:
            # Intentar obtener desde caché
            df = self.cache.load(f"ohlcv_{symbol}_5m_300")
            if df is None:
                df = self.exchange.fetch_ohlcv(symbol, '5m', 300)
                if df is not None and not df.empty:
                    self.cache.save(f"ohlcv_{symbol}_5m_300", df)
            if df is not None and not df.empty:
                data_dict[symbol] = df
                signal = self.signal_service.generate(symbol, df)
                if signal is not None:
                    all_signals.append(signal)

        ranking = self.ranking_service.rank(all_signals)
        optimal = self.ranking_service.get_optimal(ranking)

        return {
            'ranking': ranking,
            'optimal': optimal,
            'signals': all_signals,
            'data': data_dict,
        }
