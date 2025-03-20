#You use python's for loop to traverse every element in a list.
magicians = ['david Blaine', 'houdini', 'dynamo']

for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I am looking forward to your next trick, {magician.title()}\n")
print("Thank you, everyone. That was a great magic show!")

print()