import streamlit as st
import pandas as pd

# 1. SET PAGE CONFIG (The tab name and icon)
st.set_page_config(page_title="MYNDLY // ALPHA", page_icon="🧠", layout="centered")

# 2. THE DESIGN (Dark Mode + Founder Blue)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    h1 { color: #007AFF; font-family: 'Courier New', monospace; letter-spacing: -2px; font-weight: 800; }
    .stButton>button { background-color: #007AFF; color: white; border-radius: 8px; width: 100%; font-weight: bold; }
    .stMetric { background-color: #161B22; border-radius: 10px; padding: 15px; border: 1px solid #30363D; }
    </style>
    """, unsafe_allow_html=True)

# 3. PUBLIC MANIFESTO
st.title("MYNDLY // ALPHA")
st.subheader("The Operating System for your brain.")

st.write("""
Standard education was built for a world that doesn't exist anymore. 
At **Myndly**, we don't believe in 'disorders'—we believe in different drives. 
We identify your **Core Drive** so you can stop studying harder and start executing faster.
""")

# 4. THE PRESSURE COUNTER (FOMO)
st.write("---")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="FOUNDING SPOTS LEFT", value="14 / 200", delta="-3 since last hour")
with col2:
    st.metric(label="SYSTEM STATUS", value="ONLINE", delta="ACTIVE NODES: 186")

st.warning("⚠️ Access codes are rotating. If yours fails, wait for the next drop.")

# 5. THE INVITE GATE
st.write("---")
st.markdown("### 🔐 UNLOCK THE RIDE")
access_code = st.text_input("ENTER ACCESS CODE", type="password", help="Hand-delivered to Alpha testers only.")

# YOUR SECRET CODE
SECRET_KEY = "MYNDLY_RIDE_2026"

if access_code:
    if access_code == SECRET_KEY:
        st.success("ACCESS GRANTED. Welcome to the Inner Circle.")
        
        # --- HIDDEN ALPHA CONTENT ---
        with st.container():
            st.markdown("### 🧬 Welcome, Founder.")
            st.write("You are entering the Alpha phase of the most advanced learning diagnostic ever built.")
            
            name = st.text_input("Name")
            email = st.text_input("Email (where to send your Bio-Profile)")
            
            if st.button("CLAIM MY PROFILE & START DIAGNOSTIC"):
                if name and email:
                    st.balloons()
                    st.write(f"**Verification Complete.** Welcome to the ride, {name}. Check your email for your unique diagnostic link.")
                else:
                    st.error("Founder name and email required for profile generation.")
        # --- END HIDDEN CONTENT ---
    else:
        st.error("INVALID CODE. This phase is currently invite-only.")
        st.info("Follow @Myndly for the next code drop.")

st.write("---")
st.caption("© 2026 MYNDLY // Built for the Neuro-diverse.")

# Myndly Private Data
*.csv
*.log
