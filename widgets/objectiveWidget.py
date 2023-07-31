import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army
from widgets.game import Game

class objectiveWidget:

    def __init__(self,window,objective,labelText,options,defaultOption=None, _onChange=None, style = None):
        self.frame = Frame(window)
        self.objective = objective
        self.labelText = labelText
        self.options = options
        self.defaultOption = defaultOption
        if defaultOption is None:
            self.defaultOption = options[0]
        self._onChange = _onChange


        #Menu
        self.menu = OptionMenu(
            self.frame,
            self.objective,
            self.defaultOption,
            *self.options,
            command = self.option_changed)
        self.label = Label(self.frame, text=self.labelText, width=18)
        # self.blank = Frame(self.frame)
        # self.blank.config(style='Blank.TFrame')

        if style is not None:
            self.menu.config(style=style)

        self.show()


    def show(self):
        self.label.pack(side=tk.LEFT)
        self.menu.pack(side=tk.LEFT)
        # self.blank.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)


    def hide(self):
        self.label.pack_forget()
        self.menu.pack_forget()

    def lock(self):
        self.menu.state(['disabled'])

    def unlock(self):
        self.menu.state(['!disabled'])

    def pack(self):
        self.frame.pack(side=tk.TOP,anchor=tk.NW)

    def pack_forget(self):
        self.frame.pack_forget()

    def option_changed(self, *args):
        if self._onChange is not None:
            self._onChange()
        return

class soWidget:

    def __init__(self,window,objective,_onChange = None):
        self.frame = Frame(window)
        self.objective = objective
        self.paddings = {'padx': 5, 'pady': 5}
        self.isTatical = True
        self._onChange = _onChange

        #SO Menu
        self.soTaticalMenu = OptionMenu(
            self.frame,
            self.objective,
            Game.secondaries[0],
            *Game.secondaries,
            command=self.makeChoice)
        self.soTaticalMenu.config(style='SO.TMenubutton')

        self.soFixedMenu = OptionMenu(
            self.frame,
            self.objective,
            Game.fixedSecondaries[0],
            *Game.fixedSecondaries,
            command=self.makeChoice)
        self.soFixedMenu.config(style='SO.TMenubutton')

        self.soLabel = Label(self.frame, text="Seconary Objective", width=18,anchor=tk.W)
        self.soDelete = Button(self.frame, text='-', width=2,command=self.deleteChoice)
        self.soDelete.state(['disabled'])

        #show widget
        self.show()

    def setTatical(self, isTatical):
        if isTatical:
            self.objective = Game.secondaries[0]
        else:
            self.objective = Game.fixedSecondaries[0]
        self.isTatical = isTatical

    def show(self):
        self.soLabel.pack(side=tk.LEFT)
        if self.isTatical:
            self.soTaticalMenu.pack(side=tk.LEFT)
        else:
            self.soFixedMenu.pack(side=tk.LEFT)
        self.soDelete.pack(side=tk.LEFT)

    def makeChoice(self, *args):
        if self._onChange is not None:
            self._onChange('update')
        if self.isTatical:
            self.soTaticalMenu.state(["disabled"])
        else:
            self.soFixedMenu.state(["disabled"])
        self.soDelete.state(['!disabled'])


    def deleteChoice(self, *args):
        if self._onChange is not None:
            self._onChange('update')
        if self.isTatical:
            self.objective = Game.secondaries[0]
            self.soTaticalMenu.state(["!disabled"])
        else:
            self.soFixedMenu.state(["!disabled"])
            self.objective = Game.fixedSecondaries[0]
        self.soDelete.state(['disabled'])

    def hide(self):
        self.soLabel.pack_forget()
        self.soTaticalMenu.pack_forget()
        self.soFixedMenu.pack_forget()
        self.soDelete.pack_forget()

    def lock(self):
        if self.isTatical:
            self.soTaticalMenu.state(['disabled'])
        else:
            self.soFixedMenu.state(['disabled'])
        self.soDelete.pack_forget()

    def unlock(self):
        if self.isTatical:
            self.soTaticalMenu.state(['!disabled'])
        else:
            self.soFixedMenu.state(['!disabled'])

    def clear(self):
        if self.isTatical:
            self.objective = Game.secondaries[0]
        else:
            self.objective = Game.fixedSecondaries[0]

    def pack(self):
        self.frame.pack(side=tk.TOP,anchor=tk.NW)

    def pack_forget(self):
        self.frame.pack_forget()
