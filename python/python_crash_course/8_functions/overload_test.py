#Testing to see if overloading works in python.

def greet_user():
    print("Hello!\n")


def greet_user(username):
    print(f"Hello {username.title()}\n")


greet_user()
greet_user("justin")

#Conclusion, overloading does not work.