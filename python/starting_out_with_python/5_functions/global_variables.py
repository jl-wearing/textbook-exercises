#Creating global variables.
number = 0
def global_number():
    global number
    number = 5
    print(number)

global_number()
print(number)