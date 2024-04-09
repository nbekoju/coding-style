# Create a Python program that manages student records. The program should have the following functionalities:

## Create a function that can add new students to the records with their student_id, name, age, and grade. The records should be saved to “json” file and each time new record is added, it should be saved to same “json” file

## Allow searching for a student by student_id or name. The data should return age and grade from the saved file.

##Allow updating a student's information by using student_id or name(age or grade)

import json

file_name = "student_records.json"


def load_records():
    """
    load all the records from the json file

    Output:
        records: list of dictionary
    """
    try:
        with open(file_name, "r") as file:
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
    with open(file_name, "w") as file:
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
        if record["id"] == search_term or record["name"] == search_term:
            return {"age": record["age"], "grade": record["grade"]}

    raise Exception("Student Record Not Found")


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
    for record in records:
        if record["id"] == identifier or record["name"] == identifier:
            updated = True
            record[key] = value
            break
    if updated:
        write_data(records)
        return record

    if not updated:
        raise Exception("Student Record Not Found")


if __name__ == "__main__":
    records = load_records()
    data = {"id": 5, "name": "ABCD", "age": 23, "grade": 3}
    add_student(data)
    search_result = get_info_by_identifier(5)
    print(search_result)
    updated_record = update_data(5, "grade", 100)
    print(updated_record)
