"""This is the Homepage file"""
import streamlit as st
import pandas_datareader.data as web
import pandas as pd

st.title("Welcome to Company Stock Visualizzer")
if 'data1' not in st.session_state:
    st.session_state['data1'] = None

container = st.container(height=300)
start = str(container.date_input("Starting Date", pd.Timestamp('2000-01-01').date()))
end = str(container.date_input("Ending Date", pd.Timestamp.today().date()))

stock_symbol = ["AAPL","GOOGL", "GOOG", "TSLA", "AMZN", "MSFT", "META", "NFLX", "BABA", "NVDA", "AMD", "TSM", "MRNA", "TCEHY"]
company_name = ['Apple', 'Google (class A)', 'Google (class C)', 'Tesla', 'Amazon', 'Microsoft', 'Meta', 'Netflix', 'Alibaba', 'Nvidia','AMD', 'TSMC', 'Moderna', 'Tencent']

st.session_state.select = container.selectbox("Select Company", company_name)
option = st.session_state.select
if option:
    Index = company_name.index(option)
    select_option  = stock_symbol[Index]

if start and end and st.button("Scrape"):

    st.session_state['data1'] = web.DataReader(f'{select_option}', 'stooq', start, end).iloc[::-1]
    st.divider()
    st.divider()
    st.info("Click on the tabs below to view the data")
    tab1, tab2= st.tabs(["Info", "Visual"])
    with tab1:
        st.page_link("pages/1_info.py", label="Info", icon="1️⃣")
    with tab2:
        st.page_link("pages/2_Visual.py", label="Visual", icon="2️⃣")

if st.session_state['data1'] is not None:
    st.download_button(label="Download", data=st.session_state['data1'].to_csv(), file_name=f'{select_option}.csv', mime='text/csv')
    