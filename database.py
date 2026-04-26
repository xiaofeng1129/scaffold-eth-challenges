import sqlite3
conn = sqlite3.connect("trades.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS trades (symbol TEXT, profit REAL)")
conn.commit()

def log_trade(symbol, profit):
    cursor.execute("INSERT INTO trades VALUES (?,?)",(symbol,profit))
    conn.commit()

def get_trades():
    return cursor.execute("SELECT * FROM trades").fetchall()
