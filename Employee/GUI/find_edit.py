from tkinter import StringVar, E, W
from tkinter import ttk
from GUI.GUI_base import GUIBase
from GUI.popup import Popup
from .Hourly.edit_panel_hourly import HourlyEditPanel
from .Salary.edit_panel_salary import SalaryEditPanel
from Enumerators.tables import Tables
from Database.database import fetch_employee_by_name

class EditPanel(GUIBase):
    def __init__(self):
        super().__init__()
        self.root.title('Find Employee to Edit')
        
        self.id = StringVar()
        self.name = StringVar()
        self.table = StringVar()
    
    def open_edit_panel(self) -> None:
        """Open the GUIs necessary to edit employee information in the database"""
        if self.table.get() == Tables.HOURLYTABLE.value:
            try:
                HourlyEditPanel(self.id.get()).run_edit_panel()
            except AttributeError:
                HourlyEditPanel(self.id).run_edit_panel()
        elif self.table.get() == Tables.SALARYTABLE.value:
            try:
                SalaryEditPanel(self.id.get()).run_edit_panel()
            except AttributeError:
                SalaryEditPanel(self.id).run_edit_panel()
        else:
            Popup('Please select a valid Employee type.').show_popup()
            return
        
    def edit_by_id(self) -> None:
        """Check the given ID and open the GUI."""
        try:
            int(self.id.get())
        except (ValueError, TypeError):
            Popup('Please insert a valid ID.').show_popup()
            return
        
        self.open_edit_panel()
        
    def edit_by_name(self) -> None:
        """Get the ID from the given name and open the GUI."""
        employee = fetch_employee_by_name(self.name.get().capitalize().split(' '), self.table.get())
        if employee:
            self.id = employee[0][0]
            self.open_edit_panel()
        else:
            Popup('Employee not found.').show_popup()
        
    def run_edit_mainloop(self) -> None:
        """Create the GUI."""
        ttk.Label(self.frame, text='Edit by ID').grid(column=0, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.id).grid(column=0, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit ID', command=self.edit_by_id).grid(column=0, row=4, sticky=(E,W))
        
        ttk.Label(self.frame, text='Edit by Name').grid(column=1, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.name).grid(column=1, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit Name', command=self.edit_by_name).grid(column=1, row=4, sticky=(E,W))
        
        ttk.Radiobutton(self.frame, text='Hourly', variable=self.table, value=Tables.HOURLYTABLE.value).grid(
            column=0, row=3, sticky=(E,W))
        ttk.Radiobutton(self.frame, text='Salary', variable=self.table, value=Tables.SALARYTABLE.value).grid(
            column=1, row=3, sticky=(E,W))
        
        self.grid_config()