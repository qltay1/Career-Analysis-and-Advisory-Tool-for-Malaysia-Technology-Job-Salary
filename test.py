from recommend import *

import streamlit as st
 

#Allow plotting in Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

#Web App Overview Layout 
st.title('Job Advisory Tool')
st.sidebar.markdown('Web App Functionalities: ')
a = st.sidebar.multiselect("1. Analysis of Overall Local Developer Community" , options = ['Education','Skill Sets'])
b = st.sidebar.checkbox("2. Prediction of Monthly Starting Salary")
c = st.sidebar.multiselect("3. Simple Job Recommendation" , df['Job Title'].value_counts().nlargest(10).index)



#User input to be fed into the model

def user_input():
    st.header('User Preferences')

    st.sidebar.header('Input features')
    age = st.sidebar.slider('Age' , 10,60)
    experience = st.sidebar.slider('Past Experience' , 10,60)
    employments = st.sidebar.slider('Previous No of Jobs' , 10,60)
    education = st.sidebar.multiselect('Highest Education Level', ['a','b'])
    home = st.sidebar.multiselect('Current State of Residence', ['a' , 'b'])
    
    features = {'Age': age , 'Past Experience':experience ,  'Past Employments': employments, 'Education': education ,  'Residence': home ,}

    st.write(pd.DataFrame(features))

#Visualization APIs to be called

#1. Age Distribution of respondents

#2 
#1. Check for Most Used Programming Language/ Technologies
def plot_wordcloud(title):
    df_new = df[df['Job Title'] == title]
    plt.figure(figsize=(10,10))
    wc = WordCloud(max_words=100, width=500, height=500).generate(" ".join(df_new['Technologies Used']))
    plt.title("Most Common Skills Used for {}".format(title), fontsize=10)
    plt.imshow(wc, interpolation='bilinear')
    st.pyplot()
    
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

""" if a == 'Skill Sets':
    user_input = st.text_area('What kind of skill sets you wish to see for as a developer?')
    user_input  = str(user_input)
    plot_wordcloud(user_input)
elif a=='Education':
    education() """


similar_job(c)