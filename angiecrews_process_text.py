"""
Process a text file to count occurrences of the word "Romeo" and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
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

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
       with open("little_women.txt", "r", encoding="utf-8-sig") as file:
            text: str = file.read()
            return text.lower().count(word.lower())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 1

def process_text_file():
    """Read a text file, count occurrences of 'Jo', 'Meg', 'Beth', and 'Amy', and save the result."""

    # Replace with path to your text data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "little_women.txt")

    # Replace with path to your text processed file
    output_file = pathlib.Path(PROCESSED_DIR, "text_little_women_word_count.txt")

    # Replace with the word you want to count from your text file

    # Make any necessary changes to the logic
    jo_count = count_word_occurrences(input_file, "Jo")
    meg_count = count_word_occurrences(input_file, "Meg")
    beth_count = count_word_occurrences(input_file, "Beth")
    amy_count = count_word_occurrences(input_file, "Amy")
    laurie_count = count_word_occurrences(input_file, "Laurie")

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Write the results to the output file
    with output_file.open('w') as file:
        # Update the output to describe your results
        file.write(f"Occurrences of 'Jo': {jo_count}\n")
        file.write(f"Occurrences of 'Meg': {meg_count}\n")
        file.write(f"Occurrences of 'Beth': {beth_count}\n")
        file.write(f"Occurrences of 'Amy': {amy_count}\n")
        file.write(f"Occurrences of 'Laurie': {laurie_count}\n")
    
    # Log the processing of the TEXT file
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")
