import streamlit as st
import pandas as pd

page_title = 'Sales - Analysis'
layout = 'centered'
page_icon = ':euro:'
st.set_page_config(page_title=page_title,layout=layout,page_icon=page_icon)

st.title('Sales Analysis - Console Flare')
st.info('''Project:
In this project, we are going to analyze 12 months of data of sales. 
We will learn how to clean, manage and analyze the 
dataset to find some meaningful information.''')
df = pd.read_csv('Sales.csv')
with st.sidebar:
    show_data = st.multiselect('Show Data',options=list(df.columns))
    categorical = st.selectbox('Categorical',options=list(df.columns))
    numerical = st.selectbox('Numerical',options=list(df.columns))
    col1,col2 = st.columns([1,1])
    with col1:
        click1 = st.button('Sum')
    with col2:
        click2=st.button('Count')
    range = st.slider('Products Sold Together',0,5)

if(show_data):
    st.dataframe(df[show_data])

if(click1):
    st.dataframe(df.groupby(categorical)[numerical].sum())
    st.bar_chart(df.groupby(categorical)[numerical].sum().sort_values(ascending=False))
elif(click2):
    st.dataframe(df.groupby(categorical)[numerical].count())
    st.bar_chart(df.groupby(categorical)[numerical].count().sort_values(ascending=False))

# All Duplicate Order ID
if(range):
    df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x : ','.join(x))

    from itertools import combinations
    from collections import Counter

    count = Counter()
    row_list = []
    for row in df['Grouped']:
        row_list = row.split(',')
        count.update(Counter(combinations(row_list, range)))

    st.dataframe(count.most_common(10))
