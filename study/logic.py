from tkinter import NORMAL, DISABLED
from .gui import Gui
import random
import json

QUESTION = 0
ANSWER = 1

class Logic:
    def __init__(self, gui: Gui) -> None:
        self.gui = gui
        self.isLoaded = False

        self.questionNum = 0
        self.setName = "Set Name Here"
        self.totalQuestions = 0
        self.questions = []

        self.correctAnswerIndex = 0


    def loadSet(self, path):
        with open(path, "r", encoding="utf-8") as setData:
            loadedData = json.load(setData)["Questions"]

        last_slash = path.rfind("/")
        last_dot = path.rfind(".")

        self.setName = path[last_slash + 1:last_dot]
        
        self.questions = loadedData
        random.shuffle(self.questions)
        self.questionNum = 0
        self.totalQuestions = len(self.questions)

        self.isLoaded = True
        self.loadQuestion()



    def loadQuestion(self):
        answers = ["", "", "", ""]
        self.gui.question.config(text= self.questions[self.questionNum][QUESTION])  #Load Question text
        self.gui.setName.config(text= self.setName + ": " + str(self.questionNum) + " of " + str(self.totalQuestions))

        ##Generate 4 random answers
        for x in range(0, 4):
            randIndex = random.randrange(0, self.totalQuestions)
            while randIndex == self.questionNum or self.questions[randIndex][ANSWER] in answers:
                randIndex = random.randrange(0, self.totalQuestions)

            answers[x] = self.questions[randIndex][ANSWER]


        ##Put the correct answer in a random spot
        self.correctAnswerIndex = random.randint(0, 3)
        answers[self.correctAnswerIndex] = self.questions[self.questionNum][ANSWER]


        #Update all answer buttons
        for x in range(0, 4):
            self.gui.answerButtons[x].config(text= answers[x])

        self.unlockGUI()



    def checkCorrectness(self, index):
        self.displayAnswer()

        if index == self.correctAnswerIndex:
            self.questionNum += 1
        else:
            randomIndex = random.randint(self.questionNum, self.totalQuestions)
            self.questions.insert(randomIndex, self.questions.pop(self.questionNum))
        
        self.gui.setName.config(text= self.setName + ": " + str(self.questionNum) + " of " + str(self.totalQuestions))
        if self.questionNum != self.totalQuestions:
            self.gui.root.after(2000, self.loadQuestion)


    def displayAnswer(self):
        """Change the color of the gui and lock them"""
        for index, button in enumerate(self.gui.answerButtons, 0):
            if index == self.correctAnswerIndex:
                button.config(bg = self.gui.green, state= DISABLED)
                
            else:
                button.config(bg = self.gui.red, state= DISABLED)

    def unlockGUI(self):
        """Changes buttons back to normal color and unlocks"""
        for button in self.gui.answerButtons:
            button.config(bg = self.gui.gray, state= NORMAL)



    def answerSwap(self):
        if not self.isLoaded:
            return

        swappedArray = []

        for question in self.questions:
            qSet = []

            qSet.append(question[1])
            qSet.append(question[0])

            swappedArray.append(qSet)

        self.questions = swappedArray

        self.loadQuestion()

    
    def restart(self):
        if not self.isLoaded:
            return

        random.shuffle(self.questions)
        self.questionNum = 0

        self.loadQuestion()
        

    def printQnA(self):
        """Debug Function that prints the questions first then answers"""
        qArray = []
        aArray = []
        for question in self.questions:
            qArray.append(question[0])
            aArray.append(question[1])

        print(qArray)
        print(aArray)