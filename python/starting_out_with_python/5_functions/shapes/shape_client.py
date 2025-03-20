import circle
import rectangle

prompt = "1) Area of a rectangle"
prompt += "\n2) Perimeter of a rectangle"
prompt += "\n3) Area of a circle"
prompt += "\n4) Circumference of a circle"
prompt += "\nq) Quit the program\n"

def menu(choice):
    while choice != 'q':
        match choice:
            case '1':
                length = float(input('Enter rectangle length: '))
                width = float(input('Enter rectangle width: '))
                area = rectangle.area(length, width)
                print(f"Area of rectangle: {area:.2f}.\n")
            case '2':
                length = float(input('Enter the length of the rectangle: '))
                width = float(input('Enter the width of the rectangle: '))
                perimeter = rectangle.perimeter(length, width)
                print(f"Perimeter of rectangle: {perimeter:.2f}.\n")
            case '3':
                radius = float(input('Enter the radius of the circle: '))
                area = circle.calculate_area(radius)
                print(f"Area of circle: {area:.2f}\n")
            case '4':
                radius = float(input('Enter the circumference of the circle: '))
                circumference = circle.calculate_circumference(radius)
                print(f"Circumference of circle: {circumference:.2f}.\n")
            case _:
                print("Invalid input entered.")

        choice = input(prompt)

def starting_screen():
    """Display what the program does."""
    print("\nEnter a choice of calculation to perform. These are the operations: ")
    choice = input(prompt)
    return choice

def main():
    """Mainline logic for the shape client program."""
    choice = starting_screen()
    menu(choice)

#Call the main function
main()