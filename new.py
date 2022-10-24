import streamlit as st
import calendar
from datetime import datetime

page_title = 'Income Expense Tracker'
page_icon = ":euro:"
layout = "centered"
st.set_page_config(page_title=page_title,page_icon=page_icon,layout="centered")
st.title('Income Expense Tracker')
year  = [datetime.today().year,datetime.today().year+1]
month = list(calendar.month_name[1:])
incomes = ['Salary','Blog','Other Income']
expenses = ['Rent','Utilities','Saving','Groceries']

st.subheader('Submission Form')
with st.form('Data Entry Form',clear_on_submit=True):
    col1,col2 = st.columns(2)
    col1 = st.selectbox(label='Year',options=year,key='year')
    col2 = st.selectbox(label='Month',options=month,key='month')

    "---"
    with st.expander(label="Income"):
        for income in incomes:
            st.number_input(label=income,format='%i',step=10,key=income)
    with st.expander(label="Expense"):
        for expense in expenses:
            st.number_input(label=expense,format='%i',step=10,key=expense)
    "---"
    submitted = st.form_submit_button()
    if submitted:
        period = str(st.session_state['year']) + "_" + st.session_state['month']
        incomes = {income : st.session_state[income] for income in incomes}
        expenses = {expense : st.session_state[expense] for expense in expenses}
    # to do - database
    st.write(incomes)
    st.write(expenses)
    st.success('Data Saved')
    