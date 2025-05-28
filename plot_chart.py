
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def render_chart(df, tp=None, sl=None):
    fig, ax = plt.subplots(figsize=(3, 1.5))
    ax.plot(df["close"], label="Price", linewidth=1)
    if "ema9" in df.columns:
        ax.plot(df["ema9"], "--", label="EMA9", linewidth=0.8)
    if "ema21" in df.columns:
        ax.plot(df["ema21"], ":", label="EMA21", linewidth=0.8)
    if tp:
        ax.axhline(tp, color="green", linestyle="--", linewidth=0.8, label="TP")
    if sl:
        ax.axhline(sl, color="red", linestyle="--", linewidth=0.8, label="SL")
    ax.set_xticks([]); ax.set_yticks([])
    ax.legend(fontsize="xx-small", loc="upper left", frameon=False)
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    return f'<img src="data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}" width="200"/>'
