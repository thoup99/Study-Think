from tkinter import *

class MenuBar:
    def __init__(self, root: Tk, importer) -> None:
        self.root = root
        self.importer = importer

        menubar = Menu(root)


        file = Menu(menubar, tearoff= False)
        file.add_command(label= "Import As", command= self.save)
        menubar.add_cascade(label= "File", menu= file)

        help = Menu(menubar, tearoff= False)
        help.add_command(label= "Open Import Instructions", command= self.openHelp)
        menubar.add_cascade(label= "Help", menu= help)

        root.config(menu= menubar)

    def save(self):
        self.importer.logic.save()

    def openHelp(self):
        new_root = Toplevel(self.root)
        new_root.title("Study Think Importer Help")

        window_width = 300
        window_height = 200

        screen_width = new_root.winfo_screenwidth()
        screen_height = new_root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2) - 50

        new_root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        Label(new_root, wraplength= 280, justify= LEFT, text= 'Find a quizlet set and press the the dots next to the share button.\nSelect Export\nUnder between term and definition select "Tabs".\nSelect Custom for between rows. Set custom to "\\n\\n".\nPress "Copy Text"\nPaste text into the importer.\nPress File then "Import As"\nName the file and save.').pack(side= TOP, anchor= W)

        #root.resizable(False, False)
    