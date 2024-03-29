import streamlit as st
import pickle
import numpy as np
import sklearn

from sklearn.ensemble import RandomForestRegressor

# The code on the webpage metadata like tab title, tab icon, etc.
st.set_page_config(
    menu_items = {},    
    page_title = "Engineering Prediction",
    page_icon = "book",
    layout = "wide",
)

# Webpage title
st.write("""
# College of Engineering
Prediction of Students Success in Engineering Board Exams
         """)

#Input fields
c1, c2 = st.columns(2)
with c1:
   st.write("### CET Results")
   English_Proficiency = st.number_input(
       "English Proficiency", # Input title
        min_value = 0.00,     # Minimum
        max_value = 100.00,    # Maximum
        format="%.2f",
   )
   Reading_Comprehension = st.number_input(
       "Reading Comprehension", # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00,      # Maximum
        format="%.2f",
   )
   Science_Process_Skills = st.number_input(
       "Science Process Skills",    # Input title
        min_value = 0.00,           # Minimum
        max_value = 100.00,          # Maximum
        format="%.2f",
   )
   Quantitative_Skills = st.number_input(
       "Quantitative Skills",   # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00,      # Maximum
        format="%.2f",
   )
   Abstract_Thinking_Skills = st.number_input(
       "Abstract Thinking Skills",  # Input title
        min_value = 0.00,           # Minimum
        max_value = 100.00,          # Maximum
        format="%.2f",
   )
    
with c2:    
   st.write("### EAT Results")
   Vocabulary = st.number_input(
       "Vocabulary",        # Input title
        min_value = 0.00,      # Minimum
        max_value = 100.00,      # Maximum
        format="%.2f",
   )
   Knowledge_and_Comprehension = st.number_input(
       "Knowledge & Comprehension", # Input title
        min_value = 0.00,              # Minimum
        max_value = 100.00,              # Maximum
        format="%.2f",
   )
   Abstract_Reasoning = st.number_input(
       "Abstract Reasoning", # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00,       # Maximum
        format="%.2f",
   )
   Computational_Skill = st.number_input(
       "Computational Skill", # Input title
        min_value = 0.00,        # Minimum
        max_value = 100.00,        # Maximum
        format="%.2f",
   )
   Logical_Reasoning = st.number_input(
       "Logical Reasoning", # Input title
        min_value = 0.00,      # Minimum
        max_value = 100.00,      # Maximum
        format="%.2f",
   )



predict_call = st.button("Predict")
model = pickle.load(open("rfr_student_grade_modelv4.pkl", "rb"))
print(model)


if predict_call:
    main_data_x = np.array([[English_Proficiency, Reading_Comprehension, Science_Process_Skills, Quantitative_Skills, Abstract_Thinking_Skills, Vocabulary, Knowledge_and_Comprehension, Abstract_Reasoning, Computational_Skill, Logical_Reasoning]])


    # Make predictions
    main_predictions = model.predict(main_data_x)
    percent_prediction = main_predictions * 100
    prediction_str = "{:.0f}".format(percent_prediction[0])
    st.subheader(f"Prediction is: {prediction_str}% probability of passing the board exam")
    if percent_prediction >= 70:
        st.subheader(f"High likelihood of passing")
    else:
        st.subheader(f"High likelihood of failing")
