#Program to issue a receipt on goods purchased.

#Input.
number_of_goods = int(input('Enter the number of goods purchased: '))

#Process.
prices = []
sub_total = 0
for i in range(number_of_goods):
    price = float(input('Enter the price of each good: '))
    sub_total = sub_total + price

SALES_TAX = 0.07
total = sub_total + (sub_total * SALES_TAX)

#Output
print(f"\nSub Total: ${sub_total:5.2f}")
print(f"Sales Tax: {SALES_TAX * 100:<5.2f}%")
print(f"Total: \t${total:>7.2f}\n")