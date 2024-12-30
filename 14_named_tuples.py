tup = ("hello", object(), 42)
print(tup)
print(tup[2])

# tup[2] = 23
# print(tup)
# This will raise an error because tuples are immutable

# Named tuples are a subclass of tuples that have named fields which can be accessed using dot notation
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

my_car = Car("red", 3812.4) # Creating a new instance of the Car class
print(my_car.color) # Accessing the fields using dot notation
print(my_car.mileage) # Accessing the fields using dot notation
print(my_car[0]) # Accessing the color field using index

# Subclassing named tuples --------------------------------------------------
Car = namedtuple('Car', 'color mileage')

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red', 1234)
print(c.hexcolor())

Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))

ev = ElectricCar('red', 1234, 45.0)
print(ev.charge)

#  Built-in helper methods --------------------------------------------------
print(my_car._asdict())

import json
json_op = json.dumps(my_car._asdict())
print(json_op)

my_car._replace(color='blue')
print(my_car)