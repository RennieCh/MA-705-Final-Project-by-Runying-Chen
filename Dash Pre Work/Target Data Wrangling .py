#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:26:15 2022

@author: rennie
"""
import re
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.pyplot import figure
import glob
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import datetime
from bs4 import BeautifulSoup
from PIL import Image
from collections import Counter
import seaborn as sns

###data wrangling
df = pd.read_csv('/Users/rennie/Desktop/Bentley/2022 Fall/MA-705 HB1/Individual Project/Target_Bestsellers_All_Categories.csv')

df = df.drop(columns=['Unnamed: 0'])
df = df.dropna()

top_10_numberOfRating= df.sort_values(by=['ratings_total'],ascending=False).head(9)

count_rating = Counter(df.rating).most_common()

### Clean up title and creating a new columns

df["product_name"]= df['title'].str.replace("- \w+ \w+ &#\d+; ",'')
df["product_name"]=df["product_name"].str.replace("- \w+ &#\d+; ",'')
df["product_name"]=df["product_name"].str.replace("- \w+ &#\d+; ",'')
df["product_name"]=df["product_name"].str.replace(" \w+ &#\d+;",'')
df["product_name"]=df["product_name"].str.replace("\w+&#\d+;s",'')
df["product_name"]=df["product_name"].str.replace("\w+&#\d+;",'')
df["product_name"]=df["product_name"].str.replace("Good &", '')
df["product_name"]=df["product_name"].str.replace("&#\d+", '')
df["product_name"]=df["product_name"].str.replace("  ", ' ')
df["product_name"]=df["product_name"].str.strip()
df["product_name"]= df["product_name"].str.replace("- Mondo$", '')
df["product_name"]= df["product_name"].str.replace("- Room$", '')



### create a new data with selected columns

target = df[['product_name', 'category', 'rating', 'ratings_total', 'price', 'link']]


### export the cleaned dataset

#target.to_csv('/Users/rennie/Desktop/Bentley/2022 Fall/MA-705 HB1/Individual Project/Target_Cleaned.csv')











