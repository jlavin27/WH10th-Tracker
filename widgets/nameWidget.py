import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army

class nameWidget:

    def __init__(self,window,army,_onChange = None):
        self.frame = Frame(window)
        self.frame.pack(fill=tk.X,side=tk.TOP)
        self.army = army
        self.paddings = {'padx': 5, 'pady': 5}
        self._onChange = _onChange

        #Name Menu
        self.nameMenu = OptionMenu(
            self.frame,
            self.army.name,
            self.army.name.get(),
            *Army().armies,
            command = self.onChange)
        self.nameMenu.config(style='Name.TMenubutton')
        self.nameLabel = Label(self.frame, text="Army", width=18,anchor=tk.W)

        self.show()

    def show(self):
        self.nameLabel.grid(column=0, row=0, sticky=tk.W, **self.paddings)
        self.nameMenu.grid(column=1, row=0, sticky=tk.W, **self.paddings)

    def hide(self):
        self.nameLable.grid_remove()
        self.nameMenu.grid_remove()

    def submitName(self):
        self.nameMenu.state(["disabled"])

    def unlock(self):
        self.nameMenu.state(["!disabled"])

    def onChange(self,*args):
        if self._onChange is not None:
            self._onChange('update')
