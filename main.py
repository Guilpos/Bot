import tkinter as tk
import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("59a774aaa984421e42c4b7a5c6e58b5793e18413d37d238223bf96f658645a21", "24eab36e14e3ec465205884a3dab9fb08417bf002aceae74d8ea1c2cbd4434a4", True)
    bitmex = BitmexClient("auFZp6pRKUGtJOWvCvp2rmel", "wZeKgxo6utwIA1I5lna9_UglGn0ZZQTArp_TNLr5sw2ETBk-", True)



    root = tk.Tk()
    root.mainloop()
