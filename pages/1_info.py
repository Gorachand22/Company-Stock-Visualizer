import streamlit as st
import pandas as pd

st.set_page_config(page_title=f"{st.session_state.select} Stock", page_icon="📈", layout="wide")

st.title(f"{st.session_state.select} Stock")

if 'data1' not in st.session_state:
    st.session_state['data1'] = None

if st.session_state['data1'] is not None:
    st.markdown(f"<h1>{st.session_state.select} Stock</h1>", unsafe_allow_html=True)
    df = st.session_state['data1']
    col1, col2= st.columns(2)
    with col1:
        with st.expander("🔎 Dataframe Preview"):
                # 'Open', 'High', 'Low', 'Close', 'Volume']
                length = df.shape[0]
                slider = st.sidebar.slider("Rows", 0, length, 4, step=1)
                st.data_editor(df.head(slider),
                            column_config={
                                'Open': st.column_config.NumberColumn(),
                                'High': st.column_config.NumberColumn(),
                                'Low': st.column_config.NumberColumn(),
                                'Close': st.column_config.NumberColumn(),
                                'Volume': st.column_config.NumberColumn()
                            }, use_container_width=True
                            )
    
    with col2:
        with st.expander("📊 Dataframe Statistics"):
            st.data_editor(df.describe(), use_container_width=True)

    # min, max, start_date, end_date
    st.divider()
    container1 = st.container(border=True)
    container1.subheader("Today's Stock Price")
    col1, col2, col3, col4 = container1.columns(4)
    today_price = df['High'][::-1].head(1).values[0]
    diff = round(today_price - df['High'][::-1].head(2).values[-1], 3)
    col1.metric("Today High", today_price, f'{diff if diff > 0 else -diff}$')
    # low
    low = df['Low'][::-1].head(1).values[0]
    diff1 = round(low - df['Low'][::-1].head(2).values[-1], 3)
    col2.metric("Today Low", low, f'{diff1 if diff1 > 0 else -diff1}$')
    # close
    close = df['Close'][::-1].head(1).values[0]
    diff2 = round(close - df['Close'][::-1].head(2).values[-1], 3)
    col3.metric("Today Close", close, f'{diff2 if diff2 > 0 else -diff2}$')
    st.divider()
    
    df1 = st.session_state['data1'].copy()
    df1['Volume'] = df1['Volume'].fillna(method='ffill')
    df1['Open'] = df1['Open'].fillna(method='ffill')
    df1['High'] = df1['High'].fillna(method='ffill')
    df1['Low'] = df1['Low'].fillna(method='ffill')
    df1['Close'] = df1['Close'].fillna(method='ffill')
    df1 = df1.T.apply(lambda row: row.tolist(), axis=1)
    df1 = pd.DataFrame(df1, columns=['Trend'])
    st.data_editor(df1,
                    column_config={
                            "Trend": st.column_config.LineChartColumn(width = 'large')
                    }, use_container_width=True)
    st.divider()

else:
    st.write("No data found")
    st.warning("Please scrape the data first")

st.page_link("01_Homepage.py", label="Back to Homepage", icon="🏠")