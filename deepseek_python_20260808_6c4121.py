# infrastructure/persistence/sqlite_repository.py
import sqlite3
import json
from typing import List, Dict

class SQLiteRepository:
    def __init__(self, db_path='data/trades.db'):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            direction TEXT,
            entry_price REAL,
            exit_price REAL,
            pnl REAL,
            entry_time TEXT,
            exit_time TEXT,
            reason TEXT,
            metadata TEXT
        )''')
        conn.commit()
        conn.close()

    def save(self, trade: Dict):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''INSERT INTO trades (symbol, direction, entry_price, exit_price, pnl, entry_time, exit_time, reason, metadata)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (trade['symbol'], trade['direction'], trade['entry_price'], trade.get('exit_price', 0.0),
                   trade['pnl'], trade['entry_time'], trade.get('exit_time'), trade.get('reason', ''),
                   json.dumps(trade.get('metadata', {}))))
        conn.commit()
        conn.close()