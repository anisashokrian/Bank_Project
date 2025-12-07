from controller.open_account_controller import OpenAccountController
from view.component.lable_with_entry import LabelWithEntry
from view.component.table import Table
from tkinter import *
from tkinter import messagebox


class OpenAccount:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("715x315")
        self.window.title("Open Account")

        self.customer_id = LabelWithEntry(self.window, "Customer Id", 20,20, data_type=IntVar)
        self.customer_name = LabelWithEntry(self.window, "Customer Name", 20, 60)
        self.password = LabelWithEntry(self.window, "Customer Password", 20, 100)
        self.cash_deposit = LabelWithEntry(self.window, "Cash Deposit", 20, 140)


        self.table = Table(
            self.window,
            ["Id", "UserName", "password", "Cash Deposit"],
            [50, 120, 120,100],
            300, 20,
            12,
            #self.select_from_table
        )

        #OpenAccount Button
        Button(self.window, text="Save", width=25, height=2,bg="light blue" , command=self.save_button).place(x=35, y=245)

        self.window.mainloop()

    def save_button(self):
        controller = OpenAccountController()
        status, message = controller.save(
            self.customer_id.get(),
            self.customer_name.get(),
            self.password.get(),
            self.cash_deposit.get()
        )
        if status:
            messagebox.showinfo("Account Saved", message)
            self.table.treeview.insert("","end", values=(
                self.customer_id.get(),
                self.customer_name.get(),
                self.password.get(),
                self.cash_deposit.get()
            ))
        else:
            messagebox.showerror("Account Save Error", message)



