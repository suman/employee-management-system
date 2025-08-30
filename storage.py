import json

STORAGE_FILE = 'storage.json'

def load_json_file (file_name):
    try:
        with open(file_name, 'r+') as file:
            file_data = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, start with an empty list
        file_data = {}
    except json.JSONDecodeError:
        # Handle the case where the file is empty or contains invalid JSON
        file_data = {}
    return file_data

def save_data(data):
    file_data = load_json_file(STORAGE_FILE)
    file_data.update(data)
    try:
        with open(STORAGE_FILE, 'w') as storage_file:
            json.dump(file_data, storage_file)
    except FileNotFoundError:
        print("some error ")

def get_data(employee_id):
    employee_data = load_json_file(STORAGE_FILE)
    if employee_id in employee_data:
        return employee_data[employee_id]
    return None

def remove(employee_id):
    employee_data = load_json_file(STORAGE_FILE)
    if employee_id in employee_data:
        del employee_data[employee_id]
        try:
            with open(STORAGE_FILE, 'w') as storage_file:
                json.dump(employee_data, storage_file)
                print(f"Employee {employee_id} has been removed")
        except FileNotFoundError:
            print("some error ")
    else:
        print("employee ID not found")


