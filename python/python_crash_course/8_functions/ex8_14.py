#Define a function to display information about a car.

def make_car(manufacturer, model_name, **car_info):
    """Display information about the car being ordered."""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

#Testing the function.
car1 = make_car('subaru', 'imprezza', color='blue', tow_package=True)
car2 = make_car('mercedes-benz', 'c63s', color='black',tyres=23, night_package=True)

#Output
print(car1)
print(car2)