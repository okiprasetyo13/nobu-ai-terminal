import streamlit as st
import pandas as pd
from signal_engine import generate_signals
from plot_chart import render_chart
from websocket_client import start_price_feed
from ready_to_trade import get_trade_advice
from telegram_alerts import send_alert
import time

# Page setup
st.set_page_config(page_title="Nobu AI Terminal Pro", layout="wide")
st.title("📈 Nobu AI Terminal Pro - Expert Scalping Dashboard")

# Start WebSocket price feed
prices = start_price_feed()

# Load signals
with st.spinner("Fetching live data and calculating signals..."):
    signals_df = generate_signals(prices)
    time.sleep(2)  # Simulate processing time

# Filter best coins for scalping
scalping_df = signals_df[signals_df['Suitability'] == 'Scalping'].sort_values(by='Score', ascending=False)
top_20_df = scalping_df.head(20)

# Keep BTC and ETH pinned
btc_row = signals_df[signals_df['Symbol'] == 'BTC']
eth_row = signals_df[signals_df['Symbol'] == 'ETH']
final_df = pd.concat([btc_row, eth_row, top_20_df]).drop_duplicates().reset_index(drop=True)

# Expert trade advice
final_df['Expert Advice'] = final_df.apply(lambda row: get_trade_advice(row), axis=1)

# Display table
st.subheader("💹 Live Expert Scalping Signal Table")
st.dataframe(final_df[['Symbol', 'Price', 'Signal', 'Score', 'RSI', 'EMA9', 'EMA21',
                       'Support', 'Resistance', 'Buy Price', 'SL', 'TP', 'Volume', 'Suitability', 'Expert Advice']],
             height=600)

# Chart rendering per symbol
st.subheader("📊 Mini Chart (click below to view)")
selected_coin = st.selectbox("Choose Coin to View Chart", final_df['Symbol'].unique())
render_chart(selected_coin)

# Alert notification check (live SL/TP)
for _, row in final_df.iterrows():
    if row['Active'] and (row['Price'] <= row['SL'] or row['Price'] >= row['TP']):
        send_alert(f"{row['Symbol']} hit {'TP' if row['Price'] >= row['TP'] else 'SL'} at {row['Price']}")

st.success("✅ Dashboard updated with live scalping signals.")
