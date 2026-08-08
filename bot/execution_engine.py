# bot/execution_engine.py
from domain.entities.order import Order, Direction, OrderType
from domain.value_objects import Price

class ExecutionEngine:
    def __init__(self, exchange_engine):
        self.exchange = exchange_engine

    def execute(self, signal, capital):
        order = Order(
            symbol=signal.symbol,
            direction=signal.direction,
            order_type=OrderType.MARKET,
            price=signal.entry_price,
            quantity=capital / signal.entry_price.value
        )
        return self.exchange.execute_market_order(order)
