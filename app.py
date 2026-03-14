import streamlit as st
import pandas as pd

# Set page config for that "Pro" look
st.set_page_config(page_title="MYNDLY // The Ride", page_icon="🧠", layout="centered")

# Custom CSS to make it look "Cyberpunk/Startup"
st.markdown("""
    <style>
    .main { background-color: #121212; }
    h1 { color: #007AFF; font-family: 'Courier New'; }
    .stButton>button { background-color: #1C1C1E; color: white; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("MYNDLY // ALPHA")
st.subheader("The brain doesn't come with a manual. We're building one.")

st.write("---")

# The Hook
st.markdown("### 🧬 Join the Ride")
st.write("We are identifying the 'Core Drive' of the next generation of learners. Take the Alpha Diagnostic to claim your spot.")

# The Form
with st.form("waitlist_form"):
    name = st.text_input("First Name")
    email = st.text_input("Email (to receive your profile)")
    interest = st.selectbox("Your Biggest Struggle:", ["Staying Focused", "Sitting Still", "Remembering Text", "Group Projects"])
    
    submit = st.form_submit_button("UNLOCk MY PROFILE")

if submit:
    if name and email:
        st.success(f"Welcome to the ride, {name}! You're on the list. Check your email for the Alpha link soon.")
        # In a real app, this saves to a database. For now, we celebrate!
        st.balloons()
    else:
        st.error("We need your name and email to secure your spot!")

st.write("---")
st.info("Built by Founders for the Neuro-diverse.")

# Myndly Private Data
*.csv
*.log
