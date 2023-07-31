import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army
from widgets.game import Game

class FirstTurnWindow(Toplevel):

    def __init__(self, parent, game, _submit=None,_onChange=None):
        super().__init__(parent)
        self.title('First Turn')
        self.game = game
        self.first = StringVar()
        self.first.set(game.army1.name.get())

        self._submit = _submit
        self._onChange = _onChange

        self.firstLabel = Label(self,text='First Turn')
        self.firstLabel.pack(side=tk.LEFT, expand = True)
        self.firstList = OptionMenu(
            self,
            self.first,
            game.army1.name.get(),
            *[game.army1.name.get(),game.army2.name.get()],
            command = self.refresh)
        self.firstList.pack(side=tk.LEFT, expand = True)

        self.closeButton = Button(self, text='Start Game', command=self.close)
        self.closeButton.pack(side=tk.TOP, expand = True)

    def refresh(self, *args):
        if self._onChange is not None:
            self._onChange()

    def close(self, *args):
        self.destroy()
        if self._submit is not None:
            self._submit(self.first.get())
