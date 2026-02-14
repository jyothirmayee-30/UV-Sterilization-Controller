import streamlit as st
import pandas as pd
import time
from datetime import datetime

st.set_page_config(page_title="Sterile-Sync Control", page_icon="🧼", layout="wide")

st.title("🧼 UV-C Sterilization Audit Dashboard")

if 'cycle_log' not in st.session_state:
    st.session_state.cycle_log = pd.DataFrame([
        {'Time': '09:00:05', 'Duration_Sec': 300, 'Status': 'Completed'},
        {'Time': '10:15:20', 'Duration_Sec': 45, 'Status': 'ABORTED - DOOR OPEN'}
    ])

placeholder = st.empty()

with placeholder.container():
    c1, c2, c3 = st.columns(3)
    
    total_cycles = len(st.session_state.cycle_log[st.session_state.cycle_log['Status'] == 'Completed'])
    c1.metric("Successful Cycles", total_cycles)
    
    lamp_life = 82  # Percentage
    c2.metric("UVC Lamp Health", f"{lamp_life}%", delta="-2% Weekly")
    
    c3.metric("Current Mode", "Standby")

    st.subheader("Recent Sterilization Events")
    st.dataframe(st.session_state.cycle_log, use_container_width=True)

    if any(st.session_state.cycle_log['Status'].str.contains('ABORTED')):
        st.error("🚨 SAFETY ALERT: Cycle aborted due to interlock breach at 10:15.")
