# config/exchanges.py
"""
Configuración de exchanges y endpoints.
"""

from typing import Dict

EXCHANGE_CONFIGS: Dict[str, Dict] = {
    'okx': {
        'name': 'OKX',
        'type': 'swap',
        'endpoint': 'https://www.okx.com',
        'api_version': 'v5',
        'timeframes': ['1m', '3m', '5m', '15m', '30m', '1h', '4h', '1d'],
        'symbol_format': '{base}-{quote}-SWAP',
        'enabled': True,
        'priority': 1,
    },
    'kraken': {
        'name': 'Kraken',
        'type': 'spot',
        'endpoint': 'https://api.kraken.com',
        'api_version': '0',
        'timeframes': ['1m', '5m', '15m', '30m', '1h', '4h', '1d'],
        'symbol_format': '{base}/{quote}',
        'enabled': True,
        'priority': 2,
    },
    'kucoin': {
        'name': 'KuCoin',
        'type': 'spot',
        'endpoint': 'https://api.kucoin.com',
        'api_version': 'v1',
        'timeframes': ['1min', '5min', '15min', '30min', '1hour', '4hour', '1day'],
        'symbol_format': '{base}-{quote}',
        'enabled': True,
        'priority': 3,
    },
    'bybit': {
        'name': 'Bybit',
        'type': 'linear',
        'endpoint': 'https://api.bybit.com',
        'api_version': 'v5',
        'timeframes': ['1', '3', '5', '15', '30', '60', '120', '240', '360', '720', 'D', 'W', 'M'],
        'symbol_format': '{base}{quote}',
        'enabled': False,
        'priority': 4,
    },
    'binance': {
        'name': 'Binance',
        'type': 'spot',
        'endpoint': 'https://api.binance.com',
        'api_version': 'v3',
        'timeframes': ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d'],
        'symbol_format': '{base}{quote}',
        'enabled': False,
        'priority': 5,
    },
}

EXCHANGE_PRIORITY = [ex_id for ex_id, cfg in EXCHANGE_CONFIGS.items() if cfg['enabled']]
