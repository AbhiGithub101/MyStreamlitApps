import pandas as pd
import requests
import streamlit as st
api_key = 'b3eda79fa97e412bbe382506231906'
base_url = ' http://api.weatherapi.com/v1'
with st.sidebar:
    st.title('Menu')
    check = st.selectbox(label='Information',options=['Select','Weather','Air Quality'])


st.title('Weather Info')
info = st.selectbox(label=' ',options=['Select','Current','Forecast'])
country_city_data = {
        'USA': ['New York', 'Los Angeles', 'Chicago'],
        'Canada': ['Toronto', 'Vancouver', 'Montreal'],
        'Australia': ['Sydney', 'Melbourne', 'Brisbane'],
        'India' : ['Allahabad','Kanpur','Assam','Uttarakhand']
    }

    # Create the cascading dropdowns
selected_country = st.selectbox('Select a country', list(country_city_data.keys()))
selected_city = st.selectbox('Select a city', country_city_data[selected_country])

click = st.button('Submit')
if(click==True):
    data = requests.get(
            f'https://api.weatherapi.com/v1/{info.lower()}.json?key={api_key}&q={selected_city}&aqi=no').json()
        # df = st.dataframe(data)
    col1,col2,col3 = st.columns(3)
    col1.metric(label="Temperature", value=f"{data[info.lower()]['temp_c']}",)
    col2.metric(label="Atmosphere", value=f"{data[info.lower()]['condition']['text']}")
    col3.metric(label="Feels Like", value=f"{data[info.lower()]['feelslike_c']}")



