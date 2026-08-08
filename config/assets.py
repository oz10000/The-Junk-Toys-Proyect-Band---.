# config/assets.py
"""
Configuración de activos y parámetros por activo.
"""

from typing import Dict, List

ASSETS: List[str] = [
    'BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'XRP/USDT', 'LTC/USDT',
    'BNB/USDT', 'ADA/USDT', 'DOGE/USDT', 'AVAX/USDT'
]

ASSET_PARAMS: Dict[str, Dict] = {
    'BTC/USDT': {'min_score': 0.30, 'adx_threshold': 22, 'ker_threshold': 0.42},
    'ETH/USDT': {'min_score': 0.30, 'adx_threshold': 22, 'ker_threshold': 0.42},
    'SOL/USDT': {'min_score': 0.30, 'adx_threshold': 22, 'ker_threshold': 0.42},
    # ... se puede extender
}

MAX_LEVERAGE: Dict[str, int] = {
    'BTC/USDT': 8, 'ETH/USDT': 6, 'SOL/USDT': 5,
    'XRP/USDT': 5, 'LTC/USDT': 4, 'BNB/USDT': 5,
    'ADA/USDT': 4, 'DOGE/USDT': 3, 'AVAX/USDT': 4
}
