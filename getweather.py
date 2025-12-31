import os
import sys
import requests
import time
from datetime import datetime

# Check if arguments are provided
if len(sys.argv) > 1:
    API_KEY = sys.argv[1]  # Get the first argument
else:
    print("You need to pass the API key. Exiting")
    sys.exit()

BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"
# params = "lat=43.70011&lon=-79.4163&appid=5f481f43b38bc213363c1589e9140487"
params = "lat=43.70011&lon=-79.4163&appid=" + str(API_KEY)

# https://api.openweathermap.org/data/3.0/onecall?lat=43.70011&lon=-79.4163&appid=5f481f43b38bc213363c1589e9140487

try:
	response = requests.get(BASE_URL, params=params, timeout=10)
	response.raise_for_status()
	data = response.json()
except requests.RequestException as e:
	print(f"Network or request error: {e}")

if response.status_code == 200:
    name = data["timezone"].split("/",1)[1]
    offset = int(data["timezone_offset"]/(60*60))
    sunrise = data["current"]["sunrise"]
    srh = str(int(time.strftime("%H", time.gmtime(sunrise))) + offset)
    srm = time.strftime("%M", time.gmtime(sunrise))
    sunset = data["current"]["sunset"]
    ssh = str(int(time.strftime("%H", time.gmtime(sunset))) + offset)
    ssm = time.strftime("%M", time.gmtime(sunset))
    temp = int(data["current"]["temp"] - 273.15)
    feels_like = int(data["current"]["feels_like"] - 273.15)
    latest_summary = len(data["daily"]) - 1
    summary = data["daily"][latest_summary]["summary"]
	
    the_weather = "The temperature is currently " + str(temp) + ". It feels like " + str(feels_like) + "." 
    the_weather = the_weather + " " + summary + ". " 
    the_weather = the_weather + "Sunrise time " + srh + ":" + srm + " and "
    the_weather = the_weather + "Sunset time " + ssh + ":" + ssm

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print("This is the weather as of ", current_time)

    print ("This is the weather as of", current_time, "...", the_weather)
	
else:
	print(f"Error from API: {data.get('message', 'Unknown error')}")

