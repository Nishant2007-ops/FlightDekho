import requests
import streamlit as st

API_KEY = st.secrets["Aviation_api_key"]

def search_flights(dep_iata, arr_iata):

    url = "https://airlabs.co/api/v9/schedules"

    params = {
        "api_key": API_KEY,
        "dep_iata": dep_iata,
        "arr_iata": arr_iata
    }

    response = requests.get(url, params=params)

    return response.json()

