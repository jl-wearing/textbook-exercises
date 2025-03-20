def get_formatted_city_country(city, country, population=None):
    """Return a neatly formatted city and country."""
    if population:
        formatted_name = f"{city}, {country} - population {population:,}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()