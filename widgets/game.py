from tkinter import StringVar
from widgets.army import Army
import random

class Game:

    types = ["Combat Patrol",
        "Only War",
        "Leviathan",
        "Leviathan (Custom)"]

    combatPatrols = ["Clash of Patrols",
        "Archeotech Recovery",
        "Forward Outpost",
        "Scorched Earth",
        "Sweeping Raid",
        "Display of Might"]

    primaries = ["Take and Hold",
        "The Ritual",
        "Priority Targets",
        "Vital Ground",
        "Scorched Earth",
        "Supply Drop",
        "Purge the Foe",
        "Sites of Power",
        "Deploy Servo-Skulls"]

    secondaries = ["None",
        "Secure No Mans Land",
        "Capture Enemy Outpost",
        "Extend Battle Lines",
        "Defend Stronghold",
        "Storm Hostile Objective",
        "Engage on All Fronts",
        "A Tempting Target",
        "Behind Enemy Lines",
        "Area Denial",
        "Assassination",
        "Cleanse",
        "Deploy Teleport Homer",
        "Investigate Signals",
        "Overwhelming Force",
        "No Prisonsers",
        "Bring it Down"]

    fixedSecondaries = ["None",
        "Storm Hostile Objective",
        "Engage on All Fronts",
        "Behind Enemy Lines",
        "Assassination",
        "Cleanse",
        "Deploy Teleport Homer",
        "Bring it Down"]

    missionRules = ["Chilling Rain",
        "Hidden Supplies",
        "Minefields",
        "Sweep and Clear",
        "Supply Lines",
        "Scambler Fields",
        "Secret Intel",
        "Targets of Opportunity",
        "Delayed Reserves",
        "Vox Static",
        "Chosen Battlefield",
        "Maelstrom of Battle"]

    deployments = ["Hammer and Anvil",
        "Search and Destroy",
        "Crucible of Batle",
        "Dawn of War",
        "Sweeping Engagement"]

    gambits = ["Proceed as Planned",
        "Orbital Strike Corrdinate",
        "Emergency Evacuation",
        "Delaying Tatics"]

    modes = ["Tatical",
        "Fixed"]

    def __init__(self,type="None"):
        self.type = StringVar()
        self.type.set(type)
        self.mission = StringVar()
        self.mission.set("None")
        self.primary = StringVar()
        self.primary.set("None")
        self.missionRule = StringVar()
        self.missionRule.set("None")
        self.deployment = StringVar()
        self.deployment.set("None")
        self.army1 = Army()
        self.army2 = Army()

    def setMission(self):
        if self.mission.get() == self.combatPatrols[0]:
            self.primary.set("Take and Hold")
            self.missionRule.set("Retrieve Intelligence")
            self.deployment.set("Clash of Patrols")
        elif self.mission.get() == self.combatPatrols[1]:
            self.primary.set("Recover Archeotech")
            self.missionRule.set("Irradiate Power Cells")
            self.deployment.set("Archeotech Recovery")
        elif self.mission.get() == self.combatPatrols[2]:
            self.primary.set("Vital Ground")
            self.missionRule.set("Sabotage Enemy Comms")
            self.deployment.set("Forward Outpost")
        elif self.mission.get() == self.combatPatrols[3]:
            self.primary.set("Raze and Ruin")
            self.missionRule.set("Raze and Ruin")
            self.deployment.set("Scorched Earth")
        elif self.mission.get() == self.combatPatrols[4]:
            self.primary.set("Priority Targets")
            self.missionRule.set("Supply Lines")
            self.deployment.set("Sweeping Raid")
        elif self.mission.get() == self.combatPatrols[5]:
            self.primary.set("Symbolic Sites")
            self.missionRule.set("Break Their Spirit")
            self.deployment.set("Display of Might")

    def generateLeviathan(self):
        self.primary.set(self.primaries[random.randrange(len(self.primaries))])
        self.missionRule.set(self.missionRules[random.randrange(len(self.missionRules))])
        self.deployment.set(self.deployments[random.randrange(len(self.deployments))])

    def generateOnlyWar(self):
        self.primary.set("Capture and Control")
        self.missionRule.set("Only War")
        self.deployment.set("Only War")

    def getType(self):
        return self.type.get()

    def reset(self):
        self.type.set("None")
        self.mission.set("None")
        self.primary.set("None")
        self.missionRule.set("None")
        self.deployment.set("None")
        self.army1.reset()
        self.army2.reset()
