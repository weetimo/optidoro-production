import streamlit as st

if 'minutes_today' not in st.session_state:
    st.session_state['minutes_today'] = 0

if 'cycle_counter' not in st.session_state: 
    st.session_state['cycle_counter'] = 0

st.header("Welcome to the Optidoro Timer, Mandy!")

st.metric("Optidoro cycles today", st.session_state['cycle_counter'])
st.metric("Minutes today", st.session_state['minutes_today'])