import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt
import altair as alt
import numpy as np

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


venues = dataset.groupby(['venue','year'])['venue'].count().reset_index(name='count')
year = sorted(dataset.year.unique().tolist())
st.title("No. of matches in a particular venue for different years")
select_year = st.selectbox('Year:',year)
df5 = venues[ venues.iloc[:,1] == select_year]

venues_year = alt.Chart(df5).mark_bar().encode(
     x=alt.X('count:Q'),
     y= alt.Y('venue:N', sort = '-x'), color = alt.Color('venue:N')
).properties(width=800, height=500)

st.altair_chart(venues_year, use_container_width=True)

