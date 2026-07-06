import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "system_telemetry.db"


class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row

    def execute(self, query, params=None):
        cursor = self.conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        return cursor.fetchall()

    def get_tables(self):
        return self.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table';
        """)

    def get_schema(self, table_name):
        return self.execute(
            f"PRAGMA table_info({table_name});"
        )

    def close(self):
        self.conn.close()
