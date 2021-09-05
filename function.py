import numpy as np
import pandas as pd
import streamlit as st
import datetime
import re
import requests
import pickle
import matplotlib.pyplot as plt
from function import *
from wordcloud import WordCloud

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

