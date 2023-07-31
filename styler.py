import tkinter as tk
from tkinter import ttk

class Styler(tk.Tk):

    def __init__(self,tk):

        self.style = ttk.Style(tk)

        #OptionMenu
        self.style.map('TMenubutton',
                       relief=[('!disabled', 'raised'),('disabled', 'flat')],
                       foreground=[('!disabled','black'),('disabled','black')])
        self.style.layout('TMenubutton', [('Menubutton.border',
                                            {'sticky': 'nswe',
                                            'children': [('Menubutton.focus',
                                                {'sticky': 'nswe',
                                                'children': [
                                                ('Menubutton.padding',
                                                    {'expand': '1',
                                                    'sticky': 'we',
                                                    'children': [('Menubutton.label',
                                                    {'side': 'left', 'sticky': ''})]})]})]})])
        #Attacker/Defender
        self.style.map('Role.TMenubutton',
                       width=[('!disabled','8'),('disabled','8')])

        self.style.map('Red.TMenubutton',
                       foreground=[('!disabled','red'),('disabled','red')],
                       width=[('!disabled','8'),('disabled','8')]
                       )

        self.style.map('Green.TMenubutton',
                       foreground=[('!disabled','green'),('disabled','green')],
                       width=[('!disabled','8'),('disabled','8')]
                       )

        #Army Names
        self.style.map('Name.TMenubutton',
                       width=[('!disabled','22'),('disabled','22')]
                      )
        self.style.map('Type.TMenubutton',
                      width=[('!disabled','18'),('disabled','18')]
                      )

        #Frame
        self.style.configure('Left.TFrame',background='Green')
        self.style.configure('Right.TFrame',background='Red')
        self.style.configure('Blank.TFrame',background='Blue')

        #SO
        self.style.map('SO.TMenubutton',
                       width=[('!disabled','21'),('disabled','21')]
                      )
