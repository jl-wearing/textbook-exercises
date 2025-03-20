def get_monthly_sales():
    """Prompt the salesperson for their monthly sales figures."""
    while True:
        try:
            monthly_sales = float(input("Enter your monthly sales figures: "))
            break
        except ValueError:
            print("Please enter valid financial figures.")

    return monthly_sales

def get_advanced_pay():
    """Get the amount of advanced pay a salesperson got, if any."""
    while True:
        try:
            advanced_pay = float(input("Enter the amount of advanced pay received: "))
            break
        except ValueError:
            print("Please enter valid financial figures.")
    return advanced_pay

def calculate_commission_rate(monthly_sales):
    """Calculate the commission of a salesperson based on monthly sales."""
    if monthly_sales < 10_000:
        commission_rate = 0.1
    elif 10_000 <= monthly_sales < 14_999:
        commission_rate = 0.12
    elif 15_000 <= monthly_sales < 17_999:
        commission_rate = 0.14
    elif 18_000 <= monthly_sales < 21_999:
        commission_rate = 0.16
    else:
        commission_rate = 0.18
    return commission_rate

def calculate_pay(monthly_sales, advanced_pay, commission_rate):
    """Calculate a sales person's pay."""
    pay = monthly_sales * commission_rate - advanced_pay
    return pay

def main():
    """Mainline logic for the sales commission program."""
    #Get the monthly sales of an employee.
    monthly_sales = get_monthly_sales()

    #Calculate the commission rate of the employee.
    commission_rate = calculate_commission_rate(monthly_sales)

    #Calculate the advanced pay of an employee.
    advanced_pay = get_advanced_pay()

    #Calculate the overall pay of an employee.
    pay = calculate_pay(monthly_sales, advanced_pay, commission_rate)

    if pay < 0:
        print(f"You owe your boss ${pay:.2f}.\n")
    else:
        print(f"Monthly Pay: ${pay:.2f}.\n")

#Call the main function.
main()