import streamlit as st
import calendar
from datetime import datetime
import plotly.graph_objects as go
from streamlit_option_menu import option_menu



page_title = 'Income Expense Tracker'
page_icon = ":euro:"
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")
st.title('Income Expense Tracker')
year = [datetime.today().year, datetime.today().year + 1]
month = list(calendar.month_name[1:])
incomes = ['Salary', 'Blog', 'Other Income']
expenses = ['Rent', 'Utilities', 'Saving', 'Groceries']

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.subheader('Submission Form')
selected = option_menu(
    menu_title='',
    options=['Data Submission','Graphs'],
    icons=['pencil-fill','bar-chart-fill'],
    orientation='horizontal'
)
if selected=='Data Submission':
    with st.form('Data Entry Form', clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1 = st.selectbox(label='Year', options=year, key='year')
        col2 = st.selectbox(label='Month', options=month, key='month')

        "---"
        with st.expander(label="Income"):
            for income in incomes:
                st.number_input(label=income, format='%i', step=10, key=income)
        with st.expander(label="Expense"):
            for expense in expenses:
                st.number_input(label=expense, format='%i', step=10, key=expense)
        with st.expander('Comment'):
            st.text_area(label='Comment',placeholder='Remarks',key='comment')
        "---"
        submitted = st.form_submit_button('Submit')
        if submitted:
            period = str(st.session_state['year']) + "_" + st.session_state['month']
            incomes = {income: st.session_state[income] for income in incomes}
            expenses = {expense: st.session_state[expense] for expense in expenses}
            # to do - database
            st.write(incomes)
            st.write(expenses)
            st.success('Data Saved')
elif selected=='Graphs':
    st.subheader('Visualization')
    with st.form('Saved Periods'):
        # to do get periods from database
        period = st.selectbox('Period', ['2022_March'])
        submitted = st.form_submit_button('Submit')
        if submitted:
            # get data from database
            comment = 'Some comment'
            incomes = {'Salary' : 200,'Blog' : 300,'Other Income' : 300}
            expenses = {'Rent':100, 'Utilities':200, 'Saving':100, 'Groceries':150}
            # create metrics
            total_income = sum(incomes.values())
            total_expense = sum(expenses.values())
            remaining_budget = total_income - total_expense
            col1,col2,col3 =st.columns([1,1,1])
            with col1:
                col1 = st.metric('Total Income',value=total_income)
            with col2:
                col2 = st.metric('Total Expense',value=total_expense)
            with col3:
                col3 = st.metric('Remaining Budget',value=remaining_budget)
            st.text(comment)
            label = list(incomes.keys()) + ['Total Income'] + list(expenses.keys())
            source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
            value = list(incomes.values()) + [total_income] + list(expenses.values())
            target =[len(incomes) ] * len (incomes) + [label.index(expense) for expense in expenses.keys()]
            # Data to dict, dict to sankey
            link = dict(source=source, target=target, value=value)
            node = dict(label=label, pad=20, thickness=30, color="#E694FF")
            data = go.Sankey(link = link, node = node)
            fig = go.Figure(data)
            fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
            st.plotly_chart(fig,use_container_width=True)

