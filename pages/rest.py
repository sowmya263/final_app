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




#toss decisions and win by wickets
toss_decisions = dataset.groupby(['toss_decision'])['toss_decision'].count().reset_index(name = 'count')
toss_decisions
decision_bar = alt.Chart(toss_decisions).mark_bar().encode(
     x=alt.X('toss_decision:N'),
     y=alt.Y('count:Q')
)
st.altair_chart(decision_bar, use_container_width=True)

#win by wickets
wins_wicket = dataset.groupby(['win_by_wickets'])['win_by_wickets'].count().reset_index(name = 'count')

wickets_win = alt.Chart(wins_wicket).mark_area(color='green').encode(
    x=alt.X('win_by_wickets:O'),
    y=alt.Y('count:Q')
 
).transform_filter('datum.win_by_wickets != 0')

st.altair_chart(wickets_win, use_container_width=True)

#win by runs
wins_runs = dataset.groupby(['win_by_runs'])['win_by_runs'].count().reset_index(name = 'count')
wins_runs

histogram = alt.Chart(wins_runs).mark_bar().encode(
    alt.X("win_by_runs:Q", bin=alt.Bin(maxbins=18)),
    y='count()',
)
histogram