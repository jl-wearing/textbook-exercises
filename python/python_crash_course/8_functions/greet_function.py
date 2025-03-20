#A function is defined using the def keyword.
#Any indented lines following a function definition make up the body of the function.
#The first line of a function body is called a docstring, and it describes what the function does.
#A function call tells Python to execute the code in the function body.

def greet():
    """Display a simple greeting."""
    print("Hello!")

#Passing information to a function/
def greet_user(username):
    """Display a personalized greeting."""
    print(f"Hello, {username}")


#Testing the greet() function.
greet()
print()

#Testing the greet_user() function.
greet_user('messi')
greet_user('ronaldo')
print()