#Program to calculate potential profits made.

#Input
projected_sales = float(input('Enter the projected sales amount: '))

#Process
PROFIT_FACTOR = 0.23
profit = projected_sales * PROFIT_FACTOR

#Output
print(f"Projected Profits: ${profit:.2f}.\n")