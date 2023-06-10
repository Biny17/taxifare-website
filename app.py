import streamlit as st
import datetime as dt
import requests
import pandas as pd


predict_url = 'https://taxifare.lewagon.ai/predict'


# ask user for inputs
# inputs: pickup_datetime, pickup_longitude, pickup_latitude,
# dropoff_longitude, dropoff_latitude, passenger_count

st.image("https://logovtor.com/wp-content/uploads/2020/10/le-wagon-logo-vector.png", width=200)
st.image("https://images.unsplash.com/photo-1499353965760-b85389474bef?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDE0fHx8ZW58MHx8fHx8&w=1000&q=80")

# title how much will you pay for a taxi ride in NYC?
st.title("How much will you pay for a taxi ride in NYC?")

cols = st.columns((3, 5, 4))

with cols[0]:
    passengers = st.number_input("How many passengers?",step=1, min_value=1, max_value=8)
with cols[1]:
    pickup_date= st.date_input("Pickup date", dt.datetime.today())
with cols[2]:
    pickup_time = st.time_input("Pickup time", dt.datetime.now().time(), step=60)
pickup_datetime = dt.datetime.combine(pickup_date, pickup_time)

cols2 = st.columns((2, 2, 2, 2))

args = dict(
    format = '%.5f',
    step = 0.0001,
)
with cols2[0]:
    pickup_longitude = st.number_input("Pickup longitude",**args, value=-73.978)
with cols2[1]:
    pickup_latitude = st.number_input("Pickup latitude", **args)
with cols2[2]:
    dropoff_longitude = st.number_input("Dropoff longitude",**args)
with cols2[3]:
    dropoff_latitude = st.number_input("Dropoff latitude",**args)

X = dict(
    pickup_datetime = str(pickup_datetime),
    passenger_count = str(passengers),
    pickup_longitude = str(pickup_longitude),
    pickup_latitude = str(pickup_latitude),
    dropoff_longitude = str(dropoff_longitude),
    dropoff_latitude = str(dropoff_latitude)
)

if st.button('# Get Price : 💸'):
    response = requests.get(predict_url, params=X)
    fare = response.json()["fare"]
    st.write(f"### You will pay {fare:.2f} $ for this ride")
    df = pd.DataFrame.from_dict({
        "lat":[pickup_latitude, dropoff_latitude],
        "lon":[pickup_longitude, dropoff_longitude]
    })
    st.map(df)
