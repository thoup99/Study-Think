from tkinter import *
from .gui import Gui
from .logic import Logic
from .menubar import MenuBar

class Importer:
    def __init__(self, main_root) -> None:

        root = Toplevel(main_root)
        root.title("Study Think Importer")

        window_width = 600
        window_height = 400

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2) - 50

        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        root.resizable(False, False)

        self.menubar = MenuBar(root, self)
        self.gui = Gui(root)
        self.logic = Logic(self.gui)