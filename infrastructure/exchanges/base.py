# infrastructure/exchanges/base.py
from abc import ABC, abstractmethod

class BaseExchange(ABC):
    def __init__(self, name: str):
        self.name = name
        self._connected = False

    @abstractmethod
    def connect(self) -> bool: pass

    @abstractmethod
    def disconnect(self) -> bool: pass

    def is_connected(self) -> bool:
        return self._connected

    @abstractmethod
    def fetch_ohlcv(self, symbol, timeframe, limit): pass

    @abstractmethod
    def fetch_ticker(self, symbol): pass

    @abstractmethod
    def fetch_order_book(self, symbol, depth): pass

    @abstractmethod
    def fetch_funding_rate(self, symbol): pass

    @abstractmethod
    def health_check(self) -> bool: pass
