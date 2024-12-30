tup = ("hello", object(), 42)
print(tup)
print(tup[2])

tup[2] = 23
print(tup)
# This will raise an error because tuples are immutable