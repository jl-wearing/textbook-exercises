class User:
    """An attempt to model the user of a website."""

    def __init__(self, first_name, last_name, age, address):
        """A user is described by first and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.login_attempts = 0

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

#testing the implementation of the class and its methods.
#getters
user_0 = User('lionel', 'messi', 44, 'miami')
print(f"{user_0.first_name} {user_0.last_name} {user_0.age} {user_0.address}\n")

#testing the describe_user() method.
user_0.describe_user()

#testing the greet_user() method.
user_0.greet_user()

#testing the login methods.
goat = User('cristiano', 'ronaldo', 50, 'riyadh')
print(goat.login_attempts)
for i in range(10):
    goat.increment_login_attempts()
print(goat.login_attempts)
goat.reset_login_attempts()
print(goat.login_attempts)