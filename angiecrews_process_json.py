"""
Process a JSON file to review Average Temperature by Country and save the result.

JSON file is in the format where "index" is a list of dictionaries with keys "time" and "value".
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys
import requests

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

country_name = "Enter Country Name Here"

# Add or replace this with a function that reads and processes your JSON file
def avg_temp_by_country(file_path: pathlib.Path) -> dict:
    """Read average temperature by country from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:
            data = json.load(file)
            # Process the data to calculate average temperature by country
            avg_temps = {}
            for entry in data.get("index", []):
                country = entry.get("country")
                temp = entry.get("value")
                if country and temp is not None:
                    avg_temps[country] = avg_temps.get(country, []) + [temp]
            # Calculate the average for each country
            for country, temps in avg_temps.items():
                avg_temps[country] = sum(temps) / len(temps) if temps else 0
            return avg_temps
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}  # return an empty dictionary in case of error


def process_json_file():
    """Read a JSON file, average temperatures by country, and save the result."""

    # Replace with path to your JSON data file
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "avg_temp_by_country.json")

    # Replace with path to your JSON processed file
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_avg_temp_by_country.txt")

    # Call your new function to process YOUR JSON file
    # Create a new local variable to store the result of the function call
    avg_temps = avg_temp_by_country(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # Write the average temperature by country results
        file.write("Average Temperature by Country:\n")
        for country, avg_temp in avg_temps.items():
            file.write(f"{country}: {avg_temp}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")