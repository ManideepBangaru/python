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

# Decorators that accept arguments ---------------------------------
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# example
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
        f'with {args}, {kwargs}')
        original_result= func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
        f'returned {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name} : {line}'

print(say("Manideep", "Hello Decorators !"))

# Writing debuggable decorators ---------------------------------
def greet():
    """
    Returns a friendly greeting.
    """
    return 'Hello !'

decorated_greet = uppercase(greet)

print(greet.__name__)
print(greet.__doc__)
print(decorated_greet.__name__)
print(decorated_greet.__doc__)

# to copy lost metadata to the decorator
import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def sayHello():
    """
    Says Hello ...
    """
    return 'Hellooooooooo'

print(sayHello.__name__)
print(sayHello.__doc__)
decorated_sayHello = uppercase(sayHello)
print(decorated_sayHello.__name__)
print(decorated_sayHello.__doc__)
print(sayHello())