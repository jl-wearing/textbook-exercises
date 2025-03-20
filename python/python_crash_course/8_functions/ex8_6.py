#Write a function that takes the name of a city and its country.

def city_country(city, country):
    """Return information about a city and its country."""
    return f"{city.title()}, {country.title()}"

#Testing the function.
data = city_country('gaborone', 'botswana')
print(data)
data = city_country('santiago', 'chile')
print(data)
print(f"{city_country('cape town', 'south africa')}")