a = [1,2,3]
b = a

print(a)
print(b)
print(a==b)
print(a is b)

c = list(a)
print(c)

print(a==c) # a and c point to the same values
print(a is c) # a and c are different objects

"""
• An is expression evaluates to True if two variables point to the
same (identical) object.
• An== expression evaluates to True if the objects referred to by
the variables are equal (have the same contents)
"""