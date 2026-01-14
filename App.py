import tkinter as tk
from ui import SubnetUI
from controller import SubnetController

if __name__ == "__main__":
    root = tk.Tk()
    ui = SubnetUI(root)
    SubnetController(ui)
    root.mainloop()
