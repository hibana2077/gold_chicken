import os
import time
import streamlit as st
import pandas as pd
import requests

API_HOST = os.getenv("API_HOST", "localhost")

pages = {
    "Dashboard": [
        st.Page("./my_pages/dashboard.py", title="Dashboard", icon=":material/dashboard:"),
    ],
    "Settings": [
        st.Page("./my_pages/user_settings.py", title="User Settings", icon=":material/settings_account_box:"),
        st.Page("./my_pages/trade_settings.py", title="Trade Settings", icon=":material/credit_card_gear:"),
    ],
    "Strategy": [
        st.Page("./my_pages/strategy_management.py", title="Strategy Management", icon=":material/folder_managed:"),
        st.Page("./my_pages/strategy_optimizer.py", title="Strategy Optimizer", icon=":material/tune:"),
        st.Page("./my_pages/strategy_backtest.py", title="Strategy Backtest", icon=":material/analytics:"),
        st.Page("./my_pages/strategy_upload.py", title="Strategy Upload", icon=":material/upload_file:"),
    ],
    "Trade": [
        st.Page("./my_pages/trade_market.py", title="Trade Market", icon=":material/account_balance:"),
        st.Page("./my_pages/trade_history.py", title="Trade History", icon=":material/history:"),
    ],
}

if 'login' not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title('Login')
    with st.form(key='login_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            if not username or not password:
                st.warning("Please fill in both fields")
            if username == "test" and password == "test": # Test login, remove this in production
                st.session_state.login = True
                st.success("Login success")
                time.sleep(1)
                st.rerun()
            if username and password:
                response = requests.post(f"http://{API_HOST}/login", json={"username": username, "password": password})
                if response.json().get("status") == "success":
                    st.session_state.login = True
                    st.success("Login success")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Login failed")
else:
    pg = st.navigation(pages)
    pg.run()

