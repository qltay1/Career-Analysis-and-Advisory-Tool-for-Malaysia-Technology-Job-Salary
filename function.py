import numpy as np
import pandas as pd
import streamlit as st

#Input features to the model

def predict_salary_group():

    st.header('User Preferences')

    age = st.slider('Age' , 10,60)
    experience = st.slider('Past Experience' , 10,60)
    employments = st.slider('Previous No of Jobs' , 10,60)
    education = st.multiselect('Highest Education Level', ['a','b'])

    features = {'Age': age , 'Past Experience':experience ,  'Past Employments': employments, 'Education': education}
    df = pd.DataFrame(features)
    

    button = st.button('Predict Starting Monthly Salary Group')
    if button:
        st.write(df)

    #prediction = salary_model.predict([[age , exp, employ, edu]])

    