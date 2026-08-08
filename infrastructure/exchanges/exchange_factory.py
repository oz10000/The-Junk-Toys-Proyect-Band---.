# infrastructure/exchanges/exchange_factory.py
"""
Factory para crear instancias de exchanges.
"""

from typing import Dict, Type
from infrastructure.exchanges.base import BaseExchange
from infrastructure.exchanges.okx import OKXExchange
from infrastructure.exchanges.kraken import KrakenExchange
from infrastructure.exchanges.kucoin import KuCoinExchange

class ExchangeFactory:
    _registry: Dict[str, Type[BaseExchange]] = {
        'okx': OKXExchange,
        'kraken': KrakenExchange,
        'kucoin': KuCoinExchange,
    }

    @classmethod
    def create(cls, exchange_id: str) -> BaseExchange:
        exchange_class = cls._registry.get(exchange_id.lower())
        if exchange_class is None:
            raise ValueError(f"Exchange {exchange_id} no soportado")
        return exchange_class()
