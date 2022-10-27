from tkinter import W, E, Label
from GUI.GUI_base import GUIBase

class Popup(GUIBase):
    def __init__(self, message: str):
        super().__init__()
        self.message = message
        self.root.title(self.message)
    
    def show_popup(self) -> None:
        Label(self.frame, text=self.message).grid(column=0, row=0, sticky=(E,W))