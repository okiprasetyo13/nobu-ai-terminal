def generate_trade_advice(row):
    """
    Generate expert-level advice for each coin based on signal strength, price action, and indicators.
    """

    try:
        signal = row['Signal']
        score = row['Score']
        rsi = row['RSI']
        ema9 = row['EMA9']
        ema21 = row['EMA21']
        price = row['Price']
        support = row['Support']
        resistance = row['Resistance']
        tp = row['TP']
        sl = row['SL']

        # Trade direction suggestion
        if score >= 8 and price <= support * 1.01:
            strategy = "Scalping Buy"
            entry = f"Enter around {price}"
            take_profit = f"TP around {tp}"
            stop_loss = f"SL around {sl}"
        elif score >= 8 and price >= resistance * 0.99:
            strategy = "Short Trading"
            entry = f"Enter short around {price}"
            take_profit = f"TP near {support}"
            stop_loss = f"SL above {resistance}"
        elif ema9 > ema21 and rsi < 70:
            strategy = "Long Trading"
            entry = f"Buy around {price}"
            take_profit = f"TP near {tp}"
            stop_loss = f"SL near {sl}"
        else:
            strategy = "Wait"
            entry = "No clear entry"
            take_profit = "-"
            stop_loss = "-"

        return f"{strategy} | {entry} | {take_profit} | {stop_loss}"

    except Exception as e:
        return f"Error generating advice: {str(e)}"
