# config/base.py
"""
Parámetros base del sistema JUNK TOYS Ω.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class BaseConfig:
    # Timeframes
    timeframe: str = '5m'
    timeframes: List[str] = field(default_factory=lambda: ['1m', '3m', '5m', '15m', '30m', '1h', '4h', '1d'])
    primary_tf: str = '5m'
    lookback_days: int = 365

    # Capital y costes
    initial_capital: float = 10000.0
    commission: float = 0.0004
    slippage: float = 0.0005

    # Umbrales de señales
    min_score: float = 0.30
    adx_threshold: float = 22.0
    ker_threshold: float = 0.42

    # TP/SL
    tp_mult: float = 2.5
    sl_mult: float = 1.0

    # Trailing Stop
    trailing_distance: float = 0.008      # 0.8%
    trailing_activation: float = 0.012    # 1.2%
    trailing_callback: float = 0.003

    # Break Even
    break_even_trigger: float = 0.008
    break_even_buffer: float = 0.002

    # Gestión de tiempo
    max_hold_minutes: int = 120
    cooldown_minutes: int = 30

    # Riesgo
    max_leverage_global: int = 10
    risk_per_trade: float = 0.02
    max_positions: int = 3
    max_daily_loss_pct: float = 0.08
    min_risk_reward_ratio: float = 1.5

    # Horario (Argentina)
    hour_filter_start: int = 10
    hour_filter_end: int = 17
    use_hour_filter: bool = True

    # Zona horaria
    timezone: str = 'America/Argentina/Buenos_Aires'

    # Caché
    cache_dir: str = 'data/cache'
    ohlcv_dir: str = 'data/ohlcv'
    results_dir: str = 'data/results'
    wise_data_dir: str = 'data/wise'

    # Activos (se sobreescribe en assets.py)
    universe: List[str] = field(default_factory=lambda: [
        'BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'XRP/USDT', 'LTC/USDT',
        'BNB/USDT', 'ADA/USDT'
    ])
    max_leverage_by_asset: Dict[str, int] = field(default_factory=lambda: {
        'BTC/USDT': 8, 'ETH/USDT': 6, 'SOL/USDT': 5,
        'XRP/USDT': 5, 'LTC/USDT': 4, 'BNB/USDT': 5,
        'ADA/USDT': 4
    })

    # Versión
    version: str = '7.0.0'

    def __post_init__(self):
        import os
        for d in [self.cache_dir, self.ohlcv_dir, self.results_dir, self.wise_data_dir]:
            os.makedirs(d, exist_ok=True)

# Instancia global
CONFIG = BaseConfig()
