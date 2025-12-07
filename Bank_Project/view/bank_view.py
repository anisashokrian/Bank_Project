from tkinter import Tk, Label, Button

from view.withdraw_view import Withdraw
from view.open_account_view import OpenAccount
from view.deposit_view import Deposit

class BankView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("450x400")
        self.window.title("Bank Management")
        self.label = Label(self.window, text="Bank Account Management System", font=("Arial",15,"bold"), background= "orange", bd= 5, relief="groove")
        self.label.pack(side="top", fill= "x")

        self.button = Button(self.window, width= 35,height= 2, text = "Open Account", bg ="light pink", command=self.open_account_view)
        self.button.place(x=100, y=80)

        self.button = Button(self.window, width= 35,height= 2, text = "Deposit", bg ="light pink", command=self.deposit_view)
        self.button.place(x=100, y=170)

        self.button = Button(self.window, width= 35,height= 2, text = "Withdraw", bg ="light pink", command=self.withdraw_view)
        self.button.place(x=100, y=270)


        self.window.mainloop()



    def open_account_view(self):
        ui = OpenAccount()

    def deposit_view(self):
        ui = Deposit()

    def withdraw_view(self):
        ui = Withdraw()

