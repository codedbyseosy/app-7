import streamlit as st
import plotly.express as px
from backend import get_data()

st.title("Weather Forecast for the Next Days")  # this is not saved in a variable because it is not a dynamic/interactive widget
place = st.text_input("Place: ") # this is saved in a variable because it is a dynamic/interactive widget
days = st.slider("Forecast days", min_value=1, max_value=5,
                   help="Select the number of forecasted days")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

# Plotting the graph
data = get_data(place, days, option)

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"}) # plot a "LINE" graph
                # x and y should be array type objects i.e. lists, tuples etc
                # x and y should be the same length
                # labels should be a dictionary
st.plotly_chart(figure) # 