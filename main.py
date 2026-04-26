import time
from trader import Trader

symbols=["BTCUSDT","ETHUSDT"]
trader=Trader()

while True:
    for s in symbols:
        print("扫描:",s)
    time.sleep(10)
