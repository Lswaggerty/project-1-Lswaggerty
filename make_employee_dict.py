# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/6/2024
# Description: Create a function that has private data members for an employee's and displays that data
class Employee:
    """Represent an employee with name, ID number, salary, and email address."""

    def __init__(self, name, ID_number, salary, email_address):
        """Initialize the employee's data members."""
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """Return the name of the employee."""
        return self._name

    def get_ID_number(self):
        """Return the ID number of the employee."""
        return self._ID_number

    def get_salary(self):
        """Return the salary of the employee."""
        return self._salary

    def get_email_address(self):
        """Return the email address of the employee."""
        return self._email_address


def make_employee_dict(names, ids, salaries, emails):
    """Return a dictionary of Employee objects keyed by their ID numbers."""
    employee_dict = {}
    for name, ID, salary, email in zip(names, ids, salaries, emails):
        employee = Employee(name, ID, salary, email)
        employee_dict[ID] = employee
    return employee_dict
