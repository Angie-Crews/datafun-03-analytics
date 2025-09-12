"""
Process a JSON file to count books chapters and verses of the Bible.
JSON file is in the format where books is a list of dictionaries with keys "name", "chapters", and "verses".

{
    "Bible": [
        {
            "books": "Genesis",
            "chapters": 50,
            "verses": 1533
        },
        {
            "books": "Exodus",
            "chapters": 40,
            "verses": 1213
        }
    ],
    "number": 2,
    "message": "success"
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

def count_books_chapters_verses(file_path: pathlib.Path) -> dict:
    """Count the number of chapters and verses in each book from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:

            # Use the json module load() function 
            # to read data file into a Python dictionary
            data = json.load(file)  

            # initialize an empty dictionary to store the counts
            book_counts = {}

            # books is a list of dictionaries in the JSON file
            books_list: list = data.get("books", [])

            # For each book in the list, get the name, chapters, and verses
            for book_dict in books_list:  
                name = book_dict.get("books", "Unknown")
                chapters = book_dict.get("chapters", 0)
                verses = book_dict.get("verses", 0)
                book_counts[name] = {"chapters": chapters, "verses": verses}

            # Return the dictionary with counts of chapters and verses by book    
            return book_counts
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {} # return an empty dictionary in case of error

    """Read a JSON file, count books chapters and verses of the Bible, and save the result."""

def process_json_file():
    """Read a JSON file, count chapters and verses by book, and save the result."""

    # Replace with path to your JSON data file
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "bible_books.json")

    # Replace with path to your JSON processed file
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_books_chapters_verses.txt")
    
    # Call the function to process your JSON file
    book_counts = count_books_chapters_verses(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        file.write("Books, Chapters, and Verses:\n")
        for book, counts in book_counts.items():
            file.write(f"{book}: Chapters={counts['chapters']}, Verses={counts['verses']}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")