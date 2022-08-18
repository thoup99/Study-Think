from .gui import Gui
import os
from tkinter.filedialog import asksaveasfilename

class Logic:
    def __init__(self, gui: Gui) -> None:
        self.gui = gui


    def save(self):
        inp = self.gui.text.get("1.0",'end-1c')
        #print(repr(text))

        dir = os.getcwd() + "\\sets"

        if not os.path.isdir(dir):
            os.mkdir(dir)

        saveTo = asksaveasfilename(title= "Enter Set Name", initialdir= dir, filetypes=[("Json Files", "*.json")])
        if saveTo != '':

            jsonString = '{\n\t"Questions": [\n'

            start = 0
            for x in range(0, inp.count("\n\n")):
                separator = inp.index("\t", start) #Tabs
                
                try:
                    end = inp.index("\n\n", start)     #Double newline
                except ValueError:
                    end = len(inp)


                v1 = inp[start:separator]
                v2 = inp[separator + 1:end]


                jsonString += f'\t\t["{v1}", "{v2}"],\n'

                start = end + 3

            jsonString = jsonString[:-2]

            jsonString += '\n\t]\n}'
            print(jsonString)

            print(saveTo[saveTo.rfind('/') + 1:])
            print(saveTo[-5:])
            if len(saveTo[saveTo.rfind('/') + 1:]) < 6 or saveTo[-5:] != '.json':
                saveTo += '.json'

            with open(saveTo, "w", encoding="utf-8") as file:
                file.write(jsonString)