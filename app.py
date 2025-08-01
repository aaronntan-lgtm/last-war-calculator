import streamlit as st

st.set_page_config(
    page_title="Last War Calculators",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🎮"
)

# Sidebar for calculator selection
with st.sidebar:
    st.header("🛠 Select Calculator")
    calculator = st.selectbox("Choose a calculator", [
        "🚂 Train Calculator",
        "💎 T10 Resource Calculator",
        "⚔️ Arms Race Calculator"
    ])

# Route to the selected calculator
if calculator == "🚂 Train Calculator":
    from train_calculator import *
elif calculator == "💎 T10 Resource Calculator":
    from t10_calculator import *
elif calculator == "⚔️ Arms Race Calculator":
    from arms_race_calculator import *
