import base64
from io import BytesIO
import matplotlib.pyplot as plt

# ✅ Simple chart generator
def generate_chart():
    plt.figure(figsize=(2, 1))
    plt.plot([1, 2, 3], [1, 4, 2], linewidth=2)
    plt.title('Chart')
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    return f"<img src='data:image/png;base64,{image_base64}'/>"

# ✅ Simulated live signal results
def analyze_all_symbols():
    return [
        {
            "Symbol": "BTC",
            "Price": 45500.75,
            "RSI": 61.3,
            "EMA9": 45200.10,
            "EMA21": 45750.85,
            "Support": 45000.0,
            "Resistance": 46000.0,
            "Entry": 45300.0,
            "SL": 45050.0,
            "TP": 45850.0,
            "Score": 4,
            "Suitability": "Scalping",
            "Expert Tip": "Buy now, breakout expected",
            "Chart": generate_chart()
        },
        {
            "Symbol": "ETH",
            "Price": 3250.25,
            "RSI": 58.9,
            "EMA9": 3220.55,
            "EMA21": 3265.90,
            "Support": 3200.0,
            "Resistance": 3300.0,
            "Entry": 3240.0,
            "SL": 3210.0,
            "TP": 3280.0,
            "Score": 3,
            "Suitability": "Long",
            "Expert Tip": "MACD confirmed entry",
            "Chart": generate_chart()
        }
    ]
