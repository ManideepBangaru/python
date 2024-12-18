def yell(text):
    return text.upper() + "!"

print(yell("hello"))

# Functions are objects
bark = yell
print(bark("woof"))

del yell

print(bark("hey"))
print(bark.__name__)
# print(yell("hello?"))

# Functions can be stored in list
funcs = [bark, str.lower, str.capitalize]
for f in funcs:
    print(f, f("hello!"))