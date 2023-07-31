import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army

class counterWidget:

    def __init__(self,window,label,val, limit = -1, _onChange = None):
        self.frame = Frame(window)
        self.val = val
        self.paddings = {'padx': 5, 'pady': 5}
        self.limit = limit
        self._onChange = _onChange

        #Create Label
        self.counterLabel = Label(self.frame, text=label, width=18,anchor=tk.W)
        self.minus = Button(self.frame, text="-", command=self.minus, width=2)
        self.counterVal = Label(self.frame, text=str(self.val.get()))
        self.add = Button(self.frame, text="+", command=self.add, width=2)

        self.show()

    def update(self):
        # self.val.set(self.count)
        self.counterVal.config(text=str(self.val.get()))

    def add(self, amount = None):
        if amount is not None:
            if self.limit == -1:
                self.val.set(self.val.get() + amount)
            elif self.val.get() + amount < self.limit:
                self.val.set(self.val.get() + amount)
            else:
                self.val.set(self.limit)
        else:
            if self.limit == -1:
                self.val.set(self.val.get() + 1)
            elif self.val.get() + 1 < self.limit:
                self.val.set(self.val.get() + 1)
            else:
                self.val.set(self.limit)
        if self._onChange is not None:
            self._onChange()
        self.update()

    def minus(self, amount = None):
        if amount is not None:
            if self.val.get() - amount > 0:
                self.val.set(self.val.get() - amount)
            else:
                self.val.set(0)
        if self.val.get() > 0:
            self.val.set(self.val.get() - 1)
        if self._onChange is not None:
            self._onChange()
        self.update()

    def show(self):
        self.counterLabel.grid(row=0, column=0, sticky=tk.W, **self.paddings)
        self.minus.grid(row=0, column=1, sticky=tk.W, **self.paddings)
        self.counterVal.grid(row=0, column=2, sticky=tk.W, **self.paddings)
        self.add.grid(row=0, column=3, sticky=tk.W, **self.paddings)

    def hide(self):
        self.counterLabel.grid_forget()
        self.minus.grid_forget()
        self.counterVal.grid_forget()
        self.add.grid_forget()

    def pack(self):
        self.frame.pack(fill=tk.X,side=tk.TOP)

    def pack_forget(self):
        self.frame.pack_forget()

    def disable(self):
        self.minus.state(['disabled'])
        self.minus.grid_forget()
        self.add.state(['disabled'])
        self.add.grid_forget()

    def enable(self):
        self.minus.state(['!disabled'])
        self.minus.grid(row=0, column=1, sticky=tk.W, **self.paddings)
        self.add.state(['!disabled'])
        self.add.grid(row=0, column=3, sticky=tk.W, **self.paddings)
