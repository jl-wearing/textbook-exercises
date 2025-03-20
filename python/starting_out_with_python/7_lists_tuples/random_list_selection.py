#You can randomly select items from a list using the choices method.
import random

names = ['Jenny', 'Kelly', 'Chloe', 'Aubrey']
print(random.choice(names))
print(random.choices(names, k=2))