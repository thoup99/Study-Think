from tkinter import *

class Gui:
    def __init__(self, root: Tk, study) -> None:
        self.root = root

        self.black = "#000000"
        self.gray = "#F2F2F2"
        self.red = "#EE0F0F"
        self.green = "#93FF59"

        questionFont = ("Helvetica", 20)
        setNameFont = ("Helvetica", 16)
        Font = ("Helvetica", 12)

        self.setName = Label(root, text= "Load or import a set.", font= setNameFont)
        self.question = Label(root, text= "Question", font= questionFont, wraplength= 570)

        self.answerButtons = []
        self.answerButtons.append(Button(root, text= "Answer 1" , font= Font, wraplength= 270, command= lambda: study.logic.checkCorrectness(0), disabledforeground= self.black, state= DISABLED))
        self.answerButtons.append(Button(root, text= "Answer 2", font= Font, wraplength= 270, command= lambda: study.logic.checkCorrectness(1), disabledforeground= self.black, state= DISABLED))
        self.answerButtons.append(Button(root, text= "Answer 3", font= Font, wraplength= 270, command= lambda: study.logic.checkCorrectness(2), disabledforeground= self.black, state= DISABLED))
        self.answerButtons.append(Button(root, text= "Answer 4", font= Font, wraplength= 270, command= lambda: study.logic.checkCorrectness(3), disabledforeground= self.black, state= DISABLED))

        root.columnconfigure(0, minsize= 300)
        root.columnconfigure(1, minsize= 300)

        root.rowconfigure(0, minsize= 50)
        root.rowconfigure(1, minsize= 150)
        root.rowconfigure(2, minsize= 100)
        root.rowconfigure(3, minsize= 100)

        self.setName.grid(column=0, columnspan= 2, sticky=E+W)
        self.question.grid(column=0, row= 1, columnspan= 2, sticky=E+W)

        self.answerButtons[0].grid(column=0, row= 2, sticky=N+E+S+W)
        self.answerButtons[1].grid(column=1, row= 2, sticky=N+E+S+W)
        self.answerButtons[2].grid(column=0, row= 3, sticky=N+E+S+W)
        self.answerButtons[3].grid(column=1, row= 3, sticky=N+E+S+W)