# domain/entities/position.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from domain.value_objects import Direction, Price

@dataclass
class Position:
    symbol: str
    direction: Direction
    entry_price: Price
    current_price: Price
    size: float
    leverage: int
    entry_time: datetime
    sl_price: Optional[Price] = None
    tp_price: Optional[Price] = None
    trailing_active: bool = False
    trailing_sl: Optional[Price] = None
    be_activated: bool = False
    status: str = 'OPEN'
    unrealized_pnl: float = 0.0
    realized_pnl: float = 0.0
    close_time: Optional[datetime] = None