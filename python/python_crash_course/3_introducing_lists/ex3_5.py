guest_list = ['Mom', 'Dad', 'Shaun', 'Nigel']
print(f"Hey {guest_list[1]}, I would like to invite you to dinner.")
print(f"Hi {guest_list[0]}, let's go for dinner.")
print(f"Mr. {guest_list[2]}, let's go eat.")
print(f"{guest_list[-1]}, let's go eat tonight.")

print()
unavailable = guest_list.pop()
print(f"Sorry everyone, {unavailable} couldn't make it. He has class.")
guest_list.append("Harold")
print(f"Uncle {guest_list[-1]} will show up instead.")