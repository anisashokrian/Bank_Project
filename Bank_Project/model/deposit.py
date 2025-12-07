from tools.deposit_validitor import *


class Deposit:
    class Bank:
        def __init__(self, customer_id, cash):
            self.customer_id = customer_id
            self.cash = cash

        def validate(self):
            cash_validator(self.cash)

        def __repr__(self):
            return f"{self.__dict__}"

        def to_tuple(self):
            return tuple((self.customer_id, self.cash))



