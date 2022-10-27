from tkinter import StringVar, E, W
from tkinter import ttk
from GUI.GUI_base import GUIBase
from Database.database import fetch_employee_by_name
from Enumerators.tables import Tables

class FindSalaryEmployee(GUIBase):
    def __init__(self):
        super().__init__()
        self.root.title('Find Employee')
        
        self.name = StringVar()
    
    def find_employee_by_name(self) -> None:
        full_name = self.name.get().capitalize().split(' ')
        res = fetch_employee_by_name(full_name, Tables.SALARYTABLE.value)
        if not res:
            print('No Employees found.')
        for i in res:
            print(i)
    
    def run_find_salary_mainloop(self):
        ttk.Label(self.frame, text='Find Employee by name').grid(column=0, row=2, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.name).grid(column=0, row=3, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.find_employee_by_name).grid(column=0, row=4, sticky=(E,W))
        
        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)