# infrastructure/cache.py
import os
import pickle
import hashlib
import pandas as pd
from typing import Optional

class FileCache:
    """Caché en disco con verificación de integridad."""

    def __init__(self, cache_dir: str = 'data/cache'):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    def _compute_checksum(self, df: pd.DataFrame) -> str:
        return hashlib.sha256(df.to_csv(index=False).encode()).hexdigest()

    def save(self, key: str, df: pd.DataFrame) -> bool:
        try:
            filepath = os.path.join(self.cache_dir, f"{key}.pkl")
            meta_path = os.path.join(self.cache_dir, f"{key}.meta")
            checksum = self._compute_checksum(df)
            with open(filepath, 'wb') as f:
                pickle.dump(df, f)
            with open(meta_path, 'w') as f:
                f.write(checksum)
            return True
        except Exception:
            return False

    def load(self, key: str) -> Optional[pd.DataFrame]:
        filepath = os.path.join(self.cache_dir, f"{key}.pkl")
        meta_path = os.path.join(self.cache_dir, f"{key}.meta")
        if not os.path.exists(filepath) or not os.path.exists(meta_path):
            return None
        try:
            with open(meta_path, 'r') as f:
                stored_checksum = f.read().strip()
            with open(filepath, 'rb') as f:
                df = pickle.load(f)
            current_checksum = self._compute_checksum(df)
            if current_checksum != stored_checksum:
                return None
            return df
        except Exception:
            return None
