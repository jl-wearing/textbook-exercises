#Program to tally the sales for Markham.

def main():
    """Read sales from a program and display the total."""
    total = 0.0
    try:
        #Get the filename from the user.
        file_name = input('Enter the filename: ')

        #Open the file.
        infile = open(file_name, 'r')

        #accumulate the sales figures.
        for line in infile:
            total+= float(line)

        #Close the file.
        infile.close()
    except FileNotFoundError as file_error:
        print(file_error)
    except ValueError:
        print("Non-Numerical Data Found")
    except Exception as err:
        print(err)
    else:
        #Display the total.
        print(f"\nTotal Sales: ${total:.2f}")


#Call the main function.
if __name__ == '__main__':
    main()