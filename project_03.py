import pathlib
from utils_logger import logger

datafun_03_analytics_path = pathlib.Path(__file__).parent.resolve()

def process_item(filename):
    logger.info(f"Processing item: {filename}")
    print(f"Processing file: {filename}")

def main():
    print(f"DataFun 03 Analytics path: {datafun_03_analytics_path}")
    logger.info("This is a log message from project_03.py")

    process_item("billboard 1990_count.txt")
    process_item("earthquake_magnitude.stats.txt")
    process_item("text_little_women_word_count.txt")
if __name__ == "__main__":
    main()
# This script sets up logging, defines a function to process items,
# and runs a main function that processes specific files.
# and runs a main function that processes specific files.
