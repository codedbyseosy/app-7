import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")  # this is not saved in a variable because it is not a dynamic/interactive widget
place = st.text_input("Place: ") # this is saved in a variable because it is a dynamic/interactive widget
days = st.slider("Forecast days", min_value=1, max_value=5,
                   help="Select the number of forecasted days")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

if place: # if place exists as a string/is provided
    # Get the temperature/sky data
    filtered_data = get_data(place, days)


    if option == "Temperature":
        dates = [dict["dt_txt"] for dict in filtered_data]
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"}) # plot a "LINE" graph
                        # x and y should be array type objects i.e. lists, tuples etc
                        # x and y should be the same length
                        # labels should be a dictionary
        st.plotly_chart(figure) # 

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        # Render images on the web app
        print(sky_conditions)
        st.image(image_paths, width=115)