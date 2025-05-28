
import pandas as pd
import requests
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator, MACDIndicator

symbols = ["BTC", "ETH", "SOL", "AVAX", "LTC", "DOGE", "MATIC", "ADA", "LINK", "OP"]
COINBASE_API = "https://api.exchange.coinbase.com/products/{}/candles"

def fetch_coinbase_candles(symbol, granularity=60, limit=100):
    pair = f"{symbol}-USDT"
    url = COINBASE_API.format(pair)
    params = {"granularity": granularity}
    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
        if isinstance(data, list):
            df = pd.DataFrame(data, columns=["time", "low", "high", "open", "close", "volume"])
            df.sort_values("time", inplace=True)
            return df
        else:
            return pd.DataFrame()
    except:
        return pd.DataFrame()

def analyze_symbol(symbol):
    df = fetch_coinbase_candles(symbol)
    if df.empty or len(df) < 30:
        return None

    df["ema9"] = EMAIndicator(df["close"], window=9).ema_indicator()
    df["ema21"] = EMAIndicator(df["close"], window=21).ema_indicator()
    df["rsi"] = RSIIndicator(df["close"]).rsi()
    df["macd"] = MACDIndicator(df["close"]).macd_diff()

    latest = df.iloc[-1]
    price = latest["close"]
    support = df["low"].rolling(20).min().iloc[-1]
    resistance = df["high"].rolling(20).max().iloc[-1]
    entry = price
    sl = price - (resistance - support) * 0.4
    tp = price + (resistance - support) * 0.6

    score = 0
    tip = "Wait"
    suit = "Neutral"

    if latest["rsi"] < 30 and latest["ema9"] > latest["ema21"] and latest["macd"] > 0:
        score = 4
        tip = "Buy signal confirmed"
        suit = "Scalping"
    elif latest["rsi"] > 70 and latest["ema9"] < latest["ema21"] and latest["macd"] < 0:
        score = 4
        tip = "Short signal confirmed"
        suit = "Short"
    elif latest["macd"] > 0:
        score = 2
        tip = "MACD trending up"
        suit = "Long"

    return {
        "Symbol": symbol,
        "Price": round(price, 2),
        "RSI": round(latest["rsi"], 2),
        "EMA9": round(latest["ema9"], 2),
        "EMA21": round(latest["ema21"], 2),
        "Support": round(support, 2),
        "Resistance": round(resistance, 2),
        "Entry": round(entry, 2),
        "SL": round(sl, 2),
        "TP": round(tp, 2),
        "Score": score,
        "Suitability": suit,
        "Expert Tip": tip
    }

def analyze_all_symbols():
    return [r for r in [analyze_symbol(s) for s in symbols] if r is not None]
