import os
import time
import streamlit as st
import pandas as pd
import requests

API_HOST = os.getenv("API_HOST", "localhost")

pages = {
    "Dashboard": [
        st.Page("dashboard.py", "Dashboard", icon=":material/dashboard:"),
    ],
    "Settings": [
        st.Page("user_settings.py", "User Settings", icon=":material/settings_account_box:"),
        st.Page("trade_settings.py", "Trade Settings", icon=":material/credit_card_gear:"),
    ],
    "Strategy": [
        st.Page("strategy_management.py", "Strategy Management", icon=":material/folder_managed:"),
        st.Page("strategy_optimizer.py", "Strategy Optimizer", icon=":material/tune:"),
        st.Page("strategy_backtest.py", "Strategy Backtest", icon=":material/analytics:"),
        st.Page("strategy_upload.py", "Strategy Upload", icon=":material/upload_file:"),
    ],
    "Trade": [
        st.Page("trade_market.py", "Trade Market", icon=":material/account_balance:"),
        st.Page("trade_history.py", "Trade History", icon=":material/history:"),
    ],
}

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

st.write("Welcome to the home page")
st.write("Please select the page from the sidebar")

pg = st.navigation(pages)
pg.run()