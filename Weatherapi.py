import requests
import json

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        return data

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return None


# Example usage
city = "London"
api_key = "your_api_key"

weather_data = get_weather(city, api_key)
if weather_data:
    print(weather_data)
else:
    print("Failed to retrieve weather data.")
