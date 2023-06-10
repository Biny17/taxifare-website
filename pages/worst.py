import streamlit as st
import requests

predict_url = 'https://taxifare.lewagon.ai/predict'


# ask user for inputs
# inputs: pickup_datetime, pickup_longitude, pickup_latitude,
# dropoff_longitude, dropoff_latitude, passenger_count

passengers = st.radio("How many passengers?", [1, 2, 3, 4, 5, 6, 7, 8])
