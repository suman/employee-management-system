import uuid

from components.employee import Employee

import storage
STORAGE_FILE = 'storage.json'

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
        return "No data"
    else:
        storage.save_data({employee_id: data})
        print("updated data successfully")
        return "success"

def delete_employee (employee_id):
     storage.remove(employee_id)

def get_department_summary(employee_id):
    employee = storage.get_data(employee_id)

    if employee_id == employee['id']:
        department_summary =  {'position': employee['position'], 'department': employee['department']}
        return department_summary
    return None