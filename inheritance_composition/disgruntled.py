# this one doesn't inherit from Employee
# but it creates an interface calculate_payroll
class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1000000

