# domain/entities/order.py
from dataclasses import dataclass
from datetime import datetime
from domain.value_objects import Direction, OrderType, Price

@dataclass
class Order:
    symbol: str
    direction: Direction
    order_type: OrderType
    price: Price
    quantity: float
    filled_quantity: float = 0.0
    status: str = 'PENDING'
    order_id: str = ''
    timestamp: datetime = None
    fee: float = 0.0
