# A null decorator --------------------------------------------------------
def null_decorator(func):
    return func

def greet():
    return 'Hello !'

greet = null_decorator(greet)
print(greet())

# it can also be used like below
@null_decorator
def greet():
    return 'Hello !!'
print(greet())

# A useful decorator --------------------------------------------------------
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet1():
    return 'Hello !!!'

print(greet1())

# Applying multiple decorators to a function ---------------------------------
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet2():
    return 'Hello !!!!!!'

print(greet2())