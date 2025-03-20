class User:
    """An attempt to model the user of a website."""

    def __init__(self, first_name, last_name, age, address):
        """A user is described by first and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.login_attempts = 0
        self.privileges = Privileges() #composition

    def describe_user(self):
        """Describe the information about a user."""
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name:  {self.last_name.title()}")
        print(f"Age:        {self.age}")
        print(f"Address:    {self.address}\n")

    def greet_user(self):
        """Display a simple greeting to a user."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {full_name.title()}, how are you today?\n")

    def increment_login_attempts(self):
        """Increment the login attempts by 1 each time a user fails to log in."""
        self.login_attempts+= 1

    def reset_login_attempts(self):
        """Reset the number of login attempts when a user successfully logs in."""
        self.login_attempts = 0

    def show_privileges(self):
        """Display the privileges of each user."""
        print(f"\nPrivileges of user: ")
        for privilege, set in self.privileges.privileges.items():
            print(f"- {privilege}: {set}")
        print()

#Creating a subclass of User.py
class Admin(User):
    """An administrator is a type of user with raised privileges."""

    def __init__(self, first_name, last_name, age, address):
        """
        Initialize the attributes of user.
        Then, initialize the attributes of admin.
        :param first_name: the first name of the administrator
        :param last_name: the last name of the administrator
        :param age: the age of the administrator
        :param address: the address of the administrator
        """
        super().__init__(first_name, last_name, age, address)
        self.privileges = Privileges(execute=True, delete=True, ban=True)


class Privileges:
    """The privileges each user has."""

    def __init__(self, read=True, write=True, execute=False, delete=False, ban=False):
        """The rights each user has on a website."""
        self.privileges = {
            "read": read,
            "write": write,
            "execute": execute,
            "delete": delete,
            "ban": ban
        }


#testing
admin = Admin('hacker', 'way', 35, '123 hacker way')
admin.show_privileges()

user_0 = User('Spider', 'Man', 20, 'new york')
user_0.show_privileges()