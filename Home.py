import streamlit as st


if 'minutes_today' not in st.session_state:
    st.session_state['minutes_today'] = 0

if 'cycle_counter' not in st.session_state: 
    st.session_state['cycle_counter'] = 0

st.header("Welcome to the Optidoro Timer, Mandy!")

# import pandas as pd
# import numpy as np

# if 'csv_filepath' not in st.session_state:
#     st.session_state['csv_filepath'] = "actual_HCI_data.csv"

# local_CSV_filepath = st.session_state['csv_filepath']

# df = pd.read_csv(local_CSV_filepath) 

# #calculate the average effort_score for HASS
# HASS_effort_score = df['effort_score'][df['subject'] == 'HASS']
# HASS_effort_score_avg = round(np.mean(HASS_effort_score), 1)

# #calculate the average effort_score for HCI and AI
# HCI_AI_effort_score = df['effort_score'][df['subject'] == 'HCI and AI']
# HCI_AI_effort_score_avg = round(np.mean(HCI_AI_effort_score), 1)

# #calculate the average effort_score for Machine Learning
# ML_effort_score = df['effort_score'][df['subject'] == 'Machine Learning']
# ML_effort_score_avg = round(np.mean(ML_effort_score), 1)

# #calculate the average effort_score for Service Design Studio
# SDS_effort_score = df['effort_score'][df['subject'] == 'Service Design Studio']
# SDS_effort_score_avg = round(np.mean(SDS_effort_score), 1)

# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Machine Learning", ML_effort_score_avg, "-2")
# col2.metric("HCI and AI", HCI_AI_effort_score_avg, "3.5")
# col3.metric("Service Design Studio", SDS_effort_score_avg, "2.8")
# col4.metric("HASS", HASS_effort_score_avg, "-3.1")

st.metric("Optidoro cycles today", st.session_state['cycle_counter'])
st.metric("Minutes today", st.session_state['minutes_today'])