import uuid

from components.employee import Employee

import storage
STORAGE_FILE = 'storage.json'

def format_message(messages):
    max_len = max(len(message) for message in messages.split("\n"))
    all_message = "+" + ('-' * max_len) +  "+\n"
    all_message += messages
    all_message += "\n++" + ('-' * max_len) +  "++\n"
    return all_message

def add_employee(employee_to_be_added):
    employee = Employee()
    employee_id = employee.add(**employee_to_be_added)
    return employee_id

def view_employee(employee_id):
    employee = storage.get_data(employee_id)
    return employee

def update_employee (employee_id, data):
    # employee = storage.get_data(employee_id)
    if data is None or len(data) == 0 or ('name' not in data and 'age' not in data):
        return None
    else:
        storage.save_data({employee_id: data})
        format_message("Employee data is updated successfully")
        return "success"

def delete_employee (employee_id):
     storage.remove(employee_id)

def get_department_summary(employee_id):
    employee = storage.get_data(employee_id)

    if employee_id == employee['id']:
        department_summary =  {'position': employee['position'], 'department': employee['department']}
        return department_summary
    return None

