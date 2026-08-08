# config/__init__.py
from .base import CONFIG
from .exchanges import EXCHANGE_CONFIGS, EXCHANGE_PRIORITY
from .assets import ASSETS, ASSET_PARAMS, MAX_LEVERAGE
from .bot import BOT_CONFIG

__all__ = [
    'CONFIG',
    'EXCHANGE_CONFIGS',
    'EXCHANGE_PRIORITY',
    'ASSETS',
    'ASSET_PARAMS',
    'MAX_LEVERAGE',
    'BOT_CONFIG'
]
