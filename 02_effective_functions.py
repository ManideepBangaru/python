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

# Functions can be stored in list -----------------------------------------------
funcs = [bark, str.lower, str.capitalize]
for f in funcs:
    print(f, f("hello!"))

# Functions can be passed on to other functions -----------------------------------------------
def greet(func):
    greeting = func("Hi, I'm Manideep")
    print(greeting)

greet(bark)

def whisper(text):
    return text.lower()

greet(whisper)

# using higher order functions ----------------------------------------------------------------
mapped_fun_ops = list(map(bark, ["Hello","Hey","I'm manideep"]))
print(mapped_fun_ops)

# functions can be nested ----------------------------------------------------------------
def speak(text):
    def whisper(t):
        return t.lower()
    return whisper(text)
print(speak("Hello, My name is Manideep !"))

# How to access inner functions ----------------------------------------------------
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func(volume=0.2))
print(get_speak_func(volume=0.7))

speak_func = get_speak_func(0.7)
op = speak_func("Hello !")
print(op)