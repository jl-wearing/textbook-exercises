#Program to get sales values, store them and display them.

#Constants used by the program.
SALES_DAYS = 5

def main():
    """Simple program to display sales stored in a list."""
    #Create a list to hold the sales for each day.
    sales = [0.0] * SALES_DAYS

    #Get each day's sales amount from the user.
    for index in range(len(sales)):
        sale_amount = float(input(f"Enter sales for day #{index + 1}: "))

        #add the sale amount to the list.
        sales[index] = sale_amount

    #Display the sales amounts.
    for sale in sales:
        print(f"${sale:.2f}")

#Call the main function.
if __name__ == '__main__':
    main()