def validate(name):
    if len(name) < 10:
        raise ValueError("Name is too short")

# validate("John")

# --------------------------------------------------------
# class NameTooShortError(ValueError):
#     pass

# def validate(name):
#     if len(name) < 10:
#         raise NameTooShortError(name)

# validate("Jane")

# --------------------------------------------------------
def validate(name):
    if len(name) < 10:
        raise ValueError("Name is too short")
    elif len(name) > 20:
        raise NameTooLongError(name)
    else:
        print("Name is fine")

class BaseValidationError(ValueError):
    pass
class NameTooShortError(BaseValidationError):
    pass
class NameTooLongError(BaseValidationError):
    pass
class NameTooCuteError(BaseValidationError):
    pass

try:
    name = "John wick jhkjahfkewaifhweihfiewhfoih"
    validate(name)
except NameTooLongError as err:
    validate(name[:10])