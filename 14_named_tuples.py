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