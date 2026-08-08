# domain/services/amplitude_service.py
import numpy as np
import pandas as pd

class AmplitudeService:
    @staticmethod
    def compute_atr_pct(df: pd.DataFrame, period: int = 14) -> float:
        high, low, close = df['high'], df['low'], df['close']
        tr = pd.concat([high - low, (high - close.shift()).abs(), (low - close.shift()).abs()], axis=1).max(axis=1)
        atr = tr.rolling(period).mean().iloc[-1]
        return (atr / close.iloc[-1]) * 100 if close.iloc[-1] > 0 else 0.0
