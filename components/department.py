FE_DEPARTMENT = 10
BE_DEPARTMENT = 11
ADMIN_DEPARTMENT = 12

POSITIONS = [
    {
      'department_id': FE_DEPARTMENT,
      'positions': [
          {'id' : '1_1', 'name' : 'JavaScript Developer' },
          {'id': '1_2', 'name' :  'React.js Developer'},
          {'id': '1_2', 'name' :  'FullStack Developer'}
        ]
    },

    {
        'department_id': BE_DEPARTMENT,
        'positions': [
            {'id': '2_1', 'name': 'Java Developer'},
            {'id': '2_2', 'name': 'PHP Developer'},
            {'id': '2_3', 'name': 'FullStack Developer'}
        ]
    },

    {
        'department_id': ADMIN_DEPARTMENT,
        'positions': [
            {'id': '1_1', 'name': 'HR'},
            {'id': '1_2', 'name': 'Manager'},
            {'id': '1_2', 'name': 'Operation Head'}
        ]
    },
]

DEPARTMENT_LISTS = [
    {'name' : 'Frontend', 'description' : 'it mostly handles frontend work', 'id': FE_DEPARTMENT, 'total_positions': 3},
    {'name': 'Backend', 'description': 'it mostly handles frontend work', 'id': BE_DEPARTMENT, 'total_positions': 3},
    {'name': 'Admin', 'description': 'it mostly handles admin work', 'id': ADMIN_DEPARTMENT, 'total_positions': 3}
]

class Department:
    def __init__(self):
        self.lists = DEPARTMENT_LISTS
        self.positions = POSITIONS

    def get_department_details(self, name):
        for department in self.lists:
            if department['name'] == name:
                return department
        return None

    def get_position_details(self, pos):
        for position in self.positions:
            if position['name'] == pos:
                return position
        return None

    def get_all_lists(self):
        return self.lists

    def get_positions(self, department_id):
        for position in self.positions:
            if position['department_id'] == department_id:
                return position['positions']
        return None






