from function import predict_salary_group
from recommend import *

import streamlit as st
 

#Allow plotting in Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

#Web App Overview Layout 
st.title('Job Advisory Tool')
st.sidebar.markdown('Web App Functionalities: ')
a = st.sidebar.checkbox("1. Analysis of Overall Local Developer Community" )
b = st.sidebar.checkbox("2. Prediction of Monthly Starting Salary")
c = st.sidebar.checkbox("3. Career Change")



#User input to be fed into the model



#Visualization APIs to be called

#1. Age Distribution of respondents

#2 
#1. Check for Most Used Programming Language/ Technologies    
def split(col):
    temp_df = col.to_frame()
    options = []
    for i, val in col[col.notnull()].iteritems():
        for option in val.split(','):
            if not option in temp_df.columns:
                options.append(option)
                temp_df[option]= False
            temp_df.at[i, option] = True
    return temp_df[options]

def common_languages():
    skills_df = split(df['Technologies Used'])
    skills_sum_df = skills_df.sum().sort_values().nlargest(20)
    sns.barplot(x = skills_sum_df , y = skills_sum_df.index)


#2. Education background for technical degree
def education():
    education = df.groupby('Name of Highest Degree Obtained')['Degree in Tech']
    education.value_counts().sort_values(ascending=False).nlargest(10).plot(kind='barh')
    st.pyplot()



#Load in regression and NLP model
if b:
    predict_salary_group()

if c:
    input = st.text_area('Change career')
    recommend_job_skills(input)