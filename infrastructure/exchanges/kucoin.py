# infrastructure/exchanges/kucoin.py
import ccxt
import pandas as pd
from infrastructure.exchanges.base import BaseExchange

class KuCoinExchange(BaseExchange):
    def __init__(self):
        super().__init__('KuCoin')
        self._exchange = ccxt.kucoin({'enableRateLimit': True})

    # Implementación similar a Kraken
