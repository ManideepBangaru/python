"""
Class variables are declared inside the class definition (but outside
of any instance methods). They’re not tied to any particular instance
of a class. Instead, class variables store their contents on the class
itself, and all objects created from a particular class share access to the
same set of class variables. This means, for example, that modifying
a class variable affects all object instances at the same time.

Instance variables are always tied to a particular object instance.
Their contents are not stored on the class, but on each individual ob-
ject created from the class. Therefore, the contents of an instance vari-
able are completely independent from one object instance to the next.
And so, modifying an instance variable only affects one object instance
at a time.
"""

class Dog:
    num_legs = 4 # Class variable

    def __init__(self, name):
        self.name = name # Instance variable

jack = Dog("Jack")
jill = Dog("Jill")
print(jack.name, jill.name)
print(jack.num_legs, jill.num_legs)

# print(Dog.name) # This will raise an error because name is an instance variable

# Accessing class variables --------------------------------------------------
Dog.num_legs = 6
print(jack.num_legs, jill.num_legs)

Dog.num_legs = 4
jack.num_legs = 6
print(jack.num_legs, jill.num_legs, Dog.num_legs)

print(jack.num_legs, jack.__class__.num_legs)