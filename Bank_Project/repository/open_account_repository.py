import sqlite3



class OpenAccountRepository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./db/bank.sqlite")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS open_accounts (id INTEGER , name TEXT, password TEXT, cash_deposit REAL);""")
        self.connection.commit()


    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, bank):
        self.connect()
        self.cursor.execute("insert into open_accounts ( name, password, cash_deposit) values (?,?,?)",
                            [bank.name, bank.password, bank.cash_deposit])
        bank.id = self.cursor.lastrowid
        self.connection.commit()
        return bank

    # def update(self, bank):
    #     self.connect()
    #     self.cursor.execute("update banks set name=?,password=?, cash_deposit=? where id=?",
    #                         [open_account.name, open_account.password, open_account.cash_deposit, open_account.id])
    #     self.connection.commit()
    #     self.disconnect()
    #     return bank
    #
    # def delete(self, bank_id):
    #     self.connect()
    #     self.cursor.execute("delete from open_accounts where id=?",
    #                         [id])
    #     self.connection.commit()
    #     self.disconnect()
    #
    # def find_all(self):
    #     self.connect()
    #     self.cursor.execute("select * from banks")
    #     bank_list = [OpenAccount(*bank) for bank in self.cursor.fetchall()]
    #     self.disconnect()
    #     return bank_list
    #
    # def find_by_id(self, bank_id):
    #     self.connect()
    #     self.cursor.execute("select * from open_accounts where id=?", [id])
    #     bank = self.cursor.fetchone()
    #     self.disconnect()
    #     if bank:
    #         return OpenAccount(*open_account)
    #     return None
