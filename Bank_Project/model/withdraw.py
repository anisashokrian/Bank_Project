from tools.withdraw_validator import *


class Withdraw:
    class Bank:
        def __init__(self, customer_id, cash, password):
            self.customer_id = customer_id
            self.cash = cash
            self.password = password

        def validate(self):
            cash_validator(self.cash)
            password_validator(self.password)

        def __repr__(self):
            return f"{self.__dict__}"

        def to_tuple(self):
            return tuple((self.customer_id, self.cash, self.password))



