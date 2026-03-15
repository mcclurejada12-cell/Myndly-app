import streamlit as st
import pandas as pd

# 1. SET PAGE CONFIG
st.set_page_config(page_title="MYNDLY // ALPHA", page_icon="🧠", layout="centered")

# 2. THE DESIGN (Luxe-Violet & Deep Space - Matching your Screenshot)
st.markdown("""
    <style>
    /* Main Background - Deep Obsidian */
    .stApp { 
        background-color: #0A0A0C; 
        color: #F0F0F5; 
    }
    
    /* Title Styling - Electric Violet with Glow */
    h1 { 
        color: #A855F7; 
        font-family: 'Inter', sans-serif; 
        letter-spacing: -3px; 
        font-weight: 900; 
        text-transform: uppercase;
        text-shadow: 0px 0px 20px rgba(168, 85, 247, 0.4);
        padding-top: 20px;
    }

    /* Subheader - Soft Lilac */
    h3 { 
        color: #D8B4FE; 
        font-weight: 300;
        letter-spacing: 1px;
    }

    /* The Button - Violet Gradient with Hover Glow */
    .stButton>button { 
        background: linear-gradient(90deg, #7C3AED, #A855F7);
        color: white; 
        border-radius: 12px; 
        border: none;
        padding: 15px;
        font-weight: 700;
        transition: 0.3s;
        box-shadow: 0px 4px 15px rgba(124, 58, 237, 0.3);
        width: 100%;
    }
    
    .stButton>button:hover {
        box-shadow: 0px 0px 25px rgba(168, 85, 247, 0.6);
        transform: translateY(-2px);
        color: white;
    }

    /* Metrics / Cards - Glassmorphism Panels */
    [data-testid="stMetric"] { 
        background-color: #16161E; 
        border-radius: 15px; 
        padding: 20px; 
        border: 1px solid #2D2D39;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    }

    /* Input Box Styling */
    .stTextInput>div>div>input {
        background-color: #1A1A24;
        color: #FFFFFF;
        border: 1px solid #3F3F46;
        border-radius: 10px;
    }

    /* Divider color */
    hr {
        border-color: #2D2D39;
    }
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
