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
dataset
st.title("Bar Graph of Matches year wise")
matches_year = dataset.groupby(["year"])['year'].count().reset_index(name='count')
bar = alt.Chart(matches_year).mark_bar().encode(
     x='year:O',
     y='count:Q'
).properties(width=800, height=500)
st.altair_chart(bar, use_container_width=True)

#pie chart for winning of teams
st.title("Pie chart of wins by teams")
pie_year = dataset.groupby(["winner"])['winner'].count().reset_index(name = 'count')
pie = alt.Chart(pie_year).mark_arc(outerRadius=120).encode(
     theta = alt.Theta("count:Q", stack=True), color=alt.Color("winner:N")
)
text = pie.mark_text(radius=140, size=15).encode(text="winner:N")
pie+text



#wins of all teams each year
st.title("Wins of teams of different years")
year = sorted(dataset.year.unique().tolist())
year_selecter = st.selectbox("Wins_Year",year)
wins_year = dataset.groupby(['winner','year'])['winner'].count().reset_index(name='count')

df1 = wins_year[ wins_year.iloc[:,1] == year_selecter ]
bar_wins = alt.Chart(df1).mark_bar().encode(
     x='winner:N',
     y= alt.Y('count:Q', sort = '-y')
).properties(width=800, height=500)

st.altair_chart(bar_wins, use_container_width=True)

#matches won, tosses won
st.title("Top 5 teams performance based on matches and tosses won")
matches_won = dataset.groupby(['winner'])['winner'].count().reset_index(name = 'count')
sorted_data = matches_won.sort_values("count", ascending=False)
df2 = sorted_data[['winner','count']].head(n=5)

tosses_won = dataset.groupby(['toss_winner'])['toss_winner'].count().reset_index(name = 'count')
tosses_won_sorted = tosses_won.sort_values("count", ascending=False)
df3 = tosses_won_sorted[['toss_winner','count']].head(n=5)

bar_top5 = alt.Chart(df2).mark_bar().encode(
     x=alt.X('count:Q', sort = '-x'),
     y=alt.Y('winner:N')
)


bar_top5tosses = alt.Chart(df3).mark_bar().encode(
  x=alt.X('count:Q', sort = '-x'),
     y=alt.Y('toss_winner:N')   
)

# adding two bar graphs in one graph
final2 = alt.vconcat(bar_top5, bar_top5tosses)
final2

#ity","team1","team2","toss_winner","toss_decision","result","dl_applied",
#"winner","win_by_runs","win_by_wickets","player_of_match"

#scatter and correlation coefficient
#st.header("Pick two variables for your scatterplot")
#x_val = st.selectbox("Pick your x-axis",dataset.columns.tolist())
#y_val = st.selectbox("Pick your y-axis",dataset.columns.tolist())

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

density = alt.Chart(wins_wicket).mark_area(color='green').encode(
    x=alt.X('win_by_wickets:O'),
    y=alt.Y('count:Q')
 
).transform_filter('datum.win_by_wickets != 0') 

st.altair_chart(density, use_container_width=True)

# final3 = alt.vconcat(density, decision_bar, center = True)
# st.altair_chart(final3, use_container_width=True)
