import streamlit as st
import pickle
import numpy as np


def load_cet_model():
    with open("entrance-board-prediction_decision-tree.pkl", "rb") as file:
        cet_model = pickle.load(file)
    return cet_model

def load_eat_model():
    with (open("aptitude-board-prediction_decision-tree.pkl", "rb")) as file:
        eat_model = pickle.load(file)
    return eat_model
