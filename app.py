import streamlit as st
import pandas as pd
import ready_to_trade
from signal_engine import analyze_all_symbols

# Page settings
st.set_page_config(page_title="Nobu AI Terminal Pro", layout="wide")
st.title("📡 Nobu AI Terminal Pro – Expert Scalping Terminal")

# Define tabs
tabs = st.tabs(["Live Signal Scanner", "Ready to Trade", "Market Overview"])

# Tab 1: Live Signal Scanner
with tabs[0]:
    st.markdown("### 📊 Live Scalping Signal Table")

    try:
        results = analyze_all_symbols()
        df = pd.DataFrame(results)
        st.dataframe(df.set_index("Symbol"))
        st.success("✅ Full table rendered.")
    except Exception as e:
        st.error(f"⚠️ Failed to load live signal table: {e}")

# Tab 2: Ready to Trade
with tabs[1]:
    try:
        ready_to_trade.render()
    except Exception as e:
        st.error(f"⚠️ Trade panel failed to load: {e}")

# Tab 3: Market Overview
with tabs[2]:
    st.markdown("📈 Market Overview coming soon...")