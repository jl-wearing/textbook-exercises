rivers = {
    'ganges': 'india',
    'shashe': 'botswana',
    'thames': 'great britain',
    'orange': 'lesotho',
    'zambezi': 'zambia', 
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print()

for river in rivers.keys():
    print(river.title())
print()

for country in rivers.values():
    print(country.title())
print()