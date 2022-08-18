from tkinter import *

class Gui:
    def __init__(self, root) -> None:
        textFrame = Frame(root)
        textFrame.pack()

        verScroll = Scrollbar(textFrame)
        verScroll.pack(side=RIGHT, fill=Y)

        horScroll = Scrollbar(textFrame, orient='horizontal')
        horScroll.pack(side=BOTTOM, fill=X)

        self.text = Text(textFrame, width=97, height=25, font=("Helvetica", 16), selectbackground="black", selectforeground="white", undo=True, yscrollcommand=verScroll.set, wrap="none", xscrollcommand=horScroll.set)
        self.text.pack()

        # Configure our Scrollbar
        verScroll.config(command= self.text.yview)
        horScroll.config(command= self.text.xview)