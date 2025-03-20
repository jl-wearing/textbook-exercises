#You can store functions in a file called a module and then
#import that module into your main program.

#An import statement tells python to make the code in a module
#available in the currently running program file.

#Storing your functions in a separate file allows you to hide
#the details of your program's code and focus on its higher level logic.

#It also allows you to reuse the functions in many different programs.

#Importing an entire module.
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

#To import all the functions in a module, import <module_name> at the top of your source code.

#You can also import specific functions from your module.
#Syntax: from module_name import function_0, function_1, ...
#We don't need to use the dot notation because we explicity imported the functions we wish to use.

#Using as to give a function an alias.
#If the name of a function you're importing conflicts with an existing name,
#or if the function name is too long, you can give it an alias with the as clause.
#Syntax: from module_name import function_name as alias_name

#You can also give a module an alias.
#Syntax: import module_name as md etc..

#Python allows you to import every function in a module using the asterisk (*) operator.
#The implication is that you don't need to use the dot operator, you can call functions directly.
#Syntax: from module_name import *