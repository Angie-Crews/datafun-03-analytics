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

def books_of_bible(file_path: pathlib.Path) -> dict:
    """Count the number of books, chapters, and verses from a JSON file."""
    try:
        # Open the JSON file
        with file_path.open('r') as file:
            bible_data = json.load(file)

        # Initialize counters
        total_books = 0
        total_chapters = 0
        total_verses = 0

        # Get the list of books
        bible_list: list = bible_data.get("bible", [])

        # Process each book entry
        for book_entry in bible_list:
            total_books += 1
            # Convert string numbers like "1,533" into integers
            chapters = int(str(book_entry.get("chapters", "0")).replace(",", ""))
            verses = int(str(book_entry.get("verses", "0")).replace(",", ""))
            total_chapters += chapters
            total_verses += verses

        # Return dictionary of results
        return {
            "calculated_books": total_books,
            "calculated_chapters": total_chapters,
            "calculated_verses": total_verses,
            "expected_books": bible_data.get("total_books"),
            "expected_chapters": bible_data.get("total_chapters"),
            "expected_verses": bible_data.get("total_verses"),
            "message": bible_data.get("message", "no message")
        }

    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}  # return empty dict if error


def process_json_file():
    """Read a JSON file, count books, chapters, and verses, and save the result."""

    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "bible.json")
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_bible_chapter_verses.txt")

    # Call processing function
    bible_counts = books_of_bible(input_file)

    # Create output directory if it doesn’t exist
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Save results to file
    with output_file.open('w') as file:
        file.write("Bible Statistics:\n")
        for key, value in bible_counts.items():
            file.write(f"{key}: {value}\n")

    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")


#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")