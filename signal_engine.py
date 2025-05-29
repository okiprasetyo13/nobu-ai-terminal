
from datetime import datetime
import numpy as np

def analyze_all_symbols():
    symbols = ["BTC", "ETH"]
    results = []

    for symbol in symbols:
        price = np.random.uniform(1000, 70000)
        rsi = np.random.uniform(10, 90)
        ema9 = price * np.random.uniform(0.98, 1.02)
        ema21 = price * np.random.uniform(0.96, 1.04)
        support = price * 0.98
        resistance = price * 1.02
        entry = price
        sl = price * 0.99
        tp = price * 1.01
        score = int(np.random.randint(1, 6))
        suitability = "Scalping" if rsi < 30 else "Long" if rsi < 70 else "Neutral"
        expert_tip = f"Buy now, target {tp:.0f}" if suitability != "Neutral" else "Wait"

        results.append({
            "Symbol": symbol,
            "Price": round(price, 2),
            "RSI": round(rsi, 2),
            "EMA9": round(ema9, 2),
            "EMA21": round(ema21, 2),
            "Support": round(support, 2),
            "Resistance": round(resistance, 2),
            "Entry": round(entry, 2),
            "SL": round(sl, 2),
            "TP": round(tp, 2),
            "Score": score,
            "Suitability": suitability,
            "Expert Tip": expert_tip,
            "Chart": "<img src='data:image/png;base64,...'/>"
        })

    return results
