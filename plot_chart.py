import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64

def plot_mini_chart(df, symbol=""):
    fig, ax = plt.subplots(figsize=(2.5, 1.5), dpi=100)
    ax.plot(df['close'].tail(30).values, linewidth=1.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(symbol, fontsize=6)
    ax.grid(False)
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close(fig)
    return f"data:image/png;base64,{image_base64}"
