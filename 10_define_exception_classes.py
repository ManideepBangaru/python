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
    if len(name) > 20:
        raise NameTooLongError(name)

class BaseValidationError(ValueError):
    pass
class NameTooShortError(BaseValidationError):
    pass
class NameTooLongError(BaseValidationError):
    pass
class NameTooCuteError(BaseValidationError):
    pass

try:
    validate("John wick")
except BaseValidationError as err:
    handle_validation_error(err)