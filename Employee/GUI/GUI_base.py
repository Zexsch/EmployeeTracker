from tkinter import Toplevel, N, W, E, S
from tkinter import ttk

class GUIBase:
    def __init__(self):
        """Base class for all GUI-related panels."""
        self.root = Toplevel()
        self.frame = ttk.Frame(self.root, padding="3 3 12 12")

        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
    
    def grid_config(self) -> None:
        """Pad all GUI widgets. Run function after all widgets are created in every GUI."""
        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)