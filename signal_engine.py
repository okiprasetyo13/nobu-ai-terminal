
import base64
from io import BytesIO
import matplotlib.pyplot as plt

# ✅ Simple chart plotter
def generate_chart(prices):
    plt.figure(figsize=(2, 1))
    plt.plot(prices, linewidth=2)
    plt.title("Mini Chart")
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    plt.close()
    return f"<img src='data:image/png;base64,{image_base64}'/>"

# ✅ Simulated real-time scalping signals
def analyze_all_symbols():
    return [
        {
            "Symbol": "BTC",
            "Price": 45516.75,
            "RSI": 61.58,
            "EMA9": 45203.25,
            "EMA21": 47336.99,
            "Support": 44600.00,
            "Resistance": 46000.00,
            "Entry": 45300.00,
            "SL": 44900.00,
            "TP": 45900.00,
            "Score": 4,
            "Suitability": "Scalping",
            "Expert Tip": "Buy now, breakout expected",
            "Chart": generate_chart([44000, 45000, 45200, 45500, 45800])
        },
        {
            "Symbol": "ETH",
            "Price": 32445.97,
            "RSI": 54.33,
            "EMA9": 32860.86,
            "EMA21": 32987.38,
            "Support": 31797.00,
            "Resistance": 33250.00,
            "Entry": 32300.00,
            "SL": 32000.00,
            "TP": 33000.00,
            "Score": 3,
            "Suitability": "Long",
            "Expert Tip": "MACD showing bullish divergence",
            "Chart": generate_chart([31000, 31500, 32000, 32500, 32800])
        }
    ]
