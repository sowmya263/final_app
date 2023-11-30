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


df["date"] = pd.to_datetime(df["date"], errors = 'coerce')

df["year"] = df["date"].dt.year
dataset = df.drop(columns=["date","Season"])

#wins of all teams each year
st.title("Number of wins of all teams of all years")
year = sorted(dataset.year.unique().tolist())
year_selecter = st.selectbox("Year:",year)
wins_year = dataset.groupby(['winner','year'])['winner'].count().reset_index(name='count')

df1 = wins_year[ wins_year.iloc[:,1] == year_selecter]
bar_wins = alt.Chart(df1).mark_bar().encode(
     x=alt.X('winner:N', sort = '-y'),
     y= alt.Y('count:Q'), color = alt.Color('winner:N')
).properties(width=800, height=500)

st.altair_chart(bar_wins, use_container_width=True)

