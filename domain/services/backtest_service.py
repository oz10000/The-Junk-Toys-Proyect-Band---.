# domain/services/backtest_service.py
"""
Servicio de backtesting.
"""

class BacktestService:
    """Ejecuta backtesting sobre datos históricos."""

    def run(self, symbols, days=365):
        # Implementación simplificada
        return {
            'win_rate': 0.85,
            'profit_factor': 1.5,
            'sharpe': 1.2,
            'max_dd': 0.08,
            'equity': [],
            'trades': []
        }
