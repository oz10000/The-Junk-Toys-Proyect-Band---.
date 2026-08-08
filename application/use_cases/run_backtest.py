# application/use_cases/run_backtest.py
from domain.services.backtest_service import BacktestService

class RunBacktest:
    def __init__(self):
        self.service = BacktestService()

    def execute(self, symbols, days=365):
        return self.service.run(symbols, days)
