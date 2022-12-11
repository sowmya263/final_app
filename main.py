import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt
import altair as alt
import numpy as np
from PIL import Image
import io

df = pd.read_csv("matches.csv")

df = df.drop(columns=["umpire3","umpire2","umpire1","id"])

teams = df["team1"].unique()

mapping = {'Sunrisers Hyderabad':"SRH", 'Mumbai Indians':"MI", 'Gujarat Lions':"GL",
       'Rising Pune Supergiant':"RPS", 'Royal Challengers Bangalore':"RCB",
       'Kolkata Knight Riders':"KKR", 'Delhi Daredevils':"DC", 'Kings XI Punjab':"KXIP",
       'Chennai Super Kings':"CSK", 'Rajasthan Royals':"RR", 'Deccan Chargers':"SRH",
       'Kochi Tuskers Kerala':"KTK", 'Pune Warriors':"RPS", 'Rising Pune Supergiants':"RPS",
       'Delhi Capitals':"DC"}

df["team1"] = df["team1"].map(mapping)
df["team2"] = df["team2"].map(mapping)
df["toss_winner"] = df["toss_winner"].map(mapping)
df["winner"] = df["winner"].map(mapping)


df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year
dataset = df.drop(columns=["date","Season"])

tab1, tab2, tab3 = st.tabs(['Ipl Dataset','Team Logos','Matches in all years']) 
with tab1: 
     st.title("IPL Dataset")
     dataset



#logos to teams
logos = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Gujarat Lions',
       'Rising Pune Supergiants', 'Royal Challengers Bangalore',
       'Kolkata Knight Riders', 'Kings XI Punjab',
       'Chennai Super Kings', 'Rajasthan Royals',
       'Kochi Tuskers Kerala',
       'Delhi Capitals']
with tab2:
     logo_selected = st.selectbox('Teams',logos)
     image1 = Image.open('Images/SRH.png')
     image2 = Image.open('Images/MI.png')
     image3 = Image.open('Images/GL.png')
     image4 = Image.open('Images/RPS.png')
     image5 = Image.open('Images/RCB.png')
     image6 = Image.open('Images/KKR.png')
     image7 = Image.open('Images/KXIP.png')
     image8 = Image.open('Images/CSK.png')
     image9 = Image.open('Images/RR.png')
     image10 = Image.open('Images/KTK.png')
     image11 = Image.open('Images/DC.png')

     if logo_selected == 'Sunrisers Hyderabad':
          st.image(image1, width=300)
     if logo_selected == 'Mumbai Indians':
          st.image(image2, width=300)
     if logo_selected == 'Gujarat Lions':
          st.image(image3, width=300)
     if logo_selected == 'Rising Pune Supergiants':
          st.image(image4, width=300)
     if logo_selected == 'Royal Challengers Bangalore':
          st.image(image5, width=300)
     if logo_selected == 'Kolkata Knight Riders':
          st.image(image6, width=300)
     if logo_selected == 'Kings XI Punjab':
          st.image(image7, width=300)
     if logo_selected == 'Chennai Super Kings':
          st.image(image8, width=300)
     if logo_selected == 'Rajasthan Royals':
          st.image(image9, width=300)
     if logo_selected == 'Kochi Tuskers Kerala':
          st.image(image10, width=300)
     if logo_selected == 'Delhi Capitals':
          st.image(image11, width=300)
     
with tab3:
     st.title("Year wise matches")
     matches_year = dataset.groupby(["year"])['year'].count().reset_index(name='count')
     bar = alt.Chart(matches_year).mark_bar(color='green').encode(
     x='year:O',
     y='count:Q'
     ).properties(width=800, height=500)
     st.altair_chart(bar, use_container_width=True)    
 
