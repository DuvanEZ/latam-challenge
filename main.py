import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from memory_profiler import memory_usage
#from src.q1_memory import q1_memory
#from src.q1_time import q1_time
from src.q2_memory import q2_memory
from src.q2_time import q2_time
from src.q3_memory import q3_memory
from src.q3_time import q3_time

def main():
    file_path = r"\Users\DZWorld2\Documents\Studying\challenge_option\tweets.json\farmers-protest-tweets-2021-2-4.json"

    # Prepare data for q1 and q2 without measuring execution time and memory usage
    #q1time = q1_time(file_path)
    #q1memory = q1_memory(file_path)
    q2time = q2_time(file_path)
    q2memory = q2_memory(file_path)
    q3time = q3_time(file_path)
    q3memory = q3_memory(file_path)

    #q1memory_df = pd.DataFrame(q1memory, columns=['Date', 'UserName', 'Count'])
    #q1time_df = pd.DataFrame(q1time, columns=['Date', 'UserName'])
    q2memory_df = pd.DataFrame(q2memory, columns=['Emoji', 'Count'])
    q2time_df = pd.DataFrame(q2time, columns=['Emoji', 'Count'])
    q3memory_df = pd.DataFrame(q3memory, columns=['Username', 'Count'])
    q3time_df = pd.DataFrame(q3time, columns=['Username', 'Count'])

    # Sidebar for question selection
    st.sidebar.title("Select Question")
    question = st.sidebar.radio("Choose a question to view", ("Question 2", "Question 3"))

    st.title("Twitter Data Analysis")

    # Create separate containers for each table
    container_q2_time = st.empty()
    container_q2_memory = st.empty()
    container_q3_time = st.empty()
    container_q3_memory = st.empty()

    if question == "Question 2":
        with container_q2_time.container():
            st.header("Question 2")
            st.subheader("Execution Time")
            fig_q2_time = go.Figure(data=[go.Table(
                header=dict(values=list(q2time_df.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[q2time_df[col] for col in q2time_df.columns],
                           fill_color='lavender',
                           align='left'))
            ])
            st.plotly_chart(fig_q2_time)

        with container_q2_memory.container():
            st.subheader("Memory Usage")
            fig_q2_memory = go.Figure(data=[go.Table(
                header=dict(values=list(q2memory_df.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[q2memory_df[col] for col in q2memory_df.columns],
                           fill_color='lavender',
                           align='left'))
            ])
            st.plotly_chart(fig_q2_memory)

        # Clear the containers for question 3
        container_q3_time.empty()
        container_q3_memory.empty()

    elif question == "Question 3":
        with container_q3_time.container():
            st.header("Question 3")
            st.subheader("Execution Time")
            fig_q3_time = go.Figure(data=[go.Table(
                header=dict(values=list(q3time_df.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[q3time_df[col] for col in q3time_df.columns],
                           fill_color='lavender',
                           align='left'))
            ])
            st.plotly_chart(fig_q3_time)

        with container_q3_memory.container():
            st.subheader("Memory Usage")
            fig_q3_memory = go.Figure(data=[go.Table(
                header=dict(values=list(q3memory_df.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[q3memory_df[col] for col in q3memory_df.columns],
                           fill_color='lavender',
                           align='left'))
            ])
            st.plotly_chart(fig_q3_memory)

        # Clear the containers for question 2
        container_q2_time.empty()
        container_q2_memory.empty()

if __name__ == '__main__':
    main()
