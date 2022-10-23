import streamlit as st
import pandas as pd

df = pd.read_csv('Sales.csv')
st.title('Console Flare - Sales Analysis : ')
st.text('''In this project, we are going to analyze 12 months of data of sales. 
We will learn how to clean, manage and analyze the dataset to 
find some meaningful information.''')
with st.sidebar:
    click4 = st.multiselect('Show The Data', options=list(df.columns))
    categorical = st.selectbox('Categorical', options=['Select']+list(df.columns))
    numerical = st.selectbox('Numerical', options=['Select']+list(df.columns))
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        click_sum = st.button('Sum')
    with col2:
        click_count = st.button('Count')
    with col3:
        pass
    click3 = st.slider('Top Products Sold Together',0,5)


try:
    if (click_sum):
        st.dataframe(df.groupby(categorical)[numerical].sum())
        st.bar_chart(df.groupby(categorical)[numerical].sum())
    elif(click_count):
        st.dataframe(df.groupby(categorical)[numerical].count())
        st.bar_chart(df.groupby(categorical)[numerical].count())
    elif(click3>0):
        all_data = df.dropna(how='all')
        df = all_data[all_data['Order ID'].duplicated(keep=False)]

        from itertools import combinations
        from collections import Counter

        count = Counter()
        row_list = []
        df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x : ','.join(x))
        df = df[['Order ID','Grouped']]
        for row in df['Grouped']:
            row_list = row.split(',')
            count.update(Counter(combinations(row_list, click3))) #update method will update results
                                                             #2 is the combination of two products

        a = st.dataframe(count.most_common(10))    #most_common will give top values
    if(click4):
        st.dataframe(df[click4])
except Exception as e:
    st.title('This Operation is Not Possible.')
