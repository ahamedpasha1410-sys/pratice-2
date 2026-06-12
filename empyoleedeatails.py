class EmployeeIterator:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.employees):
            employee = self.employees[self.index]
            self.index += 1
            return employee
        raise StopIteration


employees = ["Pasha", "Ahmed", "Mohammed"]

company = ("Vi Technologies", "Hyderabad")

departments = {"IT", "HR", "Finance", "IT"}

salaries = {
    "Pasha": 50000,
    "Ahmed": 60000,
    "Mohammed": 55000
}

print("Company Details:")
print(company)

print("\nDepartments:")
for dept in departments:
    print(dept)

print("\nEmployee Salaries:")
for name, salary in salaries.items():
    print(name, ":", salary)

print("\nEmployees:")
iterator = EmployeeIterator(employees)

for employee in iterator:
    print(employee)
