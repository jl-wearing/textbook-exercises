guest_list = ["Aron", "Nala", "Zoi"]
print(f"Hey {guest_list[0]}, I would like to invite you to dinner.")
print(f"Hi {guest_list[1]}, let's go for dinner.")
print(f"Mr. {guest_list[2]}, let's go eat.")

print()
unavailable = guest_list.pop()
print(f"Sorry everyone, {unavailable} couldn't make it. He has eaten.")

guest_list.insert(0, "Marley")
guest_list.insert(2, "Ziggy")
guest_list.append("Kiwi")
print(guest_list)

print()
print("Sorry, the dinner table will not arrive on time.")
print("I can only allow 2 people.")

remove1 = guest_list.pop()
remove2 = guest_list.pop()
remove3 = guest_list.pop()
message = f"Sorry to {remove1}, {remove2} and {remove3}, but I will have to uninvite you."
print(message)
print(guest_list)

print()
print(f"Thanks for coming {guest_list[0]} and {guest_list[1]}.")

del guest_list[1]
del guest_list[0]
print(guest_list)