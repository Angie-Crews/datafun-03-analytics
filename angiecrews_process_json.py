"""
Process a JSON file to review Average Temperature by Country
and save the results in both Celsius and Fahrenheit.
"""

#####################################
# Import Modules
#####################################

import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Global Variables
#####################################

FETCHED_DATA_DIR = "data"
PROCESSED_DIR = "processed"

INPUT_FILE = pathlib.Path(FETCHED_DATA_DIR, "avg_temp_by_country.json")
OUTPUT_FILE = pathlib.Path(PROCESSED_DIR, "avg_temp_by_country.txt")

#####################################
# Define Functions
#####################################

def countries_and_avg_temperatures(file_path: pathlib.Path) -> dict:
    """
    Returns a dictionary {Country: (avg_celsius, avg_fahrenheit)} from JSON file.
    """
    try:
        with file_path.open('r', encoding='utf-8') as f:
            json_data = json.load(f)

        results = {}

        for entry in json_data["data"]:
            country = entry["Country"]
            temps_c = []

            for key, value in entry.items():
                if key != "Country":
                    try:
                        temps_c.append(float(value))
                    except ValueError:
                        continue  # skip invalid/missing values

            if temps_c:
                avg_c = sum(temps_c) / len(temps_c)
                avg_f = avg_c * 9/5 + 32
                results[country] = (avg_c, avg_f)

        return results

    except Exception as e:
        logger.error(f"Error processing JSON: {e}")
        return {}

def save_results_to_text(results: dict, output_file: pathlib.Path):
    """
    Save processed average temperature results to a text file,
    showing both Celsius and Fahrenheit, sorted alphabetically by country.
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w', encoding='utf-8') as f:
        f.write("Average Surface Temperatures by Country\n")
        f.write("=======================================\n\n")
        f.write(f"{'Country':<35} {'Celsius':>8} {'Fahrenheit':>12}\n")
        f.write(f"{'-'*35} {'-'*8} {'-'*12}\n")
        
        for country, (avg_c, avg_f) in sorted(results.items()):
            f.write(f"{country:<35} {avg_c:>8.2f} {avg_f:>12.2f}\n")
    
    logger.info(f"Results saved to {output_file}")

def process_json_file():
    """Main function to process JSON file and save results."""
    logger.info("Starting JSON processing...")

    results = countries_and_avg_temperatures(INPUT_FILE)
    save_results_to_text(results, OUTPUT_FILE)

    logger.info("JSON processing complete.")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    process_json_file()