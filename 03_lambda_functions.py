# lambdas are single expression functions
add = lambda x,y : x + y
print(add(5,3))

# can also be written in the below format
print((lambda x,y : x*y)(5,3))

# To obtain even numbers
print([x for x in range(20) if x%2==0])