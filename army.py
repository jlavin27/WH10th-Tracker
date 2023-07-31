from tkinter import StringVar,IntVar

class Army:

    roles = ["Attacker","Defender"]
    armies = ["Aeldari",
                "Tau",
                "Orks",
                "Necrons",
                "Leagues of Votann",
                "Genestealer Cults",
                "Drukhari",
                "Imperial Knights",
                "Astra Militarum",
                "Agents of the Imperium",
                "Deathwatch",
                "Adeptus Custodes",
                "Adeptus Mechanicus",
                "Grey Knights",
                "Adepta Soroitas",
                "Chaos Knights",
                "Thousand Sons",
                "Chaos Daemons",
                "Death Guard",
                "Chaos Space Marines",
                "World Eaters",
                "Blood Angels",
                "Black Templars",
                "Dark Angels",
                "Space Wolves",
                "Space Marines",
                "Tyranids"]
    modes = ["Tatical",
        "Fixed"]

    def __init__(self,name="None",role="None"):
        self.name = StringVar()
        self.name.set(name)
        self.role = StringVar()
        self.role.set(role)
        self.vp = IntVar()
        self.vp.set(0)
        self.pvp = IntVar()
        self.pvp.set(0)
        self.svp = IntVar()
        self.svp.set(0)
        self.cp = IntVar()
        self.cp.set(0)
        self.mode = StringVar()
        self.mode.set(self.modes[0])
        self.so1 = StringVar()
        self.so1.set("None")
        self.so2 = StringVar()
        self.so2.set("None")
        self.gambit = StringVar()
        self.gambit.set("None")

    def reset(self):
        self.name.set("None")
        self.role.set("None")
        self.vp.set(0)
        self.pvp.set(0)
        self.svp.set(0)
        self.cp.set(0)
        self.mode.set(self.modes[0])
        self.so1.set("None")
        self.so2.set("None")
        self.gambit.set("None")
