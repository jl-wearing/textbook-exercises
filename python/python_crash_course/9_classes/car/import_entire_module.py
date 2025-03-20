import car
import electric_car

bmw = car.Car('bmw', 'x5', 2008)
tesla = electric_car.ElectricCar('tesla', 'model x', 2025, 100)

print(bmw.get_descriptive_name())
print(tesla.get_descriptive_name())