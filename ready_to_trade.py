
import streamlit as st
import requests
import time

def app():
    st.markdown("## 🎯 Ready to Trade")

    # Symbol selection
    symbol = st.selectbox("Select Coin", ["BTC", "ETH", "SOL", "AVAX", "DOGE", "MATIC", "ADA", "LINK", "OP"])

    # Manual trade input
    entry_price = st.number_input("Entry Price", min_value=0.0, step=0.01, format="%.4f")
    stop_loss = st.number_input("Stop Loss (SL)", min_value=0.0, step=0.01, format="%.4f")
    take_profit = st.number_input("Take Profit (TP)", min_value=0.0, step=0.01, format="%.4f")

    # Fetch live price from Coinbase
    @st.cache_data(ttl=5)
    def fetch_live_price(symbol):
        pair = f"{symbol}-USDT"
        url = f"https://api.exchange.coinbase.com/products/{pair}/ticker"
        try:
            r = requests.get(url, timeout=10)
            return float(r.json()["price"])
        except:
            return None

    if st.button("Activate Trade Monitor"):
        if not entry_price or not stop_loss or not take_profit:
            st.warning("Please input Entry, SL and TP.")
        else:
            st.session_state[f"{symbol}_armed"] = {
                "entry": entry_price,
                "sl": stop_loss,
                "tp": take_profit,
                "start_time": time.time()
            }
            st.success(f"{symbol} trade activated ✅")

    # If this coin is armed, track it
    armed = st.session_state.get(f"{symbol}_armed")
    if armed:
        current_price = fetch_live_price(symbol)
        st.markdown(f"### 🔁 {symbol} Live Monitoring")

        if current_price:
            st.metric(label="Live Price", value=f"{current_price:.4f}")
            pnl = ((current_price - armed["entry"]) / armed["entry"]) * 100
            st.metric(label="PnL (%)", value=f"{pnl:.2f}%", delta=f"{pnl:.2f}%", delta_color="normal" if pnl >= 0 else "inverse")

            duration = time.time() - armed["start_time"]
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            st.markdown(f"⏱ Trade Duration: **{minutes}m {seconds}s**")

            if current_price <= armed["sl"]:
                st.error(f"⛔ STOP LOSS TRIGGERED! Price: {current_price}")
            elif current_price >= armed["tp"]:
                st.success(f"💰 TAKE PROFIT HIT! Price: {current_price}")
        else:
            st.warning("🔄 Fetching live price...")
