from tkinter import StringVar, W, E
from tkinter import ttk
from GUI.popup import Popup
from Database.database import fetch_employee_by_name
from Database.database import fetch_employee_by_value
from Enumerators.tables import Tables
from GUI.GUI_base import GUIBase

class FindHourlyEmployee(GUIBase):
    def __init__(self):
        super().__init__()
        self.root.title('Find Hourly Employee')
        
        self.name = StringVar()
        self.id = StringVar()
        self.hourly_pay = StringVar()
        self.hours_worked_sv = StringVar()
        self.date = StringVar()
        
    def print_res(self, res: list) -> None:
        if not res:
            Popup('No Employees found.').show_popup()
            return
        
        for i in res:
            print(i)
            
    def find_employee_by_name(self) -> None:
        full_name = self.name.get().split(' ')
        res = fetch_employee_by_name(full_name, Tables.HOURLYTABLE.value)
        self.print_res(res)
    
    def find_employee_by_id(self) -> None:
        try:
            int(self.id.get())
        except ValueError:
            Popup('Please enter a valid ID.').show_popup()
            return
        
        res = fetch_employee_by_value('id', int(self.id.get()), Tables.HOURLYTABLE.value)
        self.print_res(res)
    
    def find_employee_by_hourly_pay(self) -> None:
        try:
            float(self.hourly_pay.get())
        except ValueError:
            Popup('Please enter a valid Pay.').show_popup()
            return
        
        res = fetch_employee_by_value('HourlyPay', float(self.hourly_pay.get()), Tables.HOURLYTABLE.value)
        self.print_res(res)
    
    def find_employee_by_hours_worked(self) -> None:
        try:
            float(self.hours_worked_sv.get())
        except ValueError:
            Popup('Please enter a valid amount of hours worked.').show_popup()
            return
        
        res = fetch_employee_by_name('HoursWorked', float(self.hours_worked_sv.get()), Tables.HOURLYTABLE.value)
        self.print_res(res)

    def run_find_hourly_mainloop(self) -> None:
        ttk.Label(self.frame, text='Find Employee by name').grid(column=0, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.name).grid(column=0, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.find_employee_by_name).grid(column=0, row=3, sticky=(E,W))
        
        ttk.Label(self.frame, text='Find Employee by Database ID').grid(column=1, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.id).grid(column=1, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.find_employee_by_id).grid(column=1, row=3, sticky=(E,W))
        
        ttk.Label(self.frame, text='Find Employee by Hourly Pay').grid(column=2, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.hourly_pay).grid(column=2, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.find_employee_by_hourly_pay).grid(column=2, row=3, sticky=(E,W))
        
        ttk.Label(self.frame, text='Find Employee by Hours Worked').grid(column=3, row=1, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.hourly_pay).grid(column=3, row=2, sticky=(E,W))
        ttk.Button(self.frame, text='Submit', command=self.find_employee_by_hours_worked).grid(column=3, row=3, sticky=(E,W))
        
        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)