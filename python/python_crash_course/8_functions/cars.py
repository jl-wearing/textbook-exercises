def make_car(manufacturer, model_name, **car_info):
    """Create a dictionary of information about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['name'] = model_name

    return car_info

def describe_car(car):
    """Display the information about a car."""
    for key, value in car.items():
        print(f"{key}: {value}")
    print()

#Testing the set of methods.
describe_car(make_car('bmw', 'x7', wheels='23 inch', tow_package=True, refridgerator=True))