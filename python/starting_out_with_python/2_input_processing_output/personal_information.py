#Program to display information about myself.
user = {
    "name": "justin",
    "address": "gaborone, botswana",
    "telephone": "74137333",
    "major": "computer science",
}

for key, value in user.items():
    print(f"{key.title()}: {value.title()}")