from model.deposit import Deposit
from repository.deposit_repository import DepositRepository


class DepositController:
    deposit_repository = DepositRepository()
    @classmethod
    def deposit(cls, id, cash):
        try:
            bank = Deposit.Bank(None, cash)
            bank.validate()
            cls.deposit_repository.create_deposit(bank)
            return True, f"Deposit Successfully"
        except Exception as e:
            return False, f" Deposit Error: {e}"