#Program to determine the price of each installment to purchase an item.

#Input
price = float(input('Enter the price of the product you wish to buy: '))
number_of_installments = int(input('Enter the number of installments you will ' \
                                   'take to purchase the product: '))

#Process
INTEREST = 0.05
total_amount = price + (price * INTEREST)
installment_price = total_amount / 5

#Output
print(f"\nTotal: ${total_amount:.2f}.")
print(f"{number_of_installments} installments, of price: ${installment_price:.2f}.")