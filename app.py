from flask import Flask, render_template, request
import requests
import os
from datetime import datetime

app = Flask(__name__)

# Weatherbit API configuration
WEATHERBIT_API_KEY = "3ba981a286874fc69522361ee6afe280"
BASE_URL = "https://api.weatherbit.io/v2.0/current"


def get_weather_data(city):
    # Format city for US locations (assuming US location, add country code for international)
    location = f"{city},US"

    params = {
        "city": location,
        "key": WEATHERBIT_API_KEY,
        "units": "M"  # Metric units
    }

    try:
        response = requests.get(BASE_URL, params=params)

        # Print the actual URL being called (for debugging)
        print(f"Requesting URL: {response.url}")

        # More detailed error handling
        if response.status_code == 403:
            return None, "API key validation failed. Please check your API key."
        elif response.status_code == 404:
            return None, f"City '{city}' not found. Please check the city name."
        elif response.status_code != 200:
            return None, f"API Error: Status code {response.status_code}"

        response.raise_for_status()
        data = response.json()

        # Add response data debugging
        print(f"API Response: {data}")

        # Check if we got any data
        if not data.get("data") or len(data["data"]) == 0:
            return None, "No weather data found for this location."

        current = data["data"][0]

        weather_info = {
            "city": current["city_name"],
            "country": current["country_code"],
            "temperature": current["temp"],
            "feels_like": current["app_temp"],
            "humidity": current["rh"],
            "wind_speed": round(current["wind_spd"], 1),
            "description": current["weather"]["description"],
            "icon": current["weather"]["icon"],
            "uv": round(current["uv"], 1),
            "aqi": current.get("aqi", "N/A"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather_info, None

    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {str(e)}")
        return None, f"Error connecting to weather service: {str(e)}"
    except KeyError as e:
        print(f"Parsing Error: {str(e)}")
        return None, f"Error parsing weather data: {str(e)}"
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return None, f"An unexpected error occurred: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather_data, error = get_weather_data(city)

    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
    ##########