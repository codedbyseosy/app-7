import requests
API_KEY = "b6630e943137a1f3dcaefe8f5e29cfa4"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}" # json data
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values] # extract the number of days we need
    return filtered_data

if __name__=="__main__": # only execute this when we are running this particular script directly and not importing it from anywhere else
   print(get_data(place="Tokyo", forecast_days=3))

