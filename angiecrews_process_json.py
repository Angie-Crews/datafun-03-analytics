"""
Process a JSON file to give information about Pensacola, Florida weather.

{
    "weather": {
        "current": {
            "temperature": 75,
            "wind_speed": 5,
            "humidity": 60
        },
        "hourly": [
            {
                "time": "2023-10-01T12:00:00Z",
                "temperature": 76,
                "wind_speed": 6,
                "humidity": 58
            },
            {
                "time": "2023-10-01T13:00:00Z",
                "temperature": 77,
                "wind_speed": 7,
                "humidity": 57
            }
        ]
    }
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "data"
PROCESSED_DIR: str = "processed"

#####################################
# Define Functions
#####################################

# TODO: Add or replace this with a function that reads and processes your JSON file

def process_json_file():
    """Read weather JSON, extract info, and save the result."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "pensacola_weather.json")
    output_file = pathlib.Path(PROCESSED_DIR, "json_pensacola_weather.txt")
    try:
        with input_file.open('r', encoding='utf-8') as file:
            data = json.load(file)
        current_weather = data.get("weather", {}).get("current", {})
        temperature = current_weather.get("temperature", "N/A")
        wind_speed = current_weather.get("wind_speed", "N/A")
        humidity = current_weather.get("humidity", "N/A")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w', encoding='utf-8') as file:
            file.write("Pensacola Weather - Current Conditions:\n")
            file.write(f"Temperature: {temperature}°F\n")
            file.write(f"Wind Speed: {wind_speed} mph\n")
            file.write(f"Humidity: {humidity}%\n")
        logger.info(f"Processed JSON file: {input_file}, weather info saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing JSON file: {e}")