import threading
import json
import websocket
import pandas as pd

class WebSocketClient:
    def __init__(self, symbols):
        self.symbols = [symbol.lower() + "-usdt" for symbol in symbols]
        self.ws = None
        self.prices = {symbol.upper(): None for symbol in symbols}
        self.thread = None

    def on_message(self, ws, message):
        data = json.loads(message)
        if 'events' in data:
            for event in data['events']:
                symbol = event['product_id'].split("-")[0].upper()
                price = float(event['price'])
                self.prices[symbol] = price

    def on_error(self, ws, error):
        print("WebSocket error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket closed")

    def on_open(self, ws):
        subscribe_msg = {
            "type": "subscribe",
            "channel": "market_trades",
            "events": [{"type": "subscribe", "channel": "market_trades", "product_ids": self.symbols}]
        }
        ws.send(json.dumps(subscribe_msg))

    def start(self):
        url = "wss://advanced-trade-ws.coinbase.com"
        self.ws = websocket.WebSocketApp(
            url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
        )
        self.thread = threading.Thread(target=self.ws.run_forever)
        self.thread.daemon = True
        self.thread.start()

    def get_prices(self):
        return self.prices
