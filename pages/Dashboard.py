import streamlit as st
import pandas as pd
import numpy as np
#import datetime maybe need this for graphing

if 'daily_focus_score' not in st.session_state:
    st.session_state['daily_focus_score'] = 0

if 'daily_effort_score' not in st.session_state:
    st.session_state['daily_effort_score'] = 0

if 'cycle_counter' not in st.session_state: 
    st.session_state['cycle_counter'] = 0

if 'subject_array' not in st.session_state:
    st.session_state['subject_array'] = subject_array = ["Machine Learning", "HCI and AI", "Service Design Studio", "HASS"]

if 'csv_filepath' not in st.session_state:
    st.session_state['csv_filepath'] = "actual_HCI_data.csv"

local_CSV_filepath = st.session_state['csv_filepath']

df = pd.read_csv(local_CSV_filepath) 

st.header("Overview")

st.title("Study Progress Dashboard")

df2 = df[['effort_score', 'fatigue_score']]
# st.write(df2)

# Generating dummy metrics. Put in functions here
daily_avg_effort = st.session_state['daily_effort_score'] / st.session_state['cycle_counter'] if st.session_state['cycle_counter'] > 0 else 0
daily_avg_focus = st.session_state['daily_focus_score'] / st.session_state['cycle_counter'] if st.session_state['cycle_counter'] > 0 else 0
daily_cycles = st.session_state['cycle_counter']
daily_effort_score = st.session_state['daily_effort_score']
daily_avg_focus = st.session_state['daily_focus_score'] / st.session_state['cycle_counter'] if st.session_state['cycle_counter'] > 0 else 0
daily_cycles = st.session_state['cycle_counter']
#daily_effort_score = [daily_avg_effort[i] * daily_cycles[i] for i in range(31)]

# Creating dataframe data
#effort_data = pd.DataFrame(daily_effort_score, index=range(1, 32), columns=["Cycles x Average Effort Score"])
#effort_data = pd.DataFrame(df['effort_score'], index=range(1, 32), columns=["Cycles x Average Effort Score"])
effort_data = df['effort_score']
effort_data = df2
#focus_data = pd.DataFrame(daily_avg_focus, index=range(1, 32), columns=["Average Focus Score"])
focus_data = df['fatigue_score']

# Metrics for each subject
st.header("These metrics show how your effort score is trending for each subject.")
st.subheader("In the past week:")
subject_array = st.session_state['subject_array']
col1, col2, col3, col4 = st.columns(4)

#calculate the average effort_score for HASS
HASS_effort_score = df['effort_score'][df['subject'] == 'HASS']
HASS_effort_score_avg = round(np.mean(HASS_effort_score), 1)

#calculate the average effort_score for HCI and AI
HCI_AI_effort_score = df['effort_score'][df['subject'] == 'HCI and AI']
HCI_AI_effort_score_avg = round(np.mean(HCI_AI_effort_score), 1)

#calculate the average effort_score for Machine Learning
ML_effort_score = df['effort_score'][df['subject'] == 'Machine Learning']
ML_effort_score_avg = round(np.mean(ML_effort_score), 1)

#calculate the average effort_score for Service Design Studio
SDS_effort_score = df['effort_score'][df['subject'] == 'Service Design Studio']
SDS_effort_score_avg = round(np.mean(SDS_effort_score), 1)

col1.metric("Machine Learning", ML_effort_score_avg, "-2")
col2.metric("HCI and AI", HCI_AI_effort_score_avg, "3.5")
col3.metric("Service Design Studio", SDS_effort_score_avg, "2.8")
col4.metric("HASS", HASS_effort_score_avg, "-3.1")

# col1.metric("Machine Learning", "6.4", "-2")
# col2.metric("HCI and AI", "9.1", "3.5")
# col3.metric("Service Design Studio", "7.7", "2.8")
# col4.metric("HASS", HASS_effort_score_avg, "-3.1")

# Horizontal line to divide the page
st.markdown("""---""")
st.subheader("In the past month:")
st.header('Overall Effort & Fatigue') # Graph 1
# st.subheader('This chart shows your average effort multiplied\
#      by your number of Pomodoro cycles.')
st.line_chart(effort_data)

#calculate average effort_score


col1, col2 = st.columns(2)
col1.metric("Overall Effort", round(df['effort_score'].mean(), 1), "+1.2")
col2.metric("Overall fatigue", round(df["fatigue_score"].mean(), 1), "-0.7", delta_color='inverse')

# st.header('Focus') # Graph 2
# # st.subheader('This chart shows your average focus.')
# st.line_chart(focus_data)

# st.header("Weekly Average Study Time") # Graph 3
# # Generate dataframe data with each hour in the day on horizontal axis
# # and different study times on vertical axis
# study_times = [np.random.randint(1, 6) for i in range(24)]
# study_times_data = pd.DataFrame(study_times, index=range(1, 25), columns=["Study Time"])
# st.bar_chart(study_times_data)

st.session_state["dropdown_toggle"] = st.selectbox("View by subject", subject_array)

if st.session_state["dropdown_toggle"]:
    st.header("This week: " + st.session_state["dropdown_toggle"])
    #create a dataframe with the data for the selected subject, and only the effort_score and focus_score columns
    ml_data = df[df['subject'] == st.session_state["dropdown_toggle"]]
    #create a dataframe with only time and effort score
    ml_data_time_effort = ml_data[['effort_score', 'fatigue_score']]
    #change the index of the dataframe to be a count from 1 to the number of rows
    ml_data_time_effort.index = range(1, len(ml_data_time_effort) + 1)

    #st.write(ml_data_time_effort)
    st.line_chart(ml_data_time_effort)
    #generate the sum of minutes spent on the subject
    metrics = ml_data[['time_minutes']]
    #return sum of value in metrics

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total minutes", sum(metrics['time_minutes']))
    col2.metric("Number of cycles", len(ml_data['effort_score']))
    col3.metric("Average effort score", round(np.mean(ml_data['effort_score']), 1))
    col4.metric("Average fatigue score", round(np.mean(ml_data['fatigue_score']), 1))

    st.subheader("AI recommendations:")
    if st.session_state["dropdown_toggle"] == "Machine Learning":
        st.write("Keep up the good work!")
        st.write("Fatigue scores are trending higher. 20/10 cycles may suit you better.")
    if st.session_state["dropdown_toggle"] == "HCI and AI":
        st.write("You tend to do better in the morning with this subject.")
    if st.session_state["dropdown_toggle"] == "Service Design Studio":
        st.write("You tend to do better in the afternoon with this subject. Longer 50/10 cycles may suit you better.")
    if st.session_state["dropdown_toggle"] == "HASS":
        st.write("You may need to put in more time with this subject. You tend to have higher effort scores in the night.")




