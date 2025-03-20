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