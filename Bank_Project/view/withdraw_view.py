from tkinter import *
from tkinter import messagebox
from controller.withdraw_controller import WithdrawController
from view.component.lable_with_entry import LabelWithEntry
from view.component.table import Table


class Withdraw:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("730x315")
        self.window.title("Withdraw")

        self.customer_id = LabelWithEntry(self.window, "Customer Id", 20,20, data_type=IntVar, distance=120)
        self.cash = LabelWithEntry(self.window, "Enter Cash", 20, 60, distance=120)
        self.password = LabelWithEntry(self.window, "Enter Password", 20, 100, distance=120)

        self.table = Table(
            self.window,
            ["Customer Id", "Enter Cash", "Enter Password"],
            [140, 130, 150],
            275, 20,
            12,
          #  self.select_from_table
        )
        #Desposit Button
        Button(self.window, text="Withdraw", width=25, height=2,bg="light blue" , command=self.withdraw_button).place(x=35, y=245)








        self.window.mainloop()

    def withdraw_button(self):
        controller = WithdrawController()
        status, message = controller.withdraw(
            self.customer_id.get(),
            self.cash.get(),
            self.password.get(),
        )
        if status:
            messagebox.showinfo("Withdraw Successfully", message)
        else:
            messagebox.showerror("Withdraw  Error", message)