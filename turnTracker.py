import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army
from widgets.game import Game

class turnTracker:

    def __init__(self,window,game,_onChange=None):
        self.frame = Frame(window)
        self.game = game
        self._onChange = _onChange
        self.paddings = {'padx': 5, 'pady': 5}
        self.turn = 1
        self.firstPlayer = game.army1
        self.secondPlayer = game.army2
        self.currentlyPlaying = game.army1

        #create elements
        self.armyLabel = Label(self.frame, text='Army')
        self.armyText = Label(self.frame, text=self.currentlyPlaying.name.get())
        self.turnLabel = Label(self.frame, text='Turn')
        self.turnText = Label(self.frame, text=str(self.turn))
        self.turnButton = Button(self.frame, text="End Turn", command=self.nextTurn)
        self.endGameButton = Button(self.frame, text="End Game", command=self.endGame)

        self.show()

    def reset(self):
        self.turn = 1
        self.turnButton.state(['!disabled'])
        self.endGameButton.state(['!disabled'])
        self.turnLabel.config(text=self.currentlyPlaying.name.get())
        self.turnText.config(text=str(self.turn))


    def nextTurn(self):
        if self.currentlyPlaying == self.secondPlayer:
            if self.turn + 1 > 5:
                self.endGame()
            else:
                self.turn += 1
                self.currentlyPlaying = self.firstPlayer
                self.turnText.config(text=str(self.turn))
                if (self.game.type.get() == Game().types[2] or self.game.type.get() == Game().types[3]) and self.turn == 4:
                    # if self._enableGambit is not None:
                    #     self._enableGambit()
                    if self._onChange is not None:
                        self._onChange('enableGambit')
        else:
            if (self.game.type.get() == Game().types[2] or self.game.type.get() == Game().types[3]) and self.turn == 4:
                    if self._onChange is not None:
                        self._onChange('lockGambit')
            self.currentlyPlaying = self.secondPlayer
        self.refresh()

    def setCurrentlyPlaying(self,army):
        # if self.game.army1.role.get() == Army().roles[0]:
        #     self.firstPlayer = self.game.army1
        #     self.secondPlayer = self.game.army2
        # elif self.game.army2.role.get() == Army().roles[0]:
        #     self.firstPlayer =self.game.army2
        #     self.secondPlayer = self.game.army1
        # else:
        #     self.firstPlayer = self.game.army1
        #     self.secondPlayer = self.game.army2
        # self.currentlyPlaying = self.firstPlayer
        self.currentlyPlaying = army
        self.refresh()

    def endGame(self):
        self.turnButton.state(['disabled'])
        self.endGameButton.state(['disabled'])
        # if self._endGame is not None:
        #     self._endGame()
        if self._onChange is not None:
            self._onChange('endGame')

    def refresh(self):
        self.armyText.config(text=self.currentlyPlaying.name.get())

    def show(self):
        self.armyLabel.grid(column=0, row=0, sticky=tk.W, **self.paddings)
        self.armyText.grid(column=1, row=0, sticky=tk.W, **self.paddings)
        self.turnLabel.grid(column=0, row=1, sticky=tk.W, **self.paddings)
        self.turnText.grid(column=1, row=1, sticky=tk.W, **self.paddings)
        self.turnButton.grid(column=0,row=2, sticky=tk.W, **self.paddings)
        self.endGameButton.grid(column=1,row=2, sticky=tk.W, **self.paddings)

    def hide(self):
        self.armyLabel.grid_forget()
        self.armyText.grid_forget()
        self.turnLabel.grid_forget()
        self.turnText.grid_forget()
        self.turnButton.grid_forget()
        self.endGame.grid_forget()

    def pack(self):
        self.frame.pack(fill= tk.BOTH)

    def pack_forget(self):
        self.frame.pack_forget()
