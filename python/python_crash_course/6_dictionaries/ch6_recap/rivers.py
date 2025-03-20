rivers = {
    'shashe': 'botswana',
    'nile': 'egypt',
    'zambezi': 'zambia',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print()

print("The rivers include: ")
for river in rivers.keys():
    print(river.title())
print()

print("The countries include: ")
for country in rivers.values():
    print(country.title())
print()