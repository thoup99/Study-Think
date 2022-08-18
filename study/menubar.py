from tkinter import *
from tkinter.filedialog import askopenfilename
from study.study import Study
from importer.importer import Importer
import os

class MenuBar:
    def __init__(self, root: Tk, study: Study) -> None:
        self.root = root
        self.study = study

        menubar = Menu(root)

        file = Menu(menubar, tearoff= False)
        file.add_command(label= "Load", command= self.Load)
        file.add_command(label= "Import", command= self.Import)
        menubar.add_cascade(label= "File", menu= file)

        edit = Menu(menubar, tearoff= False)
        edit.add_command(label= "Swap Study Side", command= self.AnswerSwap)
        edit.add_command(label= "Restart", command= self.Restart)
        menubar.add_cascade(label= "Edit", menu= edit)

        root.config(menu= menubar)


    def Load(self):
        dir = os.getcwd() + "\\sets"
        fileName = askopenfilename(title= "Select Set", initialdir= dir, filetypes=[("Json Files", "*.json")])
        if fileName != '':
            self.study.logic.loadSet(fileName)

    def Import(self):
        Importer(self.root)

    def AnswerSwap(self):
        self.study.logic.answerSwap()

    def Restart(self):
        self.study.logic.restart()