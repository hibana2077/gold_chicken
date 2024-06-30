import os
import time
import streamlit as st
import pandas as pd
import requests

API_HOST = os.getenv("API_HOST", "localhost")

if 'login' not in st.session_state:
    st.session_state.login = False

st.title('Home')

if not st.session_state.login:
    with st.form(key='login_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            response = requests.post(f"http://{API_HOST}/login", json={"username": username, "password": password})
            if response.json().get("status") == "success":
                st.session_state.login = True
                st.success("Login success")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Login failed")