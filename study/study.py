from tkinter import *
from .gui import Gui
from .logic import Logic

class Study:
    def __init__(self, root) -> None:
        self.gui = Gui(root, self)
        self.logic = Logic(self.gui)
