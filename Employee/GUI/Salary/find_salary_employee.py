from tkinter import StringVar, E, W
from tkinter import ttk
from GUI.GUI_base import GUIBase
from Database.database import fetch_employee_by_name
from Database.database import fetch_employee_by_value
from Enumerators.tables import Tables
from GUI.popup import Popup

class FindSalaryEmployee(GUIBase):
    def __init__(self):
        super().__init__()
        self.root.title('Find Employee')
        
        self.name = StringVar()
        self.id = StringVar()
        self.salary = StringVar()
    
    def find_employee_by_name(self) -> None:
        """Print all employees that match the name given."""
        full_name = self.name.get().capitalize().split(' ')
        res = fetch_employee_by_name(full_name, Tables.SALARYTABLE.value)
        if not res:
            print('No Employees found.')
        else:
            for i in res:
                print(i)
    
    def find_employee_by_id(self) -> None:
        """Print all employees that match the ID given."""
        try:
            int(self.id.get())
        except ValueError:
            Popup('Please insert a valid ID.').show_popup()
            return
        
        res = fetch_employee_by_value('id', self.id.get(), Tables.SALARYTABLE.value)
        if not res:
            Popup('No Employees found.').show_popup()
        else:
            for i in res:
                print(i)
    
    def find_employee_by_salary(self) -> None:
        """Print all employees that match the salary given."""
        try:
            int(self.salary.get())
        except ValueError:
            Popup('Please insert a valid Salary.').show_popup()
            return
        
        res = fetch_employee_by_value('salary', self.salary.get(), Tables.SALARYTABLE.value)
        if not res:
            Popup('No Employees found.').show_popup()
        else:
            for i in res:
                print(i)
            
    def run_find_salary_mainloop(self):
        """Create the GUI."""
        ttk.Label(self.frame, text='Find Employee by name').grid(column=0, row=0, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.name).grid(column=0, row=1, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.find_employee_by_name).grid(column=0, row=2, sticky=(E,W))
        
        ttk.Label(self.frame, text='Find Employee by Database ID').grid(column=1, row=0, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.id).grid(column=1, row=1, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.find_employee_by_id).grid(column=1, row=2, sticky=(E,W))
        
        ttk.Label(self.frame, text='Find Employee by Salary').grid(column=2, row=0, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.salary).grid(column=2, row=1, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.find_employee_by_salary).grid(column=2, row=2, sticky=(E,W))
        
        self.grid_config()