#Program to determine the profit made by selling stock.

#Purchasing details.
number_of_shares_purchased = 2000
price_per_share = 40.00
commission_paid = number_of_shares_purchased * price_per_share * 0.03

#Selling details.
number_of_shares_sold = number_of_shares_purchased
price_when_sold = 42.75
commission_when_sold = number_of_shares_sold * price_when_sold * 0.03

#Display the amount Joe paid for the stock.
print(f"Amount Paid: ${number_of_shares_purchased * price_per_share:.2f}.")
#Display the commission when Joe paid for the stock.
print(f"Commission Paid: ${commission_paid:.2f}.")
#Display the amount Joe received when he sold.
print(f"Amount Received: ${number_of_shares_sold * price_when_sold:.2f}.")
#Display the commission when Joe sold.
print(f"Commission: ${commission_when_sold:.2f}.")

#Display the amount Joe had left.
profit_loss = ((number_of_shares_sold * price_when_sold) - commission_when_sold) - ((number_of_shares_purchased * price_per_share) - commission_paid)

if(profit_loss > 0):
    print(f"\nProfit: ${profit_loss:.2f}.")
else:
    print(f"\nLoss: ${profit_loss:.2f}.")