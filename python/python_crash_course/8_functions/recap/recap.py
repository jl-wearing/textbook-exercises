#Recapping chapter 8 functions.

#Function definition.
def greet():
    """Display a simple greeting."""
    print("Hello\n")

#Testing the function.
for i in range(3):
    greet()

#Adding parameters.
def greet_user(username):
    """Display a greeting to a user."""
    print(f"Hello, {username.title()}\n")


#Testing the function.
for i in range(3):
    greet_user(input('Enter name: '))


def display_message():
    """Displays a message about what I am learning about."""
    print("Learning about defining functions in Python!\n")

def favorite_book(title):
    """Displays the name of my favorite book."""
    print(f"My favorite book is {title.title()}.\n")

#Testing the function.
display_message()
favorite_book('Python Crash Course')
favorite_book('big java')