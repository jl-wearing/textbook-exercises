"""Module to display the steps to disassemble a dryer."""

def startup_message():
    """Message to display what the program does."""
    print("This program tells you how to disassemble a dryer.")
    print("There are 4 steps in the process.\n")

def step_1():
    """Message to display the first step in the disassembly process."""
    print("Step 1: Unplug the dryer & move it away from the wall.\n")

def step_2():
    """Message to display the second step in the process."""
    print("Step 2: Remove the 6 screws from the back of the dryer.\n")

def step_3():
    """Display the third step in the disassembly process."""
    print("Step 3: Remove the back panel from the dryer.\n")

def step_4():
    """Display the fourth step in the disassembly process."""
    print("Step 4: Pull the top of the dryer straight up.\n")

def main():
    startup_message()
    input("Press enter to see step 1: ")
    step_1()
    input("Press enter to see step 2: ")
    step_2()
    input("Press enter to see step 3: ")
    step_3()
    input("Press enter to see step 4: ")
    step_4()

main()