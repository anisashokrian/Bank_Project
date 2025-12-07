from tkinter import *
from tkinter import messagebox
from controller import deposit_controller
from controller.deposit_controller import DepositRepository, DepositController
from view.component.lable_with_entry import LabelWithEntry
from view.component.table import Table


class Deposit:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("575x315")
        self.window.title("Deposit")

        self.customer_id = LabelWithEntry(self.window, "Customer Id", 20,20, data_type=IntVar, state="readonly", distance=110)
        self.cash = LabelWithEntry(self.window, "Enter Cash", 20, 60, distance=110)

        self.table = Table(
            self.window,
            ["Customer Id", "Enter Cash"],
            [140, 130],
            270, 20,
            12,
          #  self.select_from_table
        )
        #Desposit Button
        Button(self.window, text="Deposit", width=25, height=2,bg="light blue" , command=self.deposit_button).place(x=35, y=245)








        self.window.mainloop()

    def deposit_button(self):
        controller = DepositController()
        status, message = controller.deposit(
            self.customer_id.get(),
            self.cash.get(),
        )
        if status:
            messagebox.showinfo("Deposit Successfully", message)
        else:
            messagebox.showerror("Deposit  Error", message)


