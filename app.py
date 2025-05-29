import streamlit as st
import pandas as pd
import ready_to_trade
from signal_engine import analyze_all_symbols

# Load analysis result
results = analyze_all_symbols()
df = pd.DataFrame(results)

# Streamlit UI setup
st.set_page_config(page_title="Nobu AI Terminal Pro", layout="wide")
st.title("📡 Nobu AI Terminal Pro – Expert Scalping Terminal")

tabs = st.tabs(["Live Signal Scanner", "Ready to Trade", "Market Overview"])

# === Live Signal Scanner Tab ===
with tabs[0]:
    st.markdown("### 📊 Live Scalping Signal Table")
    st.dataframe(df.set_index("Symbol"), use_container_width=True)
    st.success("✅ Full table rendered.")

# === Ready to Trade Tab ===
with tabs[1]:
    ready_to_trade.app()  # runs trade input panel

# === Market Overview Placeholder ===
with tabs[2]:
    st.markdown("⚠️ Market Overview coming soon...")
