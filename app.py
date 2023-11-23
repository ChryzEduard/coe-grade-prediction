import streamlit as st
import sklearn
import pickle
import numpy as np


from sklearn.tree import DecisionTreeClassifier
##dtree = DecisionTreeClassifier

st.set_page_config(
    menu_items = {},    
    page_title = "Engineering Prediction",
    page_icon = "book",
    layout = "wide",
)

def load_cet_model():
    with open("dt_cet_model.pkl", "rb") as file:
        cet_model = pickle.load(file)
    return cet_model

def load_eat_model():
    with (open("dt_eat_model.pkl", "rb")) as file:
        eat_model = pickle.load(file)
    return eat_model

dt_classifier_cet = load_cet_model()
dt_classifier_eat = load_eat_model()

## EnglishProficiency	ReadingComprehenshion	ScienceProcessSkills	QuantitativeSkills	AbstractThinkingSkills	
## Vocabulary	Knowledge&Comprehenshion	AbstractReasoning	ComputationalSkill	LogicalReasoning



st.write("""
# College of Engineering
Prediction of Students Success in Engineering Board Exams
         """)

c1, c2 = st.columns(2)
with c1:
   st.write("### CET Results")
   ep = st.number_input(
       "English Proficiency", # Input title
        min_value = 0.00,     # Minimum
        max_value = 100.00,    # Maximum
   )
   rc = st.number_input(
       "Reading Comprehension", # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00      # Maximum
   )
   sps = st.number_input(
       "Science Process Skills",    # Input title
        min_value = 0.00,           # Minimum
        max_value = 100.00          # Maximum
   )
   qs = st.number_input(
       "Quantitative Skills",   # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00      # Maximum
   )
   ats = st.number_input(
       "Abstract Thinking Skills",  # Input title
        min_value = 0.00,           # Minimum
        max_value = 100.00          # Maximum
   )
   # ep, rc, sps, qs, ats
   # v, kc, ar, cs, lr

with c2:    
   st.write("### EAT Results")
   voc = st.number_input(
       "Vocabulary",        # Input title
        min_value = 0,      # Minimum
        max_value = 30      # Maximum
   )
   kc = st.number_input(
       "Knowledge & Comprehension", # Input title
        min_value = 0,              # Minimum
        max_value = 30              # Maximum
   )
   ar = st.number_input(
       "Abstract Reasoning", # Input title
        min_value = 0,       # Minimum
        max_value = 30       # Maximum
   )
   cs = st.number_input(
       "Computational Skill", # Input title
        min_value = 0,        # Minimum
        max_value = 30        # Maximum
   )
   lr = st.number_input(
       "Logical Reasoning", # Input title
        min_value = 0,      # Minimum
        max_value = 30      # Maximum
   )

predict_call = st.button("Predict")

if predict_call:
    cet_result = "Fail"
    eat_result = "Fail"
    entrance_data_x = np.array([[ep, rc, sps, qs, ats]])
    aptitude_data_x = np.array([[voc, kc, ar, cs, lr]])

    # Make predictions
    cet_predictions = dt_classifier_cet.predict(entrance_data_x)
    if cet_predictions[0] == 1:
        cet_result = "Pass"
    st.subheader(f"CET prediction is: {cet_result}")
    eat_predictions = dt_classifier_eat.predict(entrance_data_x)
    if eat_predictions[0] == 1:
        eat_result = "Pass"
    st.subheader(f"EAT prediction is: {eat_result}")
