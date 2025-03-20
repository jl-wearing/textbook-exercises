#Program to calculate the total of sales figures from a file.

def calculate_total(file_path):
    """Calculate the sum of sales figures in the file."""
    #Open the file for reading.
    while True:
        try:
            my_file = open(rf"{file_path}", "r")
            break
        except FileNotFoundError:
            print("File not found!")

    #Process the sales figures.
    total = 0
    while True:
        data = my_file.readline()

        #Reached the end of the file.
        if data == '':
            break

        #Add data to total.
        total+= float(data)

    return total

def main():
    """Mainline logic for sales figures calculation."""
    file_path = "files/sales.txt"

    #Get the sum of the sales figures.
    total = calculate_total(file_path)

    #Output
    print(f"\nTotal: ${total:.2f}.")

#Call the main function.
if __name__ == '__main__':
    main()