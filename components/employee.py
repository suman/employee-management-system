import storage
import json, random, uuid

STORAGE_FILE = 'storage.json'

class Employee:
    def __init__(self):
        self.name = None
        self.age = None
        self.salary = None
        self.position = None
        self.department = None
        self.id = None

    def add (self, name, age, salary, position, department):
        self.name = name
        self.age = age
        self.salary = salary

        self.position = position
        self.department =  department

        try:
            with open(STORAGE_FILE, "r") as f:
                employee_data = json.loads(f.read())
        except (json.JSONDecodeError, FileNotFoundError) as e:
            employee_data = {}  # fallback if file is missing or invalid
            print("Error:", e)

        # employee_data = json.loads(STORAGE_FILE)

        employee_id =  str(uuid.uuid4())

        while employee_id in employee_data:
            employee_id = random.randint(1, 100)
        self.id = employee_id
        temp_employee = {employee_id: self.__dict__}
        storage.save_data(temp_employee)

        return employee_id







