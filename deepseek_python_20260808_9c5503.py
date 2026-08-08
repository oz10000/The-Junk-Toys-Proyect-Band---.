# application/use_cases/manage_position.py
from domain.services.order_service import OrderService

class ManagePosition:
    def __init__(self):
        self.order_service = OrderService()

    def execute(self, position, current_price):
        return self.order_service.update(position, current_price)