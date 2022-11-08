from tkinter import StringVar, E, W
from tkinter import ttk
from GUI.GUI_base import GUIBase
from GUI.popup import Popup
from Enumerators.tables import Tables
from Database.database import fetch_employee_by_name
from Database.database import delete_employee
from Database.database import DeleteException

class DeletePanel(GUIBase):
    def __init__(self):
        super().__init__()
        self.root.title('Delete Employee')
        
        self.id = StringVar()
        self.name = StringVar()
        self.table = StringVar()
    
    def delete(self, id: int) -> None:
        """Delete the employee given from the database."""
        if self.table.get() == Tables.HOURLYTABLE.value or self.table.get() == Tables.SALARYTABLE.value:
            try:
                delete_employee(id, self.table.get())
            except DeleteException:
                Popup('Employee not found.').show_popup()
        else:
            Popup('Please select a valid table.').show_popup()
            
    def delete_by_id(self) -> None:
        """Get the ID and run the delete function."""
        try:
            int(self.id.get())
        except (ValueError, TypeError):
            Popup('Please insert a valid ID.').show_popup()
            return
        self.delete(self.id.get())
        
    def delete_by_name(self) -> None:
        """Get the ID via employee name and run the delete function."""
        employee = fetch_employee_by_name(self.name.get().capitalize().split(' '), self.table.get())
        if employee:
            self.delete(employee[0][0])
        else:
            Popup('Employee not found.').show_popup()
        
    def run_delete_mainloop(self) -> None:
        """Create the GUI."""
        ttk.Label(self.frame, text='Delete by ID').grid(column=0, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.id).grid(column=0, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit ID', command=self.delete_by_id).grid(column=0, row=4, sticky=(E,W))
        
        ttk.Label(self.frame, text='Delete by Name').grid(column=1, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.name).grid(column=1, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit Name', command=self.delete_by_name).grid(column=1, row=4, sticky=(E,W))
        
        ttk.Radiobutton(self.frame, text='Hourly', variable=self.table, value=Tables.HOURLYTABLE.value).grid(
            column=0, row=3, sticky=(E,W))
        ttk.Radiobutton(self.frame, text='Salary', variable=self.table, value=Tables.SALARYTABLE.value).grid(
            column=1, row=3, sticky=(E,W))
        
        self.grid_config()