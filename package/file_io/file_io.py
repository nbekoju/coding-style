# Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of individuals who are 18 years or older.

import csv
import logging


input_file = "data.csv"
output_file = "adults.csv"

logging.basicConfig(filename='file_io.log', encoding='utf-8', level=logging.DEBUG)


try:
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if int(row["Age"]) >= 18:
                writer.writerow(row)

except FileNotFoundError as e:
    logging.error(e)

# Create a function add_to_json that takes a filename and a dictionary as input. The function should read the JSON data from the file, add the new dictionary to it, and write the updated data back to the same file.

# Sample Json: 
# [
#   {
#     "name": "Ram",
#     "age": 30
#   },
#   {
#     "name": "Sita",
#     "age": 25
#   }
# ]
            
import json

def add_to_json(filename, new_data):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    data.append(new_data)

    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

filename = "data.json"
new_dict = {"name" : "Shyam", "age" : 39}
add_to_json(filename, new_dict)

# Create a function search_log that takes a log file and a search keyword as input. The function should find and display all lines containing the search keyword.

def search_log(log_file, keyword):
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if keyword in line:
                    print(line)
    except FileNotFoundError as e:
        logging.error(e)

log_file = "test.log"
keyword = "apple"
search_log(log_file, keyword)