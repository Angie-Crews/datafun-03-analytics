"""
Process a text file to count occurrences of the words "Jo, Meg, Beth, Amy and Laurie" and save the result.
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

def process_text_file():
    """Read Little Women, count words, and save the result."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "little_women.txt")
    output_file = pathlib.Path(PROCESSED_DIR, "text_little_women_word_count.txt")
    try:
        with input_file.open('r', encoding='utf-8') as file:
            text = file.read()
        word_count = len(text.split())
        # Count specific words (case-insensitive)
        words_to_count = ['jo', 'meg', 'beth', 'amy', 'laurie']
        counts = {word: text.lower().count(word) for word in words_to_count}
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w', encoding='utf-8') as file:
            file.write(f"Little Women - Total word count: {word_count}\n")
            for word in words_to_count:
                file.write(f"Count of '{word}': {counts[word]}\n")
        logger.info(f"Processed text file: {input_file}, word counts saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing text file: {e}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")