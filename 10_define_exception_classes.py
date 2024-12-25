# def validate(name):
#     if len(name) < 10:
#         raise ValueError("Name is too short")

# validate("John")

# --------------------------------------------------------

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)

validate("Jane")