# domain/services/support_resistance_service.py
"""
Detección de soportes, resistencias y pivots.
"""

import pandas as pd
import numpy as np
from typing import List, Tuple

class SupportResistanceService:
    @staticmethod
    def find_pivots(df: pd.DataFrame, window: int = 5) -> Tuple[List[float], List[float]]:
        high = df['high'].values
        low = df['low'].values
        supports, resistances = [], []
        for i in range(window, len(high) - window):
            if high[i] == max(high[i-window:i+window+1]):
                resistances.append(high[i])
            if low[i] == min(low[i-window:i+window+1]):
                supports.append(low[i])
        return supports, resistances