from tkinter import W, E, Label
from GUI.GUI_base import GUIBase

class Popup(GUIBase):
    def __init__(self, message: str):
        """Open up a popup GUI for alerts."""
        super().__init__()
        self.message = message
        self.root.title(self.message)
    
    def show_popup(self) -> None:
        """Create the Popup GUI."""
        Label(self.frame, text=self.message).grid(column=0, row=0, sticky=(E,W))