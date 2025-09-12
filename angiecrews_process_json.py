"""
Process a JSON file to Report current weather information for Pensacola, Florida and save the result.

JSON file is in the format where weather is a dictionary with keys "temperature", "humidity", and "description".

{
    "weather": {
        "temperature": 75,
        "humidity": 60,
        "description": "Partly cloudy"
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

# Replace with the names of your folders
FETCHED_DATA_DIR: str = "data"
PROCESSED_DIR: str = "processed"

#####################################
# Define Functions
#####################################

# This function reads and processes your JSON file

def get_weather_info(file_path: pathlib.Path) -> dict:
    """Extract weather information from a JSON file."""
    try:
        with file_path.open('r') as file:
            weather_data = json.load(file)
            return weather_data.get("weather", {})
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}


def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""

    # Replace with path to your JSON data file
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "weather_pensacola.json")

    # Replace with path to your JSON processed file
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_weather_pensacola.txt")
    
    # Call your new function to process YOUR JSON file
    # Create a new local variable to store the result of the function call
    weather_info = get_weather_info(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # Update the output to describe your results
        file.write("Current weather in Pensacola, Florida:\n")
        file.write(f"Temperature: {weather_info.get('temperature_2m', '')}°F\n")
        file.write(f"Wind Speed: {weather_info.get('wind_speed_10m', '')}%\n")
        file.write(f"Humidity: {weather_info.get('relative_humidity_2m', '')}\n")

    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")