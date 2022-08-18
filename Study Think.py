from tkinter import *
from study.menubar import MenuBar
from study.study import Study

root = Tk()
root.title("Study Think")

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2) - 50

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)

study = Study(root)
menubar = MenuBar(root, study)

root.mainloop()