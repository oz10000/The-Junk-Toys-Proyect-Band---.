# config/bot.py
"""
Configuración específica del bot automático.
"""

from dataclasses import dataclass

@dataclass
class BotConfig:
    enabled: bool = False
    scan_interval_minutes: int = 5
    max_positions: int = 3
    max_daily_trades: int = 10
    stop_on_drawdown: float = 0.10
    require_confirmation: bool = True
    demo_mode: bool = True
    telegram_notifications: bool = False
    telegram_token: str = ''
    telegram_chat_id: str = ''
    email_notifications: bool = False
    email_recipient: str = ''

BOT_CONFIG = BotConfig()
