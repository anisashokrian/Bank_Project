import re


def cash_validator(cash):
    if not (type(cash) == str and re.match(r"^[0-9]{7,20}$", cash)):
        raise ValueError("Invalid cash !!!")
    else:
        return cash



def password_validator(password):
    if not (type(password) == str and re.match(r"^[a-zA-Z\s][0-9]{2,30}$", password)):
        raise ValueError("Invalid password !!!")
    else:
        return password