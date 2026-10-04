import sqlite3
from config import DB_PATH

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM Товар")
print(f"Товаров в базе: {cur.fetchone()[0]}")
conn.close()
