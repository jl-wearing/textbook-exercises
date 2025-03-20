#Program to display the name of a city and country, neatly formatted.

def city_country(country, city):
    """Display a country a city, neatly formatted."""
    return f"{city.title()}, {country.title()}"

#Testing the city_country() function.
gabs = city_country('botswana', 'gaborone')
print(gabs)

