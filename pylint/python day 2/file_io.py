"""
assignments on file input and output in python
"""

# Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age."
# Create a new CSV file called "adults.csv" with the rows of individuals who are 18 years or older.

import csv
import logging


INPUT_FILE = "data.csv"
OUTPUT_FILE = "adults.csv"

logging.basicConfig(filename="file_io.log", encoding="utf-8", level=logging.DEBUG)


try:
    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as infile, open(
        OUTPUT_FILE, "w", newline="", encoding="utf-8"
    ) as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if int(row["Age"]) >= 18:
                writer.writerow(row)

except FileNotFoundError as e:
    logging.error(e)


# Create a function search_log that takes a log file and a search keyword as input.
# The function should find and display all lines containing the search keyword.


def search_log(log_file, keyword):
    """
    search keyword in the given log file
    """
    try:
        with open(log_file, "r", encoding="utf-8") as file:
            for line in file:
                if keyword in line:
                    print(line)
    except FileNotFoundError as file_not_found_error:
        logging.error(file_not_found_error)


LOG_FILE = "test.log"
KEYWORD = "apple"
search_log(LOG_FILE, KEYWORD)
