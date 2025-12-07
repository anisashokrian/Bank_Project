from model.withdraw import Withdraw
from repository.withdraw_repository import WithdrawRepository


class WithdrawController:
    withdraw_repository = WithdrawRepository()
    @classmethod
    def withdraw(cls, id, cash, password):
        try:
            bank = Withdraw.Bank(None, cash, password)
            bank.validate()
            cls.withdraw_repository.withdraw(bank)
            return True, f"Withdraw Successfully"
        except Exception as e:
            return False, f"Withdraw Error: {e}"

