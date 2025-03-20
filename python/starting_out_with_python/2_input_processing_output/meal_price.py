#Program to calculate the price of a meal.

#Input
meal_price = float(input('Enter the price of the meal: '))

#Process
TAX = 0.07
TIP = 0.18
worker_tip = meal_price * TIP
tax_amount = meal_price * TAX
total_amount = meal_price + worker_tip + tax_amount

#Output
print(f"Sales Tax: ${tax_amount:.2f}.")
print(f"Worker Tip: ${worker_tip:.2f}.")
print(f"Total Amount: ${total_amount:.2f}.\n")