import re


def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name)):
        raise ValueError("Invalid name !!!")
    else:
        return name

def password_validator(password):
    if not (type(password) == str and re.match(r"^[a-zA-Z\s0-9]{2,30}$", password)):
        raise ValueError("Invalid password !!!")
    else:
        return password


def cash_deposit_validator(cash_deposit):
    if not (type(cash_deposit) == str and re.match(r"^[0-9]{7,20}$", cash_deposit)):
        raise ValueError("Invalid cash_deposit !!!")
    else:
        return cash_deposit
