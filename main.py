import streamlit as st

st.title("Weather Forecast for the Next Days")  # this is not saved in a variable because it is not a dynamic/interactive widget
place = st.text_input("Place: ") # this is saved in a variable because it is a dynamic/interactive widget
days = st.slider("Forecast days", min_value=1, max_value=5,
                   help="Select the number of forecasted days")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")