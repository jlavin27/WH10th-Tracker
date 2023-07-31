import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army
from widgets.game import Game

class GameEndScreen(Toplevel):

    def __init__(self, parent, game, _onChange=None):
        super().__init__(parent)
        self.title('GameEnd')
        self.game = game
        self._onChange = _onChange
        self.winner = self.getWinner()
        self.winnerLabel = Label(self,text=self.winner)
        self.winnerLabel.pack(side=tk.TOP, expand = True)
        self.closeButton = Button(self, text='Close', command=self.close)
        self.closeButton.pack(side=tk.TOP, expand = True)
        self.resetButton = Button(self, text='Reset', command=self.reset)
        self.resetButton.pack(side=tk.TOP, expand = True)

    def getWinner(self):
        # print(self.game.army1.vp.get())
        # print(self.game.army2.vp.get())
        if self.game.army1.vp.get() > self.game.army2.vp.get():
            return self.game.army1.name.get() + ' Wins'
        elif self.game.army2.vp.get() > self.game.army1.vp.get():
            return self.game.army2.name.get() + ' Wins'
        else:
            return "Draw"

    def close(self, *args):
        self.destroy()
        if self._onChange is not None:
            self._onChange('close')


    def reset(self, *args):
        if self._onChange is not None:
            self._onChange('reset')
        self.destroy()
