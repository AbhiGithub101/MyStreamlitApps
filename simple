import streamlit as st

st.title('Simple Interest Calculator')

principle = st.number_input('Principle',step=1)
rate = st.number_input('Rate',step=1)
time = st.number_input('Time',step=1)

check = st.checkbox('I agree for Terms and Conditions ')
if(check):
    click = st.button('Calculate SI')
    if(click):
        st.title(f'Simple Interest : {principle * rate * time / 100}')
