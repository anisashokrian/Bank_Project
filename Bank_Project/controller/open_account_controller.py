from model.open_account import OpenAccount
from repository.open_account_repository import OpenAccountRepository



class OpenAccountController:
    open_account_repository = OpenAccountRepository()
    @classmethod
    def save(cls, id, name, password, cash_deposit):
        try:
            bank = OpenAccount.Bank(None, name, password, cash_deposit)
            bank.validate()
            cls.open_account_repository.save(bank)
            return True, f"Account Saved Successfully"
        except Exception as e:
            return False, f"Account Saved Error: {e}"