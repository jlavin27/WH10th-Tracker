import tkinter as tk
from tkinter import ttk
from widgets import *
from styler import Styler

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('40K Game Tracker')

        # set up variables
        self.game = Game()

        self.style = Styler(self)

        # create widgets
        self.header = Frame(self)
        self.gameSheet = gameWidget(self.header, self.game,_onChange=self.update)


        self.trackerFrame = Frame(self)

        self.tracker1 = armyTracker(self.trackerFrame,self.game.army1,_onChange=self.update)
        self.tracker2 = armyTracker(self.trackerFrame,self.game.army2,_onChange=self.update)

        self.header.pack(fill=tk.BOTH)
        self.trackerFrame.pack(fill=tk.BOTH)


    def tracker2ChangeRole(self):
        if(self.game.army1.role.get() == Army.roles[0]):
            self.game.army2.role.set(Army.roles[1])
        elif(self.game.army1.role.get() == Army.roles[1]):
            self.game.army2.role.set(Army.roles[0])
        self.gameSheet.showGameDetails()
        self.tracker2.format()

    def tracker1ChangeRole(self):
        if(self.game.army2.role.get() == Army.roles[0]):
            self.game.army1.role.set(Army.roles[1])
        elif(self.game.army2.role.get() == Army.roles[1]):
            self.game.army1.role.set(Army.roles[0])
        self.gameSheet.showGameDetails()
        self.tracker1.format()

    #Call Back Handler
    def update(self, command, arg=None):
        match command:
            case 'lockGambit':
                self.lockGambit()
            case 'enableGambit':
                self.enableGambit()
            case 'startGame':
                self.startGame()
            case 'endGame':
                self.endGame()
            case 'reset':
                self.reset()
            case 'close':
                self.destroy()
            case 'enableLeviathan':
                self.enableLeviathan()
            case 'disableLeviathan':
                self.disableLeviathan()
            case 'role':
                if arg == self.game.army1:
                    self.tracker2ChangeRole()
                if arg == self.game.army2:
                    self.tracker1ChangeRole()
            case 'update':
                self.gameSheet.showGameDetails()

            case _:
                pass

    def startGame(self):
        self.firstTurnWindow = FirstTurnWindow(self,self.game,_submit=self.gameSheet.setCurrentlyPlaying,_onChange=self.gameSheet.refresh)
        self.tracker1.start(self.game.type)
        self.tracker2.start(self.game.type)

        # self.tracker1.hideMode()
        # self.tracker2.hideMode()
        #
        # #Check if Leviathan
        # if self.game.type.get() == Game.types[2] or self.game.type.get() == Game.types[3]:
        #     self.tracker1.showSO()
        #     self.tracker2.showSO()
            # if self.game.mode.get() == Game.modes[1]:
            #     self.tracker1.lockSO()
            #     self.tracker2.lockSO()

    def endGame(self):
        self.tracker1.end()
        self.tracker2.end()
        self.endScreen = GameEndScreen(self,self.game,_onChange=self.update)

    def reset(self):
        self.game.reset()
        self.gameSheet.reset()
        self.tracker1.reset()
        self.tracker2.reset()

    def enableGambit(self):
        self.tracker1.enableGambit()
        self.tracker2.enableGambit()

    def lockGambit(self):
        self.tracker1.lockGambit()
        self.tracker2.lockGambit()

    def enableSecondaries(self, enable):
        if enable:
            self.tracker1.isSOTatical(False)
            self.tracker2.isSOTatical(False)
            self.tracker1.showSO()
            self.tracker2.showSO()

        else:
            self.tracker1.isSOTatical(True)
            self.tracker2.isSOTatical(True)
            self.tracker1.hideSO()
            self.tracker2.hideSO()

    def enableLeviathan(self):
        self.tracker1.showMode()
        self.tracker2.showMode()

    def disableLeviathan(self):
        self.tracker1.hideMode()
        self.tracker2.hideMode()
        # self.tracker1.hideSO()
        # self.tracker2.hideSO()

if __name__ == "__main__":
    app = App()
    app.mainloop()
