class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

myCar = Car('red', 37281)
print(myCar)
print(myCar.color, myCar.mileage)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f'a {self.color} car'

myCar = Car('red', 37281)
print(myCar)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'

myCar = Car('red', 37281)
print(myCar)

# inspecting an object in a Python inter-
# preter session simply prints the result of the object’s __repr__.