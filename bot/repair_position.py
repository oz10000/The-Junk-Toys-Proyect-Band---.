# bot/repair_position.py
"""
Reconstruye el estado de posiciones desde el exchange.
"""

class RepairPosition:
    def __init__(self, exchange_engine):
        self.exchange = exchange_engine

    def repair(self, symbol):
        position = self.exchange.get_position(symbol)
        if position is None:
            return None
        # Sincronizar estado
        return position
