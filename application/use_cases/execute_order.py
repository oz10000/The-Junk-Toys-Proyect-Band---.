# application/use_cases/execute_order.py
"""
Caso de uso: Ejecución de órdenes.
"""

from domain.services.order_service import OrderService

class ExecuteOrder:
    """Ejecuta una orden de compra/venta."""

    def __init__(self):
        self.order_service = OrderService()

    def execute(self, signal, capital):
        return self.order_service.execute(signal, capital)
