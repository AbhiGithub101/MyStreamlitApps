import streamlit as st



st.title('BMI Calculator')
st.subheader('This application is designed to calculate BMI')
name = st.text_input('Name',placeholder='Enter Your Name')
gender = st.radio('Gender',('Male','Female'))
if(gender=='Male'):
    initial = 'Mr'
else:
    initial = 'Mrs'
if(name!=''):
    st.text(f'Hello {initial} {name}, Please enter appropriate fields.')


weight = st.slider('Range of Weight',min_value=20,max_value=200)
height = st.slider('Range of Height',min_value=100,max_value=300)
click = st.button('Calculate BMI')
if(click==True):
    bmi = weight/height**2*10000
    st.subheader(f'BMI : {round(bmi)}')

    if(bmi>=30):
        st.title('Obese')
    elif(bmi>=25):
        st.title('Over Weight')
    elif(bmi>=18):
        st.title('Normal Weight')
        st.balloons()
    else:
        st.title('Underweight')
