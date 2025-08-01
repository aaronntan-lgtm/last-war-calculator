import streamlit as st
from train_calculator import render_train_calculator
from t10_calculator import render_t10_calculator
from arms_race_calculator import render_vs_duel_calculator


st.markdown("""
    <style>
        .block-container {
            padding-top: 2.5rem;
        }
        header .css-18ni7ap.e8zbici2::after {
            content: "More Calculators";
            font-weight: bold;
            color: #666;
            margin-left: 12px;
        }
    </style>
""", unsafe_allow_html=True)

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
        "⚔️ VS Duel Calculator"
    ])

if calculator == "🚂 Train Calculator":
    render_train_calculator()
elif calculator == "💎 T10 Resource Calculator":
    render_t10_calculator()
elif calculator == "⚔️ VS Duel Calculator":
    render_vs_duel_calculator()
