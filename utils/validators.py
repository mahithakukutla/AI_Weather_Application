def validate_city(value):
    city = value.strip()
    if not city:
        return None, "Please enter a city name."
    if len(city) > 100 or not all(c.isalpha() or c in " -.'" for c in city):
        return None, "Please enter a valid city name."
    return city, None