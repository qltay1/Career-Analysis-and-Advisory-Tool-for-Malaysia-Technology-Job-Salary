import numpy as np
import pandas as pd
import streamlit as st
import datetime
import re
import requests
from bs4 import BeautifulSoup



#df = pd.read_csv('Developer Kaki_Developer Salary Survey 2021 Results - Form responses 1.csv')
df = pd.read_csv('Developer Kaki _ Developer Salary Survey 2021 Results - Form responses 1.csv')


def header():
    st.header('Job Recommender System')
    #st.markdown('This recommendation engine targets developers across Malaysia')
    st.write('This recommendation engine targets developers across Malaysia')
    


def input_parameters():
    st.sidebar.header('Input features')
    age = st.sidebar.slider('Age' , 18,60)
    occupation = st.sidebar.multiselect('Work' , ['Engineer' , 'Accountant'])
    current_salary = st.sidebar.slider('Wage' ,2000,10000)

    features = {'Age': age , 'Occupation':occupation , 'Salary': current_salary}


    return pd.DataFrame(features)

def print_dataframe():
    st.subheader('Dataset')
    st.write(input_parameters())


#st.write(df)


print(df.isnull.sum())