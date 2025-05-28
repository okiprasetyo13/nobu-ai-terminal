
import streamlit as st
import pandas as pd
import ready_to_trade

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

# Simulated signal results (to be replaced with analyze_all_symbols logic)
from signal_engine import analyze_all_symbols
results = analyze_all_symbols()

df = pd.DataFrame(results)

st.markdown("### 📊 Live Scalping Signal Table")
#st.dataframe(df.set_index("Symbol"))

st.success("✅ Full table rendered. Replace placeholder with signal_engine.analyze_all_symbols().")
st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
