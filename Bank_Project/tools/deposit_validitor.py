import re


def cash_validator(cash):
    if not (type(cash) == str and re.match(r"^[0-9]{1,50}$", cash)):
        raise ValueError("Invalid cash !!!")
    else:
        return cash
