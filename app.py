import streamlit as st
from train_calculator import render_train_calculator
from t10_calculator import render_t10_calculator
from arms_race_calculator import render_arms_race_calculator

st.set_page_config(
    page_title="Last War Calculators",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🎮"
)

with st.sidebar:
    st.header("🛠 Select Calculator")
    calculator = st.radio("Choose a calculator", [
        "🚂 Train Calculator",
        "💎 T10 Resource Calculator",
        "⚔️ Arms Race Calculator"
    ])

if calculator == "🚂 Train Calculator":
    render_train_calculator()
elif calculator == "💎 T10 Resource Calculator":
    render_t10_calculator()
elif calculator == "⚔️ Arms Race Calculator":
    render_arms_race_calculator()
