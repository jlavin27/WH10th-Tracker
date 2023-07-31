import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from widgets.army import Army
from widgets.game import Game
from widgets.nameWidget import nameWidget
from widgets.roleWidget import roleWidget
from widgets.counterWidget import counterWidget
from widgets.objectiveWidget import *

class armyTracker:

    def __init__(self,window,army,_onChange = None):
        self.frame = Frame(window)
        self.frame.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)
        self.army = army
        self._onChange = _onChange

        #Name Menu
        self.name = nameWidget(self.frame,self.army,self._onChange)

        #Role Menu
        self.role = roleWidget(self.frame,self.army,_onChange)

        #VP Tracker
        self.vp = counterWidget(self.frame, "Victory Points", self.army.vp)
        self.vp.hide()

        self.pvp = counterWidget(self.frame, "Primary Points", self.army.pvp, limit = 50, _onChange = self.updateVP)
        self.pvp.hide()

        self.svp = counterWidget(self.frame, "Secondary Points", self.army.svp, limit = 40, _onChange = self.updateVP)
        self.svp.hide()

        #CP Tracker
        self.cp = counterWidget(self.frame, "Command Points", self.army.cp)
        self.cp.hide()

        #Mode
        self.modeChoice = objectiveWidget(self.frame,self.army.mode,"Secondary Missions",Army.modes,defaultOption=self.army.mode.get(),_onChange=self.submitMode)
        self.modeChoice.hide()
        self.modeChoice.pack()

        #SO Trackers
        self.so1 = soWidget(self.frame,self.army.so1,self._onChange)
        self.so2 = soWidget(self.frame,self.army.so2,self._onChange)
        self.hideSO()
        self.packSO()

        #Gambit Tracker
        self.gambit = objectiveWidget(self.frame,self.army.gambit,"Gambit",Game.gambits,defaultOption=Game.gambits[0])
        self.gambit.hide()


        self.name.show()

    def onChange(self):
        if self._onChange is not None:
            self._onChange('Tracker')
            self.format()

    def format(self):
        self.role.format()

    def reset(self):
        self.name.unlock()
        self.role.unlock()

        #Counters
        self.pack_forget_Counters()
        self.vp.enable()
        self.vp.update()
        self.pvp.enable()
        self.pvp.update()
        self.svp.enable()
        self.svp.update()
        self.cp.enable()
        self.cp.update()
        self.hideCounters()

        #Mode
        self.modeChoice.pack_forget()
        self.modeChoice.hide()

        #Secondary Objectives
        self.SOpack_forget()
        self.hideSO()
        self.so1.unlock()
        self.so2.unlock()

        #Gambits
        self.gambit.pack_forget()
        self.gambit.hide()
        self.gambit.unlock()

        self.format()

    def showSO(self):
        self.so1.show()
        self.so2.show()
        self.so1.unlock()
        self.so2.unlock()

    def hideSO(self):
        self.so1.hide()
        self.so2.hide()
        self.so1.clear()
        self.so2.clear()

    def packSO(self):
        self.so1.pack()
        self.so2.pack()

    def SOpack_forget(self):
        self.so1.pack_forget()
        self.so2.pack_forget()

    def showMode(self):
        self.modeChoice.show()
        self.modeChoice.pack()

    def hideMode(self):
        self.modeChoice.hide()
        self.modeChoice.pack_forget()
        self.SOpack_forget()

    def lockSO(self):
        self.so1.lock()
        self.so2.lock()

    def submitMode(self):
        if self.army.mode.get() == self.army.modes[0]:
            self.so1.setTatical(True)
            self.so2.setTatical(True)
            self.hideSO()
            self.SOpack_forget()
        else:
            self.so1.setTatical(False)
            self.so2.setTatical(False)
            self.showSO()
            self.packSO()
        if self._onChange is not None:
            self._onChange('update')

    def isSOTatical(self, isTatical):
        self.so1.setTatical(isTatical)
        self.so2.setTatical(isTatical)

    def showCounters(self):
        self.vp.show()
        self.pvp.show()
        self.svp.show()
        self.cp.show()

    def hideCounters(self):
        self.vp.hide()
        self.pvp.hide()
        self.svp.hide()
        self.cp.hide()

    def packCounters(self,gameType):
        self.vp.pack()
        self.pvp.pack()
        if gameType.get() == Game.types[2] or gameType.get() == Game.types[3]:
            self.svp.pack()
        self.cp.pack()

    def pack_forget_Counters(self):
        self.vp.pack_forget()
        self.pvp.pack_forget()
        self.svp.pack_forget()
        self.cp.pack_forget()

    def updateVP(self):
        self.army.vp.set(self.army.pvp.get() + self.army.svp.get())
        self.vp.update()

    def start(self, gameType):
        self.name.submitName()
        self.role.submitRole()
        self.SOpack_forget()
        self.showCounters()
        self.vp.disable()
        self.packCounters(gameType)
        self.modeChoice.pack_forget()
        if gameType.get() == Game.types[2] or gameType.get() == Game.types[3]:
            self.showSO()
            self.packSO()
            if self.army.mode.get() == self.army.modes[1]:
                self.lockSO()

    def end(self):
        self.vp.disable()
        self.cp.disable()
        self.pvp.disable()
        self.svp.disable()
        self.so1.lock()
        self.so2.lock()

    def enableGambit(self):
        self.gambit.show()
        self.gambit.pack()

    def lockGambit(self):
        self.gambit.lock()
