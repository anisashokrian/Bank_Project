from tools.open_account_validator  import *


class OpenAccount:
    class Bank:
        def __init__(self, id=None, name="", password="", cash_deposit=0):
            self.id = id
            self.name = name
            self.password = password
            self.cash_deposit = cash_deposit

        def validate(self):
            name_validator(self.name)
            password_validator(self.password)
            cash_deposit_validator(self.cash_deposit)

        def __repr__(self):
            return f"{self.__dict__}"

        def to_tuple(self):
            return (self.id, self.name, self.password, self.cash_deposit)



