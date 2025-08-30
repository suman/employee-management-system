from operations import add_employee, update_employee, delete_employee, view_employee, get_department_summary, format_message
from components.department import Department
department_instance = Department()

def get_department_from_user():
    all_departments = department_instance.get_all_lists()
    indexing_department = {}
    department_list_strings = ""

    for index, department in enumerate(all_departments):
        department_list_strings += f"{index + 1} {department['name']}\n"
        indexing_department[f"{index + 1}"] = department

    try:
        user_department_code = input(
        format_message(f"Please select your department by typing 1, 2, or 3: \n{department_list_strings.strip()}"))
        if user_department_code != '3'  and  user_department_code != '2' and user_department_code != '1':
            return None
    except:
        print(format_message("Please select your department by typing 1, 2, or 3: "))
        return None
    return indexing_department[user_department_code]

def get_position_from_user(user_department):
    # Collect Position Information
    position_list_strings = ""
    try:
        department_positions = department_instance.get_positions(user_department['id'])
    except:
        raise Exception(f"Something went wrong with department id, please check carefully.")
    indexing_position = {}

    for index, position in enumerate(department_positions):
        position_list_strings += f"{index + 1} {position['name']}\n"
        indexing_position[f"{index + 1}"] = position

    user_position_code = input(
        format_message(f"Please select your 'Position' for {user_department['name']} by typing 1, 2, or 3: \n{position_list_strings.strip()}"))


    return indexing_position[user_position_code]

def collect_employee_information():
    user_name = input("Please enter your name: ")
    user_age = input("Please enter your age: ")
    try:
        user_department = get_department_from_user()
        user_position = get_position_from_user(user_department)
    except IndexError:
        print(format_message("Please select your department by typing 1, 2, or 3: \n"))
        return None
    user_salary = int(input(f"Please input your annual salary: "))

    employee_to_be_added = {'name': user_name, 'age': user_age, 'salary': user_salary, 'position': user_position,
                            'department': user_department}
    return add_employee(employee_to_be_added)

def format_employee_information(current_employee):
    employee_information = f'Name: {current_employee['name']} \t|  Age: {current_employee["age"]} \n'
    employee_information += f'Department: {current_employee['department']['name'] } \t|  Position: {current_employee['position']['name']}'
    print(format_message(employee_information))

def get_employee_id (emp_id):
    if emp_id is None or emp_id == "":
        emp_id = input("Please enter a valid employee ID: ")
    return emp_id

def ask_option_for_update(emp_obj):
    update_continue = True
    updated_employee_info = {}
    while update_continue:
        update_message = "Please select the option you want to update.\n"
        update_message += "1. Name \n"
        update_message += "2. Age \n"
        update_message += "3. Department \n"
        update_message += "4. Position \n"
        update_message += "5. Exit"
        try:
            user_update_action = int(input(format_message(update_message)))
        except ValueError:
            continue

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

def  format_department_summary(info):
    summary = "EMS DEPARTMENT INFO\n"
    summary += f"Name: {info['department']['name']}\n"
    summary += f"total positions: {info['department']['total_positions']}\n"
    extracted_positions = [pos['name'] for position in department_instance.positions if info['department']['id'] == position['department_id'] for pos in position['positions']]
    extracted_positions = ", ".join(extracted_positions)
    summary += f"Position Name: {extracted_positions}"
    print(format_message(summary))
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
    action_msg  = "Enter any number between 1-6: to perform the action\n"
    action_msg +=  "1. Add Employee\n"
    action_msg += "2. View Employees\n"
    action_msg += "3. Update Employee\n"
    action_msg += "4. Delete Employee\n"
    action_msg += "5. Department Summary\n"
    action_msg += "6. Exit"

    try:
        user_action = int(input(format_message(action_msg)))
    except ValueError:
        print(format_message("Incorrect input, please try again."))
        continue

    if user_action == 1:
        try:
            employee_id = collect_employee_information()
        except ValueError:
            employee_id = None
            print(format_message(f"Incorrect input, please try again.\n{ValueError}"))
            continue
        if employee_id is None or employee_id == "":
            print(format_message("Please enter a valid employee ID."))
        else:
            employee_created_msg = "You have been successfully added to the employee list.\n"
            employee_created_msg += "Your employee ID is " + employee_id
            print(format_message(employee_created_msg))
    elif user_action == 2:
        employee_id  = get_employee_id(employee_id)
        employee_details = view_employee(employee_id)
        if not employee_details is None or employee_details != "":
            try:
                format_employee_information(employee_details)
            except Exception as e:
                employee_id = None
                print(format_message(f"Something went wrong, please try again.\n{e}"))
                continue
    elif user_action == 3:
        employee_id = get_employee_id(employee_id)
        employee_details = view_employee(employee_id)
        try:
            data = ask_option_for_update(employee_details)
        except Exception as e:
            employee_id = None
            print(format_message(f"Something went wrong, please try again.\n{e}"))
            continue
        employee_details.update(data)
        result = update_employee(employee_id, employee_details)
        if result is None:
            print(format_message("Something went wrong, please try again."))

    elif user_action == 4:
        employee_id  = get_employee_id(employee_id)
        delete_employee(employee_id)
    elif user_action == 5:
        employee_id = get_employee_id(employee_id)
        try:
            department_summary = get_department_summary(employee_id)
            format_department_summary(department_summary)
        except Exception as e:
            employee_id = None
            print(format_message(f"Something went wrong, please try again.\n{e}"))

    elif user_action == 6:
        exit()
