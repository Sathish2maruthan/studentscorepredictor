import streamlit as st
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        color: white;
        background: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)
import pickle
import numpy as np

with open("student_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.title("Final Score Prediction")
st.write("Enter the following details:")


# Use columns for a modern, organized layout
col1, col2 = st.columns(2)

with col1:
    Hours_Studied = st.number_input(
        "📚 Hours Studied",
        min_value=0,
        max_value=24,
        help="Enter the number of hours you studied per day."
    )
    Assignments_Completed = st.number_input(
        "📝 Assignments Completed",
        min_value=0,
        max_value=50,
        help="Total assignments you have completed."
    )
    Extra_Activities = st.number_input(
        "🎯 Extra-curricular Activities (hours/week)",
        min_value=0,
        max_value=20,
        help="Hours spent on extra-curricular activities per week."
    )

with col2:
    Attendance = st.slider(
        "🏫 Attendance (%)",
        min_value=0,
        max_value=100,
        help="Your attendance percentage in class."
    )
    Sleep_Hours = st.slider(
        "😴 Sleep Hours",
        min_value=0,
        max_value=12,
        help="Average hours of sleep per day."
    )

if st.button("Predict"):
    features = np.array([[Hours_Studied, Attendance, Assignments_Completed, Sleep_Hours, Extra_Activities]])
    prediction = model.predict(features)
    st.write(f"Predicted Final Score: {prediction[0]}")
