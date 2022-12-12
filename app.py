#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:34:25 2022

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
import statsmodels.api as sm
import datetime
from PIL import Image
from collections import Counter
import dash
from dash import dcc, dash_table
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server

df = pd.read_csv('/Users/rennie/Desktop/Bentley/2022 Fall/MA-705 HB1/Individual Project/Target_Cleaned.csv')

df = df.drop(columns=['Unnamed: 0'])

#create a column for distigishing different levels of ratings total

def condition(x):
    if x >= 800:
        return "High Ratings Total"
    if x< 800 and x >= 300:
        return "Mid Ratings Total"
    else:
        return "Low Ratings Total"

df['ratings_total_levels'] = df['ratings_total'].apply(condition)

#modify Link column into a markdown presentation

df.link='[Link]('+df.link+')'


#create a histogram
fig = px.histogram(df, x="rating", color = "category", title="Number of Target Bestsellers by Category")

#set the page size for table
Page_size = 20

#app Layout

app.layout = html.Div([
    html.H1("Target Bestsellers Dashboard", style ={'textAlign':'center','color':'indigo'}),
    dcc.Markdown('''**MA705 Individual Project** |  **Runying Chen**
                 ''',style ={'textAlign':'center','font-size': 20 }),
    dcc.Markdown(''' ##### **Abount:**''',style ={'textAlign':'left','color':'indigo' } ),            
    dcc.Markdown('''
                 - This dashboard summarizes the most recent four to five stars rating Bestsellers in 17 categories available at [Target](https://www.target.com/).
                 - **Objective:** Create a more convenient online shopping experience for shoppers only interested in the bestsellers at Target.
                 - There is a total of 1575 products separated by different categories.
                 - Data in this dashboard was collected on December 7, 2022, using [RedCircle API](https://app.redcircleapi.com/playground).
                 - The graph shows the number of bestsellers by rating score and categories, and the graph can be filtered by: Category, Ratings Total Levels, and Price.
                 - Rating total per product is distinguished into three levels
                     * Low Rating Total for products that have less than 300 ratings.
                     * Min Rating Total for products higher than 300 but less than 800 ratings.
                     * High Rating Total for products with equal or more than 800 ratings.
                 '''),
    dcc.Markdown('''---'''),
    
    #fliter
    dcc.Markdown('''##### **Filter:**''',style ={'textAlign':'left','color':'indigo'}),
    dcc.Markdown('''**Pick Category:**''', ),
    dcc.Dropdown(id ="dropdown",
                 options = [{'label':'Beauty','value':'Beauty'},
                            {'label':'Electronics','value':'Electronics'},
                            {'label':'Furniture','value':'Furniture'},
                            {'label':'Grocery','value':'Grocery'},
                            {'label':'Health','value':'Health'},
                            {'label':'Household Essentials','value':'Household Essentials'},
                            {'label':'Kids','value':'Kids'},
                            {'label':'Kitchen & Dining','value':'Kitchen & Dining'},
                            {'label':'Men','value':'Men'},
                            {'label':'Movies, Music & Books','value':'Movies, Music & Books'},
                            {'label':'Personal Care','value':'Personal Care'},
                            {'label':'Pets','value':'Pets'},
                            {'label':'School & Office Supplies','value':'School & Office Supplies'},
                            {'label':'Sports & Outdoors','value':'Sports & Outdoors'},
                            {'label':'Toys','value':'Toys'},
                            {'label':'Video Games','value':'Video Games'},
                            {'label':'Women','value':'Women'}],
                             value=['Grocery','Furniture','Electronics'],multi =True,
                             style={"width": "60%", "offset":1,},clearable=False),
    html.Br(),
    dcc.Markdown('''**Ratings Total Level:**'''),
    dcc.Checklist(['Low Ratings Total','Mid Ratings Total','High Ratings Total'],['Low Ratings Total','Mid Ratings Total','High Ratings Total'],
                      inline=True, id="checklist"),
    
    html.Br(),
    dcc.Markdown('''**Price:**'''),
    dcc.Slider(min=0, max=600, 
               marks={0:"$0",
                      10:"10",
                      25:"$25",
                      50:"$50",
                      100:'$100',
                      200:'$200',
                      300:'$300',
                      400:'$400',
                      500:'$500',
                      600:'$600'}, 
               value=20, id='price_sliders'),
    
    #graph
    dcc.Markdown('''---'''),
    dcc.Markdown('''##### **Graph:**''',style ={'textAlign':'left','color':'indigo'}),
    dcc.Graph(figure=fig, id="graph"),
    dcc.Markdown('''---'''),
    dcc.Markdown('''##### **Products Table:**''',style ={'textAlign':'left','color':'indigo'}),
    
    
    #table
    dash_table.DataTable(id = 'table',
                         style_data={'whiteSpace': 'normal','height': 'auto',},
                         columns = [{"name":i, "id":i,"presentation":"markdown" } for i in df.columns],
                         page_current=0, page_size = Page_size, page_action = 'custom',
                         sort_action = 'custom', sort_mode='multi',sort_by=[],
                         markdown_options={"html":True}),
    
    
    ])

                 
@app.callback(
    Output(component_id="graph",component_property="figure"),
    Input(component_id="dropdown",component_property="value"),
    Input(component_id="checklist",component_property="value"),
    Input(component_id="price_sliders",component_property="value"))
def update_bar_chart(category, level, price):
    df_c = df[(df.category.isin(category)) & (df.ratings_total_levels.isin(level)) & (df.price <= price)]
    fig = px.histogram(df_c, x="rating", color = "category", title="Number of Target Bestsellers by Category")
    return fig

@app.callback(
    Output(component_id="table",component_property="data"),
    Input(component_id="table",component_property="page_current"),
    Input(component_id="table",component_property="page_size"),
    Input(component_id="table",component_property="sort_by"),
    Input(component_id="dropdown",component_property="value"),
    Input(component_id="checklist",component_property="value"),
    Input(component_id="price_sliders",component_property="value"))

def update_table(page_current, page_size, sort_by, category, level, price):
    df3 = df[(df.category.isin(category)) & (df.ratings_total_levels.isin(level)) & (df.price <= price)]
    print(sort_by)
    if len(sort_by):
        df_s = df3.sort_values([col['column_id'] for col in sort_by],
                              ascending=[col['direction']=='asc' for col in sort_by],
                              inplace=False)
    else:
        df_s = df3
    return df_s.iloc[page_current*page_size:(page_current+1)*page_size].to_dict('records')



if __name__ == '__main__':
    app.run_server(debug=True)



