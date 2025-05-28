
import streamlit as st
import pandas as pd
import ready_to_trade
from signal_engine import analyze_all_symbols

# Load results first
results = analyze_all_symbols()
df = pd.DataFrame(results)

st.set_page_config(page_title="Nobu AI Terminal Pro", layout="wide")
st.title("📡 Nobu AI Terminal Pro – Expert Scalping Terminal")

tabs = st.tabs(["Live Signal Scanner", "Ready to Trade", "Market Overview"])

with tabs[0]:
    st.markdown("### 📊 Live Scalping Signal Table")
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

with tabs[1]:
    ready_to_trade.app()  # ✅ This actually runs the trade panel UI

with tabs[2]:
    st.markdown("🚧 Market Overview coming soon...")
