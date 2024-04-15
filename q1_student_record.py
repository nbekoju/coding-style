"""
Create a Python program that manages student records. 
The program should have the following functionalities:
- Create a function that can add new students to the records with their 
student_id, name, age, and grade. The records should be saved to a "json" file 
and each time a new record is added, it should be saved to the same "json" file.
- Allow searching for a student by student_id or name. 
The data should return age and grade from the saved file.
- Allow updating a student's information by using student_id or name (age or grade).
"""

import json

FILE_NAME = "student_records.json"


class RecordNotFoundError(Exception):
    """custom exception class for record not found"""


def load_records():
    """
    load all the records from the json file

    Output:
        records: list of dictionary
    """
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        records = []

    return records


def write_data(records: list):
    """
    write whole data to the json file

    Parameters:
        records: list of dictionary
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def print_data():
    """
    load and print all the list fo records
    """
    records = load_records()
    print(records)


def add_student(data: dict):
    """
    add student to the json file

    Parameters:
        data: dictionary containg studnet information
    """
    existing_data = load_records()
    existing_data.append(data)
    write_data(existing_data)
    print("student record added successfully...")


def get_info_by_identifier(search_term):
    """
    search implementation by using the identifier (id or name)

    Parameters:
        search_term: 'integer' if id and 'string' if name
    """
    records = load_records()
    for record in records:
        if search_term in (record["id"], record["name"]):
            return {"age": record["age"], "grade": record["grade"]}

    raise RecordNotFoundError("Record Not Found")


def update_data(identifier, key: str, value):
    """
    update the data value based on the identifier
    only one key can be updated at a time

    Parameters:
        identifier: id(integer) or name(string)
        key: "age" or "grade"
        value: age(integer) or grade(float)
    """
    records = load_records()
    updated = False
    updated_record = None
    for record in records:
        if identifier in (record["id"], record["name"]):
            updated = True
            record[key] = value
            updated_record = record
            break
    if not updated:
        raise RecordNotFoundError("Record Not Found")

    write_data(records)
    return updated_record


if __name__ == "__main__":
    current_records = load_records()
    data_to_add = {"id": 5, "name": "ABCD", "age": 23, "grade": 3}
    add_student(data_to_add)
    search_result = get_info_by_identifier(5)
    print(search_result)
    updated_record = update_data(5, "grade", 100)
    print(updated_record)
