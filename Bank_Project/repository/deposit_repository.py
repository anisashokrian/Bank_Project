import sqlite3
from model import deposit
from model.deposit import Deposit


class DepositRepository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./db/bank.sqlite")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS deposits(id INTEGER PRIMARY KEY AUTOINCREMENT, cash INTEGER);""")
        self.connection.commit()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def create_deposit(self, bank):
        self.connect()
        self.cursor.execute("INSERT INTO deposits (cash) VALUES (?)",
                            [bank.cash])
        bank.id = self.cursor.lastrowid
        self.connection.commit()
        return bank

    def update(self, bank):
        self.connect()
        self.cursor.execute("UPDATE deposits SET cash=? WHERE id=?",
                            [bank.cash, bank.id])
        self.connection.commit()
        self.disconnect()
        return bank

    def delete(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM deposits WHERE id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM deposits")
        bank_list = [Deposit(*bank) for bank in self.cursor.fetchall()]
        self.disconnect()
        return bank_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from deposits where id=?", [id])
        bank = self.cursor.fetchone()
        self.disconnect()
        if bank:
            return Deposit(deposit)
        return None
