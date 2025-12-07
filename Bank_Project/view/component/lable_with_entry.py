from tkinter import *

class LabelWithEntry:
    def __init__(self, master, label_text, x, y , data_type=StringVar, state="normal", distance=140, on_keypress_function=None):
        self.data_type = data_type
        self.variable = data_type(master)
        Label(master, text=label_text, bg="light blue" , font=("Arial",10,"bold")).place(x=x, y=y)
        txt = Entry(master, textvariable=self.variable, state=state)
        if on_keypress_function:
            self.on_keypress_function = on_keypress_function
            txt.bind("<KeyRelease>", self.key_press)
        txt.place(x=x + distance, y=y)

    def key_press(self, e):
        self.on_keypress_function()

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

    def clear(self):
        if self.data_type == IntVar:
            self.variable.set(0)
        elif self.data_type == StringVar:
            self.variable.set("")
        elif self.data_type == DoubleVar:
            self.variable.set(0.0)
        elif self.data_type== BooleanVar:
            self.variable.set(True)
