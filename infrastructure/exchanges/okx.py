# infrastructure/exchanges/okx.py
import ccxt
import pandas as pd
from infrastructure.exchanges.base import BaseExchange

class OKXExchange(BaseExchange):
    """Implementación del exchange OKX."""

    def __init__(self):
        super().__init__('OKX')
        self._exchange = ccxt.okx({
            'enableRateLimit': True,
            'options': {'defaultType': 'swap'}
        })

    def connect(self) -> bool:
        try:
            self._exchange.load_markets()
            self._connected = True
            return True
        except Exception:
            self._connected = False
            return False

    def disconnect(self) -> bool:
        self._connected = False
        return True

    def fetch_ohlcv(self, symbol, timeframe, limit):
        if not self._connected:
            return None
        try:
            okx_sym = symbol.replace('/', '-').replace('USDT', 'USDT-SWAP')
            ohlcv = self._exchange.fetch_ohlcv(okx_sym, timeframe, limit=limit)
            if not ohlcv:
                return None
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            return df.astype(float)
        except Exception:
            return None

    def fetch_ticker(self, symbol):
        if not self._connected:
            return {}
        try:
            okx_sym = symbol.replace('/', '-').replace('USDT', 'USDT-SWAP')
            return self._exchange.fetch_ticker(okx_sym)
        except Exception:
            return {}

    def fetch_order_book(self, symbol, depth):
        if not self._connected:
            return {}
        try:
            okx_sym = symbol.replace('/', '-').replace('USDT', 'USDT-SWAP')
            return self._exchange.fetch_order_book(okx_sym, limit=depth)
        except Exception:
            return {}

    def fetch_funding_rate(self, symbol):
        if not self._connected:
            return 0.0
        try:
            okx_sym = symbol.replace('/', '-').replace('USDT', 'USDT-SWAP')
            funding = self._exchange.fetch_funding_rate(okx_sym)
            return funding.get('fundingRate', 0.0)
        except Exception:
            return 0.0

    def health_check(self) -> bool:
        try:
            self._exchange.fetch_time()
            return True
        except Exception:
            return False
