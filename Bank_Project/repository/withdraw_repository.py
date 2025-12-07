import sqlite3

from model import withdraw
from model.withdraw import Withdraw


class WithdrawRepository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./db/bank.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def withdraw(self, bank):
        self.connect()
        self.cursor.execute("insert into withdraws (cash, password) values (?)",
                            [bank.cash])
        bank.id = self.cursor.lastrowid
        self.connection.commit()
        return bank

    def update(self, bank):
        self.connect()
        self.cursor.execute("update banks set cash=?, password=? where id=?",
                            [bank.cash])
        self.connection.commit()
        self.disconnect()
        return bank

    def delete(self, deposit_id):
        self.connect()
        self.cursor.execute("delete from withdraws where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from banks")
        bank_list = [Withdraw(*bank) for bank in self.cursor.fetchall()]
        self.disconnect()
        return bank_list

    def find_by_id(self, bank_id):
        self.connect()
        self.cursor.execute("select * from withdraws where id=?", [id])
        bank = self.cursor.fetchone()
        self.disconnect()
        if bank:
            return Withdraw(*withdraw)
        return None
