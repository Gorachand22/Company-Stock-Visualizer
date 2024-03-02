import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title=f"{st.session_state.select} Stock Visualization", page_icon="🎢", layout="wide")

st.title(f"{st.session_state.select} Stock Visualization")

if 'data1' not in st.session_state:
    st.session_state['data1'] = None

if st.session_state['data1'] is not None:
    df1 = st.session_state['data1'].copy()
    df2 = st.session_state['data1'].copy()

    df2['month'] = df2.index.month
    df2['month_name'] = df2.index.month_name()
    df2['day'] = df2.index.day
    df2['year'] = df2.index.year
    df2['quarter'] = df2.index.quarter
    df2['week'] = df2.index.weekday
    df2['week'] = df2['week'].map({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday'})

    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(2)
    row4= st.columns(2)
    row5 = st.columns(3)
    row6 = st.columns(3)

    container = st.sidebar.container(height=200)
    st.session_state.start = str(container.date_input("Starting Date", df2.index[0].date(), min_value=df2.index[0].date(), max_value=df2.index[-2].date()))
    st.session_state.end = str(container.date_input("Ending Date", df2.index[-1].date(), min_value=df2.index[1].date(), max_value=df2.index[-1].date()))

    if st.session_state.start and st.session_state.end:
        start1 = str(st.session_state.start)
        end1 = str(st.session_state.end)
        with row1[0]:
            container1 = st.container(height=600, border=True )
            container1.subheader("Yearly Trend")
            slider1 = container1.slider("Years-gap", 1, len(df1.index.year.unique()), 1, step=1)
            M = df1[df1.index.isin(pd.date_range(start=start1,end=end1,freq=pd.DateOffset(years=slider1)))]
            color = container1.color_picker('Pick A Color', "#F98C00", key = 'color1')
            container1.line_chart(M, y = 'Close', use_container_width=True, color=color)

        with row1[1]:
            container2 = st.container(height=600, border=True)
            container2.subheader("Monthly Trend")
            slider2 = container2.slider("Months-gap", 1, 12, 1, step=1)
            M = df1[df1.index.isin(pd.date_range(start=start1,end=end1,freq=pd.DateOffset(months=slider2)))]
            color = container2.color_picker('Pick A Color', "#00F900", key = 'color2')
            container2.line_chart(M, y = 'Close', use_container_width=True, color=color)

        with row1[2]:
            container3 = st.container(height=600, border=True)
            container3.subheader("Date Trend")
            slider3 = container3.slider("Months-gap", 1, 365, 1, step=1)
            M = df1[df1.index.isin(pd.date_range(start=start1,end=end1,freq=pd.DateOffset(months=slider3)))]
            color = container3.color_picker('Pick A Color', "#F91A00", key = 'color3')
            container3.line_chart(M , y = 'Close', use_container_width=True, color=color)

        st.divider()

        with row2[0]:
            container4 = st.container(height=450, border=True)
            container4.subheader("Date VS Open")
            M = df1.loc[start1: end1]
            container4.line_chart(M,y= ['Open'], use_container_width=True, color=["#F98C00"])

        with row2[1]:
            container5 = st.container(height=450, border=True)
            container5.subheader("Date Vs High")
            M = df1.loc[start1: end1]
            container5.line_chart(M,y= ['High'], use_container_width=True, color=["#00F900"])
        with row2[2]:
            container6 = st.container(height=450, border=True)
            container6.subheader("Date VS Low")
            M = df1.loc[start1: end1]
            container6.line_chart(M,y= ['Low'], use_container_width=True, color=[ "#F91A00"])
        
        with row3[0]:
            container7 = st.container(height=450, border=True)
            container7.subheader("Date VS Close")
            M = df1.loc[start1: end1]
            container7.line_chart(M,y= ['Close'], use_container_width=True, color=["#00F9E3"])

    
        with row3[1]:
            container8 = st.container(height=450, border=True)
            container8.subheader("Date VS Volume")
            M = df1.loc[start1: end1]
            container8.line_chart(M,y= ['Volume'], use_container_width=True, color=["#003DF9"])
        
        with row4[0]:
            container9 = st.container(height=450, border=True)
            container9.subheader("Specific Year Trend")
            st.session_state.year = container9.selectbox("Year", df2['year'].unique())
            if st.session_state.year:
                day = st.session_state.year
                D = df2[df2['year'] == day]
                container9.line_chart(D, y = 'Close', use_container_width=True)
        
        with row4[1]:
            container10 = st.container(height=450, border=True)
            container10.subheader("Specific Month Trend")
            st.session_state.month = container10.selectbox("Month", df2['month'].unique())
            if st.session_state.month:
                month = st.session_state.month
                D = df2[df2['month'] == month]
                container10.line_chart(D, y = 'Close', use_container_width=True)
        
        # bar plot month wise
        with row5[0]:
            container11 = st.container(height=500, border=True)
            container11.subheader("Month Wise Trend")
            Z1 = df2.groupby('month_name')['Close'].mean().reset_index()
            container11.bar_chart(Z1, x = 'month_name', y='Close', color='month_name', width=400, height=400, use_container_width=True)
        
        # bar plot year wise
        with row5[1]:
            container12 = st.container(height=500, border=True)
            container12.subheader("Year Wise Trend")
            Z2 = df2.groupby('year')['Close'].mean().reset_index()
            container12.bar_chart(Z2, x = 'year', y='Close', color='year', width=400, height=400, use_container_width=True)

        # bar plot week wise
        with row5[2]:
            container13 = st.container(height=500, border=True)
            container13.subheader("Week Wise Trend")
            Z3 = df2.groupby('week')['Close'].mean().reset_index()
            container13.bar_chart(Z3, x = 'week', y='Close', color='week', width=400, height=400, use_container_width=True)

        # downsampling (smoothing)
        with row6[0]:
            container14 = st.container(height=500, border=True)
            container14.subheader("Downsampling (Trend Smoothing)")
            st.session_state.option1 = container.radio("Select", ['Yearly', 'Monthly', "Day"])
            if st.session_state.option1 == 'Yearly':
                num1 = container14.slider("Year", 1, len(df1.index.year.unique()), 1, step=1)
                df3 = df1['Close'].resample(f'{num1}Y').mean().reset_index().set_index('Date')
                container14.line_chart(df3, y = 'Close', use_container_width=True)
            
            if st.session_state.option1 == 'Monthly':
                num2 = container14.slider("Month", 1, 12, 1, step=1)
                df4 = df1['Close'].resample(f'{num2}M').mean().reset_index().set_index('Date')
                container14.line_chart(df4, y = 'Close', use_container_width=True)
            
            if st.session_state.option1 == 'Day':
                num3 = container14.slider("Day", 1, 365, 1, step=1)
                df5 = df1['Close'].resample(f'{num3}D').mean().reset_index().set_index('Date')
                container14.line_chart(df5, y = 'Close', use_container_width=True)

        # rolling mean
        with row6[1]:
            container15 = st.container(height=500, border=True)
            container15.subheader("Rolling Mean")
            num4 = container15.slider("Day ", 1, 365, 1, step=1)
            df6 = df1['Close'].rolling(num4).mean().reset_index().set_index('Date')
            container15.line_chart(df6, y = 'Close', use_container_width=True)

        # ewm
        with row6[2]:
            container16 = st.container(height=500, border=True)
            container16.subheader("Exponentially Weighted Mean")
            num5 = container16.slider("Day  ", 1, 365, 1, step=1)
            df7 = df1['Close'].ewm(span=num5).mean().reset_index().set_index('Date')
            container16.line_chart(df7, y = 'Close', use_container_width=True)

else:
    st.write("No data found")
    st.warning("Please scrape the data first")

st.page_link("01_Homepage.py", label="Back to Homepage", icon="🏠")