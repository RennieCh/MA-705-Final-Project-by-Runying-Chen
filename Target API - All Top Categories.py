#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:45:59 2022

@author: rennie
"""

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

#Get all top-level standard categories from Target

"""

url = "https://api.redcircleapi.com/categories?api_key=91ADAC34B9064D58B7688C4D87606610"

params = {'apiKey' : '91ADAC34B9064D58B7688C4D87606610'} #noted this is my personal API 
response1 = requests.get(url, params=params)
response1.raise_for_status()
categories = response1.json()['categories']

categories = pd.DataFrame.from_dict(categories)

C_ids = categories['id']

print(categories)

"""
params = {'apiKey' : '91ADAC34B9064D58B7688C4D87606610'} #noted this is my personal API 

#get the frist five pages best seller in-stock products whith 4-5 Rating
 

#Category - grocery 
url_c1 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xt1a&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c1 = requests.get(url_c1, params=params)
response_c1.raise_for_status()
Grocery = response_c1.json()['category_results']

Grocery= pd.DataFrame.from_dict(Grocery)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller1 = pd.DataFrame(columns=df_variables)
best_seller1['title'] = [x['title'] for x in Grocery['product']]
best_seller1['rating'] = [ x.get('rating') for x in Grocery['product']]
best_seller1['ratings_total'] = [x.get('ratings_total') for x in Grocery['product']]
best_seller1['price'] = [x['primary']['price'] for x in Grocery['offers']]
best_seller1['link'] = [x['link'] for x in Grocery['product']]
best_seller1['category'] = 'Grocery'



#Category - Household Essentials
url_c2 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xsz1&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c2 = requests.get(url_c2, params=params)
response_c2.raise_for_status()
Household = response_c2.json()['category_results']

Household= pd.DataFrame.from_dict(Household)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller2 = pd.DataFrame(columns=df_variables)
best_seller2['title'] = [x['title'] for x in Household['product']]
best_seller2['rating'] = [ x.get('rating') for x in Household['product']]
best_seller2['ratings_total'] = [x.get('ratings_total') for x in Household['product']]
best_seller2['price'] = [x['primary'].get('price') for x in Household['offers']]
best_seller2['link'] = [x['link'] for x in Household['product']]
best_seller2['category'] = 'Household Essentials'


#Category - Women
url_c3 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xtd3&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c3 = requests.get(url_c3, params=params)
response_c3.raise_for_status()
Women = response_c3.json()['category_results']

Women= pd.DataFrame.from_dict(Women)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller3 = pd.DataFrame(columns=df_variables)
best_seller3['title'] = [x['title'] for x in Women['product']]
best_seller3['rating'] = [ x.get('rating') for x in Women['product']]
best_seller3['ratings_total'] = [x.get('ratings_total') for x in Women['product']]
best_seller3['price'] = [x['primary'].get('price') for x in Women['offers']]
best_seller3['link'] = [x['link'] for x in Women['product']]
best_seller3['category'] = 'Women'



#Category - Men
url_c4 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=18y1l&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c4 = requests.get(url_c4, params=params)
response_c4.raise_for_status()
Men = response_c4.json()['category_results']

Men= pd.DataFrame.from_dict(Men)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller4 = pd.DataFrame(columns=df_variables)
best_seller4['title'] = [x['title'] for x in Men['product']]
best_seller4['rating'] = [ x.get('rating') for x in Men['product']]
best_seller4['ratings_total'] = [x.get('ratings_total') for x in Men['product']]
best_seller4['price'] = [x['primary'].get('price') for x in Men['offers']]
best_seller4['link'] = [x['link'] for x in Men['product']]
best_seller4['category'] = 'Men'


#Category - Toys
url_c5 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xtb0&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c5 = requests.get(url_c5, params=params)
response_c5.raise_for_status()
Toys = response_c5.json()['category_results']

Toys= pd.DataFrame.from_dict(Toys)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller5 = pd.DataFrame(columns=df_variables)
best_seller5['title'] = [x['title'] for x in Toys['product']]
best_seller5['rating'] = [ x.get('rating') for x in Toys['product']]
best_seller5['ratings_total'] = [x.get('ratings_total') for x in Toys['product']]
best_seller5['price'] = [x['primary'].get('price') for x in Toys['offers']]
best_seller5['link'] = [x['link'] for x in Toys['product']]
best_seller5['category'] = 'Toys'



#Category - Video Games
url_c6 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xtg5&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c6 = requests.get(url_c6, params=params)
response_c6.raise_for_status()
Video_Games= response_c6.json()['category_results']

Video_Games= pd.DataFrame.from_dict(Video_Games)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller6 = pd.DataFrame(columns=df_variables)
best_seller6['title'] = [x['title'] for x in Video_Games['product']]
best_seller6['rating'] = [ x.get('rating') for x in Video_Games['product']]
best_seller6['ratings_total'] = [x.get('ratings_total') for x in Video_Games['product']]
best_seller6['price'] = [x['primary'].get('price') for x in Video_Games['offers']]
best_seller6['link'] = [x['link'] for x in Video_Games['product']]
best_seller6['category'] = 'Video Games'


#Category - Movies, Music & Books
url_c7 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xsxe&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c7 = requests.get(url_c7, params=params)
response_c7.raise_for_status()
MMB= response_c7.json()['category_results']

MMB= pd.DataFrame.from_dict(MMB)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller7 = pd.DataFrame(columns=df_variables)
best_seller7['title'] = [x['title'] for x in MMB['product']]
best_seller7['rating'] = [ x.get('rating') for x in MMB['product']]
best_seller7['ratings_total'] = [x.get('ratings_total') for x in MMB['product']]
best_seller7['price'] = [x['primary'].get('price') for x in MMB['offers']]
best_seller7['link'] = [x['link'] for x in MMB['product']]
best_seller7['category'] = 'Movies, Music & Books'


#Category - Sports & Outdoors
url_c8 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xt85&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c8 = requests.get(url_c8, params=params)
response_c8.raise_for_status()
Sports= response_c8.json()['category_results']

Sports= pd.DataFrame.from_dict(Sports)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller8 = pd.DataFrame(columns=df_variables)
best_seller8['title'] = [x['title'] for x in Sports['product']]
best_seller8['rating'] = [ x.get('rating') for x in Sports['product']]
best_seller8['ratings_total'] = [x.get('ratings_total') for x in Sports['product']]
best_seller8['price'] = [x['primary'].get('price') for x in Sports['offers']]
best_seller8['link'] = [x['link'] for x in Sports['product']]
best_seller8['category'] = 'Sports & Outdoors'


#Category - Beauty
url_c9 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=55r1x&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c9 = requests.get(url_c9, params=params)
response_c9.raise_for_status()
Beauty= response_c9.json()['category_results']

Beauty= pd.DataFrame.from_dict(Beauty)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller9 = pd.DataFrame(columns=df_variables)
best_seller9['title'] = [x['title'] for x in Beauty['product']]
best_seller9['rating'] = [ x.get('rating') for x in Beauty['product']]
best_seller9['ratings_total'] = [x.get('ratings_total') for x in Beauty['product']]
best_seller9['price'] = [x['primary'].get('price') for x in Beauty['offers']]
best_seller9['link'] = [x['link'] for x in Beauty['product']]
best_seller9['category'] = 'Beauty'


#Category - Furniture
url_c10 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xtnr&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c10 = requests.get(url_c10, params=params)
response_c10.raise_for_status()
Furniture= response_c10.json()['category_results']

Furniture= pd.DataFrame.from_dict(Furniture)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller10 = pd.DataFrame(columns=df_variables)
best_seller10['title'] = [x['title'] for x in Furniture['product']]
best_seller10['rating'] = [ x.get('rating') for x in Furniture['product']]
best_seller10['ratings_total'] = [x.get('ratings_total') for x in Furniture['product']]
best_seller10['price'] = [x['primary'].get('price') for x in Furniture['offers']]
best_seller10['link'] = [x['link'] for x in Furniture['product']]
best_seller10['category'] = 'Furniture'



#Category - Kitchen & Dining
url_c11 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=hz89j&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c11 = requests.get(url_c11, params=params)
response_c11.raise_for_status()
KD= response_c11.json()['category_results']

KD= pd.DataFrame.from_dict(KD)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller11 = pd.DataFrame(columns=df_variables)
best_seller11['title'] = [x['title'] for x in KD['product']]
best_seller11['rating'] = [ x.get('rating') for x in KD['product']]
best_seller11['ratings_total'] = [x.get('ratings_total') for x in KD['product']]
best_seller11['price'] = [x['primary'].get('price') for x in KD['offers']]
best_seller11['link'] = [x['link'] for x in KD['product']]
best_seller11['category'] = 'Kitchen & Dining'



#Category - Electronics
url_c12 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xtg6&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c12 = requests.get(url_c12, params=params)
response_c12.raise_for_status()
Electronics= response_c12.json()['category_results']

Electronics= pd.DataFrame.from_dict(Electronics)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller12 = pd.DataFrame(columns=df_variables)
best_seller12['title'] = [x['title'] for x in Electronics['product']]
best_seller12['rating'] = [ x.get('rating') for x in Electronics['product']]
best_seller12['ratings_total'] = [x.get('ratings_total') for x in Electronics['product']]
best_seller12['price'] = [x['primary'].get('price') for x in Electronics['offers']]
best_seller12['link'] = [x['link'] for x in Electronics['product']]
best_seller12['category'] = 'Electronics'



#Category - Kids
url_c13 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=xcoz4&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c13 = requests.get(url_c13, params=params)
response_c13.raise_for_status()
Kids= response_c13.json()['category_results']

Kids= pd.DataFrame.from_dict(Kids)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller13 = pd.DataFrame(columns=df_variables)
best_seller13['title'] = [x['title'] for x in Kids['product']]
best_seller13['rating'] = [ x.get('rating') for x in Kids['product']]
best_seller13['ratings_total'] = [x.get('ratings_total') for x in Kids['product']]
best_seller13['price'] = [x['primary'].get('price') for x in Kids['offers']]
best_seller13['link'] = [x['link'] for x in Kids['product']]
best_seller13['category'] = 'Kids'



#Category - Pets
url_c14 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xt44&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c14 = requests.get(url_c14, params=params)
response_c14.raise_for_status()
Pets= response_c14.json()['category_results']

Pets= pd.DataFrame.from_dict(Pets)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller14 = pd.DataFrame(columns=df_variables)
best_seller14['title'] = [x['title'] for x in Pets['product']]
best_seller14['rating'] = [ x.get('rating') for x in Pets['product']]
best_seller14['ratings_total'] = [x.get('ratings_total') for x in Pets['product']]
best_seller14['price'] = [x['primary'].get('price') for x in Pets['offers']]
best_seller14['link'] = [x['link'] for x in Pets['product']]
best_seller14['category'] = 'Pets'



#Category - Personal Care
url_c15 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xtzq&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c15 = requests.get(url_c15, params=params)
response_c15.raise_for_status()
Personal= response_c15.json()['category_results']

Personal= pd.DataFrame.from_dict(Personal)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller15 = pd.DataFrame(columns=df_variables)
best_seller15['title'] = [x['title'] for x in Personal['product']]
best_seller15['rating'] = [ x.get('rating') for x in Personal['product']]
best_seller15['ratings_total'] = [x.get('ratings_total') for x in Personal['product']]
best_seller15['price'] = [x['primary'].get('price') for x in Personal['offers']]
best_seller15['link'] = [x['link'] for x in Personal['product']]
best_seller15['category'] = 'Personal Care'


#Category - Health
url_c16 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xu1n&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c16 = requests.get(url_c16, params=params)
response_c16.raise_for_status()
Health= response_c16.json()['category_results']

Health= pd.DataFrame.from_dict(Health)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller16 = pd.DataFrame(columns=df_variables)
best_seller16['title'] = [x['title'] for x in Health['product']]
best_seller16['rating'] = [ x.get('rating') for x in Health['product']]
best_seller16['ratings_total'] = [x.get('ratings_total') for x in Health['product']]
best_seller16['price'] = [x['primary'].get('price') for x in Health['offers']]
best_seller16['link'] = [x['link'] for x in Health['product']]
best_seller16['category'] = 'Health'


#Category - School & Office Supplies
url_c17 = "https://api.redcircleapi.com/request?api_key=91ADAC34B9064D58B7688C4D87606610&type=category&category_id=5xsxr&rating=four_star&include_out_of_stock=false&sort_by=best_seller&page=1&max_page=5"

response_c17 = requests.get(url_c17, params=params)
response_c17.raise_for_status()
SOS= response_c17.json()['category_results']

SOS= pd.DataFrame.from_dict(SOS)


df_variables = ['title', 'rating', 'ratings_total', 'price','link']
best_seller17 = pd.DataFrame(columns=df_variables)
best_seller17['title'] = [x['title'] for x in SOS['product']]
best_seller17['rating'] = [ x.get('rating') for x in SOS['product']]
best_seller17['ratings_total'] = [x.get('ratings_total') for x in SOS['product']]
best_seller17['price'] = [x['primary'].get('price') for x in SOS['offers']]
best_seller17['link'] = [x['link'] for x in SOS['product']]
best_seller17['category'] = 'School & Office Supplies'

#concact all categories
df_all=pd.concat([best_seller1,best_seller2,best_seller3,best_seller4,
                  best_seller5,best_seller6,best_seller7,best_seller8,
                  best_seller9,best_seller10,best_seller11,best_seller12,
                  best_seller13,best_seller14,best_seller15,best_seller16,
                  best_seller17], axis=0)

#export the dataframe
#df_all.to_csv('/Users/rennie/Desktop/Bentley/2022 Fall/MA-705 HB1/Individual Project/Target_Bestsellers_All_Categories.csv')