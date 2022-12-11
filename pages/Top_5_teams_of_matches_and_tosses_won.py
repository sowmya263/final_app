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


#matches won, tosses won

matches_won = dataset.groupby(['winner'])['winner'].count().reset_index(name = 'count')
sorted_data = matches_won.sort_values("count", ascending=False)
df2 = sorted_data[['winner','count']].head(n=5)

tosses_won = dataset.groupby(['toss_winner'])['toss_winner'].count().reset_index(name = 'count')
tosses_won_sorted = tosses_won.sort_values("count", ascending=False)
df3 = tosses_won_sorted[['toss_winner','count']].head(n=5)
tab1, tab2 = st.tabs(['Top 5 tosses and winner teams','Top 10 Man of match players'])

bar_top5 = alt.Chart(df2).mark_bar().encode(
     x=alt.X('count:Q'),
     y=alt.Y('winner:N', sort='-x'), color = alt.Color('winner:N')
)


bar_top5tosses = alt.Chart(df3).mark_bar().encode(
  x=alt.X('count:Q'),
     y=alt.Y('toss_winner:N', sort='-x'), color = alt.Color('toss_winner:N')
)
# adding two bar graphs in one graph
with tab1:
    st.title("Top 5 teams performance based on matches and tosses won")
    final2 = alt.vconcat(bar_top5, bar_top5tosses)
    final2


with tab2:
    st.title("Top 10 man of the match players across all years")
    player_MOM = dataset.groupby(['player_of_match'])['player_of_match'].count().reset_index(name = 'count')
    player_MOM_sorted = player_MOM.sort_values("count", ascending=False)
    df4 = player_MOM_sorted[['player_of_match','count']].head(n=10)

    bar_MOM = alt.Chart(df4).mark_bar().encode(
        x=alt.X('count:Q'),
        y=alt.Y('player_of_match:N', sort='-x'), color = alt.Color('player_of_match:N')
    )
    st.altair_chart(bar_MOM, use_container_width=True)
