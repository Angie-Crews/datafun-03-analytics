import pathlib
import sys
import requests
import pandas as pd  # Add this import

sys.path.append(str(pathlib.Path(__file__).resolve().parent))
from utils_logger import logger

FETCHED_DATA_DIR = "data"

def fetch_csv_and_convert_to_excel_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch CSV data from a URL, convert it to Excel format, and write it to a file.
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching CSV data from {url}...")
        response = requests.get(url)
        response.raise_for_status()

        # Convert CSV bytes to pandas DataFrame
        from io import StringIO
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)

        # Save DataFrame to Excel
        write_dataframe_to_excel(folder_name, filename, df)
        logger.info(f"SUCCESS: CSV file converted and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_dataframe_to_excel(folder_name: str, filename: str, df: pd.DataFrame) -> None:
    """
    Write a pandas DataFrame to an Excel file.
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing DataFrame to Excel at {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(file_path, index=False)  # Save as Excel
        logger.info(f"SUCCESS: DataFrame saved to {file_path}")
    except Exception as e:
        logger.error(f"Error writing DataFrame to Excel: {e}")

def main():
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/refs/heads/master/Billboard%201990.csv'
    logger.info("Starting CSV-to-Excel fetch demonstration...")
    fetch_csv_and_convert_to_excel_file(FETCHED_DATA_DIR, "Billboard 1990.xlsx", csv_url)

if __name__ == '__main__':
    main()
