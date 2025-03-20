#Program to determine the amount of money that accumulates through compound interest.
#A = P(1 + (r/n))**(n*t), where:
#A = amount of money in the account after the specified number of years.
#P = principal amount that was originally deposited into the account.
#r = annual interest rate.
#n = number of times per year the interest is compounded.
#t = specified number of years.

#Input
principal = float(input('Enter your starting balance: '))
interest_rate = float(input('Enter the interest rate: '))
number_of_compounds = int(input('Enter the number of times the interest compounds per year: '))
time = int(input('Enter how many years you want your principal to compound: '))

#Process
amount = principal * (1 + interest_rate / number_of_compounds)**(time * number_of_compounds)

#Output
print(f"\nAmount accrued: ${amount:.2f}.")