# Project setup + file/module structure
# Implement Employee and Department classes
# Implement storage module (JSON read/write)
# CRUD operations in operations.py
# Build interactive menu (main.py)
# Test all features
# Polish code + comments + error handling
# Buffer/extra time
import storage
# Add Employee
# View Employees
# Update Employee
# Delete Employee
# Department Summary
# Exit
#

from operations import add_employee, update_employee, delete_employee, view_employee
from components.department import Department
department_instance = Department()


def get_department_from_user():
    all_departments = department_instance.get_all_lists()
    indexing_department = {}
    department_list_strings = ""

    for index, department in enumerate(all_departments):
        department_list_strings += f"{index + 1} {department['name']}\n"
        indexing_department[f"{index + 1}"] = department
    user_department_code = input(
        f"Please select your department by typing 1, 2, or 3: \n{department_list_strings.strip()}\n")

    return indexing_department[user_department_code]

def get_position_from_user(user_department):
    # Collect Position Information
    position_list_strings = ""
    department_positions = department_instance.get_positions(user_department['id'])

    indexing_position = {}

    for index, position in enumerate(department_positions):
        position_list_strings += f"{index + 1} {position['name']}\n"
        indexing_position[f"{index + 1}"] = position

    user_position_code = input(
        f"Please select your 'Position' for {user_department['name']} by typing 1, 2, or 3: \n{position_list_strings.strip()}\n")

    return indexing_position[user_position_code]

def collect_employee_information():
    user_name = input("Please enter your name: ")
    user_age = input("Please enter your age: ")
    user_department = get_department_from_user()
    user_position = get_position_from_user(user_department)
    user_salary = int(input(f"Please input your annual salary: "))
    employee_to_be_added = {'name': user_name, 'age': user_age, 'salary': user_salary, 'position': user_position,
                            'department': user_department}
    return add_employee(employee_to_be_added)

def format_employee_information(current_employee):
    employee_information = ""
    employee_information +=  f'Name: {current_employee['name']} \t|  Age: {current_employee["age"]} \n'
    employee_information += "------------------------\n"
    employee_information += f'Department: {current_employee['department']['name'] } \t|  Position: {current_employee['position']['name']} \n'
    print(employee_information)

def get_employee_id (emp_id):
    if emp_id is None or emp_id == "":
        emp_id = input("Please enter a valid employee ID: ")
    return emp_id

def ask_option_for_update(emp_obj):
    update_continue = True
    updated_employee_info = {}
    while update_continue:
        print("Please select the option you want to update.")
        user_update_action = int(input(
            "1. Name \n"
            "2. Age \n"
            "3. Department \n"
            "4. Position \n"
            "5. Exit\n"))
        if user_update_action == 1:
            user_name = input("Please update your name: ")
            updated_employee_info['name'] = user_name
        elif user_update_action == 2:
            user_age = input("Please update your age: ")
            updated_employee_info['user_age'] = user_age
        elif user_update_action == 3:
            user_department = get_department_from_user()
            updated_employee_info['department'] = user_department
        elif user_update_action == 4:
            user_position = get_position_from_user(emp_obj['department'])
            updated_employee_info['position'] = user_position
        elif user_update_action == 5:
            update_continue = False
    return updated_employee_info
continue_to_ask = True
print("Welcome to console-based Employee Management System!")
employee_id = None

ems_logo = """
+--------------------------------------+
|      Employee Management Service     |
+--------------------------------------+
"""
print(ems_logo)

while continue_to_ask:
    print("Enter any number between 1-5: to perform the action")
    print("---------------------------------------------------")
    user_action = int(input(
          "1. Add Employee\n"
          "2. View Employees\n"
          "3. Update Employee\n"
          "4. Delete Employee\n"
          "5. Department Summary\n"
          "6. Exit\n"))

    if user_action == 1:
        employee_id = collect_employee_information()
        if employee_id is None or employee_id == "":
            print("Please enter a valid employee ID.")
        else:
            print("-------------------------------------------------------")
            print("You have been successfully added to the employee list.")
            print("Your employee ID is " + employee_id )
            print("-------------------------------------------------------")
    elif user_action == 2:
        employee_id  = get_employee_id(employee_id)
        employee_details = view_employee(employee_id)
        if not employee_details is None or employee_details != "":
            format_employee_information(employee_details)
    elif user_action == 3:
        employee_id = get_employee_id(employee_id)
        employee_details = view_employee(employee_id)
        data = ask_option_for_update(employee_details)
        employee_details.update(data)
        update_employee(employee_id, employee_details)
    elif user_action == 4:
        employee_id  = get_employee_id(employee_id)
        delete_employee(employee_id)

    elif user_action == 5:
        pass
    elif user_action == 6:
        exit()