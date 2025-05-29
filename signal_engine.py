import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator
import numpy as np

def calculate_indicators(df):
    df['EMA9'] = EMAIndicator(close=df['close'], window=9).ema_indicator()
    df['EMA21'] = EMAIndicator(close=df['close'], window=21).ema_indicator()
    df['RSI'] = RSIIndicator(close=df['close'], window=14).rsi()
    return df

def detect_support_resistance(df):
    support = df['low'].rolling(window=20).min().iloc[-1]
    resistance = df['high'].rolling(window=20).max().iloc[-1]
    return support, resistance

def generate_signals(live_prices):
    results = []

    for symbol, df in live_prices.items():
        if df is None or len(df) < 21:
            continue

        df = calculate_indicators(df)
        support, resistance = detect_support_resistance(df)

        price = df['close'].iloc[-1]
        rsi = df['RSI'].iloc[-1]
        ema9 = df['EMA9'].iloc[-1]
        ema21 = df['EMA21'].iloc[-1]

        signal = "HOLD"
        if rsi < 30 and price < ema9 < ema21:
            signal = "BUY"
        elif rsi > 70 and price > ema9 > ema21:
            signal = "SELL"

        score = 0
        if signal == "BUY":
            score = round((ema21 - price) / price * 100, 2)
        elif signal == "SELL":
            score = round((price - ema21) / price * 100, 2)

        sl = round(support * 0.98, 8)
        tp = round(resistance * 0.98, 8)
        buy_price = round(support * 1.01, 8)

        # Determine trading suitability
        suitability = "Scalping"
        if rsi > 70:
            suitability = "Short Trading"
        elif rsi < 30:
            suitability = "Long Trading"

        # Volume approximation
        volume = round(df['volume'].iloc[-20:].mean(), 2)

        results.append({
            "Symbol": symbol,
            "Price": price,
            "Signal": signal,
            "Score": score,
            "RSI": round(rsi, 2),
            "EMA9": round(ema9, 2),
            "EMA21": round(ema21, 2),
            "Support": round(support, 8),
            "Resistance": round(resistance, 8),
            "Buy Price": buy_price,
            "SL": sl,
            "TP": tp,
            "Volume": volume,
            "Suitability": suitability,
            "Active": signal == "BUY"
        })

    return pd.DataFrame(results)
