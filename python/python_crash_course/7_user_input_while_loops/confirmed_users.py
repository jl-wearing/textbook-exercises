#A for loop can be used to loop through a list, but the loop body
#should not modify the list in any way.
#To modify a list as you work through it, use a while loop

unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []

#Verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:        #while unconfirmed_users is not empty.
    current_user = unconfirmed_users.pop()

    print(f"Verifying user {current_user.title()}.")
    confirmed_users.append(current_user)
print()
confirmed_users.reverse()

#Display all confirmed users.
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print()