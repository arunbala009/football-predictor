import streamlit as st
import pickle
import numpy as np

model=pickle.load(
open(
"model.pkl",
"rb"))

team_stats=pickle.load(
open(
"team_stats.pkl",
"rb"))

teams=list(
team_stats.keys())

st.title(
"⚽ European Football Predictor")

home=st.selectbox(
"Home Team",
teams)

away=st.selectbox(
"Away Team",
teams)

if st.button(
"Predict"):

    features=np.array([[
        0,
        0,
        team_stats[home]["avg_goals"],
        team_stats[away]["avg_goals"],
        team_stats[home]["winrate"],
        team_stats[away]["winrate"]
    ]])

    pred=model.predict(features)[0]

    if pred==2:
        st.success(
        f"{home} likely to win")

    elif pred==1:
        st.warning(
        "Likely Draw")

    else:
        st.error(
        f"{away} likely to win")