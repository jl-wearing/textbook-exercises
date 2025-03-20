#Program to determine the present value required to grow an account
#to a certain size.

#Input
future_value = float(input('Enter your desired future value: '))
years = float(input('Enter the number of years you want to accrue your money: '))
interest_rate = float(input('Enter the interest rate: '))

#Process
present_value = future_value / ((1.0 + (interest_rate/100.0))**years)

#Output
print(f"Present value required to grow your account to " \
      f"${future_value:.2f} in {years} years: ${present_value:.2f}.\n")