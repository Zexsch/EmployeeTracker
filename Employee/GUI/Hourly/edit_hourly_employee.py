from tkinter import StringVar, E, W
from tkinter import ttk
from GUI.GUI_base import GUIBase
from GUI.popup import Popup
from .edit_panel_hourly import HourlyEditPanel

class EditHourlyEmployee(GUIBase):
    def __init__(self):
        super().__init__()
        self.root.title('Find Employee to Edit')
        
        self.id = StringVar()
    
    def edit_by_id(self) -> None:
        try:
            int(self.id.get())
        except ValueError:
            Popup('Please insert a valid ID.').show_popup()
            return
        
        HourlyEditPanel(self.id.get()).run_edit_panel()
    
    def run_edit_hourly_mainloop(self) -> None:
        ttk.Label(self.frame, text='Edit by ID').grid(column=0, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.id).grid(column=0, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.edit_by_id).grid(column=0, row=3, sticky=(E,W))
        
        self.grid_config()