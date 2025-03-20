#A function is a named block of code that performs an operation.
#Functions make code more modular and reusable.

#Simplest function.
def greet_user(username):           #Function definition
    """Display a simple greeting."""   #A docstring describes what the function does.
    print(f"Hello {username.title()}\n")

greet_user('justin')
greet_user('kiwi')

#docstrings describe what a function does.
#docstrings are placed immediately after the function definition.
#docstrings are enclosed in triple quotes and triple quotes let you write multiple lines.


# the variable username is called a parameter.
#A parameter is a piece of information a function needs to do its job.
# 'justin' is called an argument.
#An argument is a piece of information that's passed from a function call to a function.