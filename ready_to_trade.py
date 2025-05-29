
import streamlit as st
import requests
import time

def app():
    st.markdown("### 🎯 Ready to Trade")

    # Symbol selection
    symbol = st.selectbox("Select Coin", ["BTC", "ETH", "SOL", "AVAX", "DOGE", "MATIC", "ADA", "LINK", "OP"])

    # Manual trade input
    entry_price = st.number_input("Entry Price", min_value=0.0, step=0.01, format="%.4f")
    stop_loss = st.number_input("Stop Loss (SL)", min_value=0.0, step=0.01, format="%.4f")
    take_profit = st.number_input("Take Profit (TP)", min_value=0.0, step=0.01, format="%.4f")

    # Fetch live price from Coinbase (optional use)
    @st.cache_data(ttl=5)
    def fetch_live_price(symbol):
        pair = f"{symbol}-USD"
        url = f"https://api.exchange.coinbase.com/products/{pair}/ticker"
        try:
            r = requests.get(url, timeout=10)
            return float(r.json()["price"])
        except:
            return None

    live_price = fetch_live_price(symbol)
    if live_price:
        st.info(f"📡 Current {symbol} Price: {live_price:.4f} USD")

    # Trade activation
    if st.button("Activate Trade Monitor"):
        if not entry_price or not stop_loss or not take_profit:
            st.warning("⚠️ Please input all Entry, SL and TP values.")
        else:
            st.session_state[f"{symbol}_trade"] = {
                "entry": entry_price,
                "stop_loss": stop_loss,
                "take_profit": take_profit,
                "start_time": time.time()
            }
            st.success(f"✅ {symbol} trade activated and being monitored.")
