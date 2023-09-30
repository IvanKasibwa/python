# Define an Employee class to represent individual employees
class Employee:
    # Initialize employee attributes (ID, name, salary) when an Employee object is created
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id   # Set the employee ID
        self.emp_name = emp_name   # Set the employee name
        self.emp_salary = emp_salary   # Set the employee salary

    # Display employee details
    def display_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: ${self.emp_salary:.2f}")
        print("------------------------")

# Define an HRDepartment class to manage employees
class HRDepartment:
    # Initialize the HR department with an empty list of employees
    def __init__(self):
        self.employees = []   # Create an empty list to store employees

    # Hire a new employee and add them to the list
    def hire_employee(self, emp_id, emp_name, emp_salary):
        new_employee = Employee(emp_id, emp_name, emp_salary)   # Create an Employee object
        self.employees.append(new_employee)   # Add the employee to the list
        print(f"{emp_name} has been hired!")

    # List all employees and their details
    def list_employees(self):
        if not self.employees:   # Check if the list is empty
            print("No employees in the HR department.")
        else:
            print("Employee Details:")
            for employee in self.employees:   # Iterate through the list of employees
                employee.display_employee_details()   # Display each employee's details

    # Fire an employee based on their ID
    def fire_employee(self, emp_id):
        for employee in self.employees:   # Iterate through the list of employees
            if employee.emp_id == emp_id:   # Check if the employee ID matches the provided ID
                self.employees.remove(employee)   # Remove the employee from the list
                print(f"Employee with ID {emp_id} has been fired.")
                break
        else:
            print(f"Employee with ID {emp_id} not found in the HR department.")

# Create an HR department object
hr = HRDepartment()

# Hire two employees
hr.hire_employee(1, "Ivan Kasibwa", 50000)
hr.hire_employee(2, "Matthew Janson", 60000)

# List all employees
hr.list_employees()

# Fire an employee by ID
hr.fire_employee(1)

# List employees after firing one
hr.list_employees()
