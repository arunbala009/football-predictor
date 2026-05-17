import streamlit as st
import pickle
import xgboost
import sklearn

model=pickle.load(
open(
'model.pkl',
'rb'))

encoder=pickle.load(
open(
'encoder.pkl',
'rb'))

teams=[
'Real Madrid',
'Barcelona',
'Manchester City',
'Liverpool',
'Arsenal',
'Bayern Munich',
'PSG',
'Inter Milan'
]

st.title(
"European Football Predictor")

home=st.selectbox(
"Home Team",
teams)

away=st.selectbox(
"Away Team",
teams)

goals1=st.number_input(
"Home Goals")

goals2=st.number_input(
"Away Goals")

shots1=st.number_input(
"Home Shots")

shots2=st.number_input(
"Away Shots")

if st.button(
"Predict"):

 home=encoder.transform([home])[0]

 away=encoder.transform([away])[0]

 result=model.predict(
 [[
 home,
 away,
 goals1,
 goals2,
 shots1,
 shots2,
 2,
 1
 ]])

 if result==2:
     st.success(
     "Home Win")

 elif result==1:
     st.warning(
     "Draw")

 else:
     st.error(
     "Away Win")