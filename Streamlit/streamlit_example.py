import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the **stock closing price** and ***volume*** of Google!
""")

tickerSymbol = "GOOGL"

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period="1d", start="2011-08-15", stop="2021-08-15")

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
