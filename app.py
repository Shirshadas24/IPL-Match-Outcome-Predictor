import streamlit as st
import pickle
import pandas as pd

st.title("IPL Match Predictor")
teams= ["Chennai Super Kings", "Delhi Capitals", "Kolkata Knight Riders", 
         "Mumbai Indians", "Punjab Kings", "Rajasthan Royals", 
         "Sunrisers Hyderabad", "Gujarat Titans","Royal Challengers Bangalore",
         "Lucknow Super Giants"]
city= ['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']
pipe=pickle.load(open('ra_pipe.pkl', 'rb'))
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox("Select Batting Team", sorted(teams))
with col2:
    bowling_team = st.selectbox("Select Bowling Team", sorted(teams))
venue = st.selectbox("Select Venue", sorted(city))
target = st.number_input("Target")
col3, col4,col5 = st.columns(3)
with col3:
    score = st.number_input("Score")
with col4:
    overs = st.number_input("Overs", min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input("Wickets", min_value=0, max_value=10, step=1)
if st.button("Predict"):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr= score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df= pd.DataFrame({'batting_team': [batting_team],
                            'bowling_team': [bowling_team],
                            'city': [venue],
                            'runs_left': [runs_left],
                            'balls_left': [balls_left],
                            'wickets_remaining': [wickets],
                            'total_run_x':[target],
                            'crr': [crr],
                                'rrr': [rrr]})
    
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.subheader("Predicted Result")
    st.write(f"Chances of {batting_team} winning: {win * 100:.2f}%")
    st.write(f"Chances of {bowling_team} winning: {loss * 100:.2f}%")
