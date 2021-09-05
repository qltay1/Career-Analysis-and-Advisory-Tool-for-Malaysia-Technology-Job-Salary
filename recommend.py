import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import re
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

#Read in the dataset
df = pd.read_csv('Developer Kaki _ Developer Salary Survey 2021 Results - Form responses 1.csv')
df.rename(columns={
    'What was your starting monthly salary?':'Starting Monthly Salary',
    'Number of past employments/jobs (excluding the current one)':'Past Employments',
    
    'What is the size of your company?':'Company Size',
    'What technologies do you use for work on a regular basis?':'Technologies Used',
    'Is your degree tech related?':'Degree in Tech',
    'How many days of annual leave are you entitled to?':'Annual Leave Entitled',
    'What is your current equity (stock) compensation per year?':'Stock Compensation (Year)',
    'What is your current bonus compensation per year?':'Bonus Compensation (Year)',
    'What is your currency code?': 'Currency',
    'What is your current monthly base salary?':'Monthly Base Salary',
    'Did you go through a bootcamp to learn technical skills?':'Attended Bootcamp'
    }, inplace =True)

recommend_df = df.copy()
tags = recommend_df.groupby('Job Title')['Technologies Used'].apply(set).apply(list)
recommend_df['tags'] = recommend_df['Job Title'].apply(lambda x: ' '.join(tags[x]))




tfidf = TfidfVectorizer(stop_words = 'english')
matrix = tfidf.fit_transform(recommend_df['tags'])
similarities = cosine_similarity(matrix, matrix)

def get_title_id(title):
    index = recommend_df[recommend_df['Job Title'] == title].index.to_list()
    #print(index)
    if len(index) == 0 | len(index) < 3:
        return index[0]
    else:
        return index[1]
    
def get_title(title_id):
    title = recommend_df.iloc[title_id]['Job Title']
    return title


def similar_job(title):
    title_id = get_title_id(title)
    
    if (title_id is not None):
        temp = list(enumerate(similarities[title_id]))
        job_similarities = sorted(temp, key = lambda x: x[1], reverse=True)
        
        similar_job = job_similarities[1:6]
        
            
        similar_job = list(map(lambda x: (get_title(x[0]), round(x[1], 2)), job_similarities))
        similar_job_df = pd.DataFrame(similar_job, columns = ['Job Title' , 'Similarity']).head(10)
        
        st.write(similar_job_df.drop_duplicates().style.hide_index())
        sns.barplot(x = similar_job_df['Job Title'] , y = similar_job_df['Similarity'] * 100)
        plt.xticks(rotation=90)
        st.pyplot()