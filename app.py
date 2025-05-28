
import streamlit as st

st.set_page_config(page_title="Nobu AI Terminal", layout="wide")

st.title("📡 Nobu AI Terminal Pro")

tabs = st.tabs(["Live Signal Scanner", "Ready to Trade", "Market Overview"])

with tabs[0]:
    st.subheader("📈 Live Signal Scanner")
    st.markdown("⚠️ Signals not yet loaded. Please connect Coinbase WebSocket and indicator logic.")

with tabs[1]:
    st.subheader("🧠 Ready to Trade")
    st.markdown("⚙️ Feature under active development. This section will show trade breakdown per coin.")

with tabs[2]:
    st.subheader("📊 Market Overview")
    st.markdown("📌 A snapshot of the market trend, MACD, RSI and top coins will appear here.")

st.info("✅ Nobu AI Terminal v0.1 loaded successfully. Please update 'app.py' with full logic to enable live trading signals.")
