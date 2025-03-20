"""A module that models an Employee object with a name, and annual salary."""

class Employee:
    """Creates an instance of an Employee."""
    def __init__(self, first_name, last_name, annual_salary):
        """
        Initialize the attributes of an employee.
        :param first_name: the first name of the employee.
        :param last_name: the last name of the employee.
        :param annual_salary: the annual salary of the employee.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000.00):
        """Gives an employee a raise."""
        if amount < 0:
            print("Cannot give a negative raise.")
            return
        else:
            self.annual_salary+= amount