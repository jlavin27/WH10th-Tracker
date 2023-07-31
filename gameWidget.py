import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army
from widgets.game import Game
from widgets.turnTracker import turnTracker
from widgets.objectiveWidget import *

class gameWidget:

    states = ['PreGame','Playing','PostGame']

    def __init__(self,window,game,_onChange=None):
        self._onChange = _onChange
        self.frame = Frame(window)
        self.state = self.states[0]

        self.frameLeft = Frame(self.frame)

        self.frameRight = Frame(self.frame)

        self.frame.pack(fill=tk.X,side=tk.TOP,expand=True)
        self.frameLeft.pack(side=tk.LEFT,anchor=tk.W,fill=tk.BOTH,expand=True)
        self.frameRight.pack(side=tk.RIGHT,anchor=tk.W,fill=tk.BOTH,expand=True)
        self.game = game

        # create elements

        #Game Type Select menu
        self.typeChoice = objectiveWidget(self.frameLeft,self.game.type,"Game Type",Game.types,defaultOption='None',_onChange=self.submitType, style='Type.TMenubutton')

        #Mission Select menu
        self.missionChoice = objectiveWidget(self.frameLeft,self.game.mission,"Mission",Game.combatPatrols,defaultOption=self.game.mission.get(),_onChange=self.submitMission)

        #Turn Tracker
        self.turn = turnTracker(self.frameLeft,self.game,self._onChange)

        #Game Details
        self.primary = objectiveWidget(self.frameRight,self.game.primary,"Primary Objective",Game.primaries,defaultOption=Game.primaries[0], style='Name.TMenubutton')
        self.rule = objectiveWidget(self.frameRight,self.game.missionRule,"Mission Rule",Game.missionRules,defaultOption=Game.missionRules[0], style='Name.TMenubutton')
        self.deployment = objectiveWidget(self.frameRight,self.game.deployment,"Deployment",Game.deployments,defaultOption=Game.deployments[0], style='Name.TMenubutton')

        #Finalize Game
        self.finalize = Button(self.frameLeft, text="Start Game", command=self.finalizeGame)

        #Take action
        self.chooseGameType()

    def reset(self):
        self.state = self.states[0]
        self.turn.pack_forget()
        self.turn.reset()
        self.chooseGameType()
        self.showGameDetails()

    def submitType(self, *args):
        #Combat Partol
        if self.game.type.get() == Game().types[0]:
            self.playMission()
        #Only War
        elif self.game.type.get() == Game().types[1]:
            self.playOnlyWar()
        #Leviathan
        elif self.game.type.get() == Game().types[2] or self.game.type.get() == Game().types[3]:
            self.playLeviathan()

        self.submitMode()
        self.showGameDetails()

    def submitMode(self, *args):
        if self._onChange is not None:
            if (self.game.type.get() == Game().types[2] or self.game.type.get() == Game().types[3]):
                self._onChange('enableLeviathan')
            else:
                self._onChange('disableLeviathan')
        self.showGameDetails()

    def submitMission(self, *args):
        self.game.setMission()
        self.showGameDetails()


    def chooseGameType(self):
        self.typeChoice.pack()

    def clearTypeLine(self):
        self.typeChoice.pack_forget()

    def showMission(self):
        self.missionChoice.pack()

    def clearMissionLine(self):
        self.missionChoice.pack_forget()

    def playMission(self):
        self.submitMission()
        if self._onChange is not None:
            self._onChange('disableLeviathan')
        self.showMission()
        self.lockMission()

    def playOnlyWar(self):
        self.clearMissionLine()
        if self._onChange is not None:
            self._onChange('disableLeviathan')
        self.game.generateOnlyWar()
        self.lockMission()

    def playLeviathan(self):
        self.clearMissionLine()
        if self._onChange is not None:
            self._onChange('enableLeviathan')
        self.game.generateLeviathan()
        if self.game.type.get() == Game().types[3]:
            self.unlockMission()
        else:
            self.lockMission()

    def checkSO(self, army):
        if army.mode.get() == Army.modes[1]:
            if army.so1.get() != Game.fixedSecondaries[0] and army.so2.get() != Game.fixedSecondaries[0]:
                return True
            else:
                return False
        else:
            return True

    def showGameDetails(self):
        #Check Game State
        if self.state == self.states[0]:
            #Checkgame Type
            if self.game.type.get() != 'None':
                self.primary.pack()
                self.rule.pack()
                self.deployment.pack()

                #Check if army names are selected
                if self.game.army1.name.get() != 'None' and self.game.army2.name.get() != 'None':
                    #Check if roles are chosen
                    if self.game.army1.role.get() != 'None' and self.game.army2.role.get() != 'None':
                        #Check if Leviathan Game
                        if self.game.type.get() == Game.types[2] or self.game.type.get() == Game.types[3]:
                            #check if Army has fixed objectives and selected them
                            if self.checkSO(self.game.army1) and self.checkSO(self.game.army2):
                                self.showFinalizeGame()
                            else:
                                self.hideFinalizeGame()
                        #Check if Combat Patrol and Mission is selected
                        elif self.game.type.get() == Game.types[0] and self.game.mission.get() == 'None':
                            self.hideFinalizeGame()
                        else:
                            self.showFinalizeGame()
                    else:
                        self.hideFinalizeGame()
                else:
                    self.hideFinalizeGame()
            else:
                self.hideFinalizeGame()
                self.primary.pack_forget()
                self.rule.pack_forget()
                self.deployment.pack_forget()
        else:
            self.hideFinalizeGame()

    def lockMission(self):
        self.primary.lock()
        self.rule.lock()
        self.deployment.lock()

    def unlockMission(self):
        self.primary.unlock()
        self.rule.unlock()
        self.deployment.unlock()

    def showFinalizeGame(self):
        self.finalize.pack(fill=tk.X,side=tk.BOTTOM,expand=True)

    def hideFinalizeGame(self):
        self.finalize.pack_forget()

    def refresh(self):
        print('Refresh')
        self.turn.refresh()

    def setCurrentlyPlaying(self,armyName):
        if armyName == self.game.army1.name.get():
            self.turn.setCurrentlyPlaying(self.game.army1)
        else:
            self.turn.setCurrentlyPlaying(self.game.army2)


    def finalizeGame(self):
        #Remove Type and Mission lines
        self.clearTypeLine()
        self.clearMissionLine()
        self.hideFinalizeGame()

        #Lock Rules
        self.lockMission()

        self.state = self.states[1]

        # if self._submit is not None:
        #     self._submit()
        if self._onChange is not None:
                self._onChange('startGame')
        # self.turn.getFirstTurn()
        self.turn.pack()


    def deleteWindow(self):
        self.frame.pack_forget()
