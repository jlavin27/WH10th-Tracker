import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army

class roleWidget:

    def __init__(self,window,army,_onChange = None):
        self.frame = Frame(window)
        self.frame.pack(fill=tk.X,side=tk.TOP)
        self.army = army
        self.role = army.role
        self._onChange = _onChange
        self.paddings = {'padx': 5, 'pady': 5}


        self.roleMenu = OptionMenu(
            self.frame,
            self.role,
            self.role.get(),
            *Army().roles,
            command=self.makeSelection)
        self.roleLabel = Label(self.frame, text="Role", width=18,anchor=tk.W)
        self.roleMenu.config(style='Role.TMenubutton')

        # show widget
        self.show()

    def show(self):
        self.roleLabel.grid(column=0, row=0, sticky=tk.W, **self.paddings)
        self.roleMenu.grid(column=1, row=0, sticky=tk.W, **self.paddings)


    def hide(self):
        self.roleLabel.grid_remove()
        self.roleMenu.grid_remove()

    def makeSelection(self, *args):
        if self._onChange is not None:
            self._onChange('role', self.army)
        self.format()

    def format(self):
        if(self.role.get() == Army().roles[1]):
            self.roleMenu.config(style='Green.TMenubutton')
        elif(self.role.get() == Army().roles[0]):
            self.roleMenu.config(style='Red.TMenubutton')
        else:
            self.roleMenu.config(style='TMenubutton')

    def submitRole(self):
        self.roleMenu.state(["disabled"])

    def unlock(self):
        self.roleMenu.state(["!disabled"])
