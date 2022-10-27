from tkinter import StringVar, W, E
from tkinter import ttk
from GUI.popup import Popup
from Enumerators.roles import Roles
from Database.database import insert_salary_employee
from GUI.GUI_base import GUIBase

class SalaryEmployeeGUI(GUIBase):
    def __init__(self):
        super().__init__()
        self.root.title('Salary Employee')
        
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.salary_pay_rate = StringVar()
        self.role = StringVar()
        
    def create_salary_gui(self) -> None:
        ttk.Label(self.frame, text='First Name').grid(column=0, row=0, sticky=(W,E))
        ttk.Entry(self.frame, width=20, textvariable=self.first_name).grid(column=0, row=1, sticky=(W,E))
        
        ttk.Label(self.frame, text='Last Name').grid(column=1, row=0, sticky=(W,E))
        ttk.Entry(self.frame, width=20, textvariable=self.last_name).grid(column=1, row=1, sticky=(W,E))
        
        ttk.Label(self.frame, text='Salary').grid(column=2, row=0, sticky=(W,E))
        ttk.Entry(self.frame, textvariable=self.salary_pay_rate).grid(column=2, row=1, sticky=(W,E))
        
        x = 0
        for i in Roles:
            ttk.Radiobutton(self.frame, text=i.name.capitalize(), variable=self.role, value=i.name).grid(column=x, row=2, sticky=(W,E))
            x += 1
        
        
        def submit_salary_values() -> None:
            if not self.first_name.get() or not self.last_name.get():
                Popup('Please insert a first and last name.').show_popup()
                return
                
            if not self.salary_pay_rate.get():
                Popup('Please insert a salary pay rate.').show_popup()
                return
            
            if not self.role.get():
                Popup('Please select a role.').show_popup()
                return
            
            try:
                float(self.salary_pay_rate.get())
            except ValueError:
                Popup('Please insert a valid pay rate.').show_popup()
                return
            
            insert_salary_employee(self.first_name.get(), self.last_name.get(), float(self.salary_pay_rate.get()), self.role.get())
            Popup('Successfully added the Employee.').show_popup()
            
        
        ttk.Button(self.frame, text='Submit', command=submit_salary_values).grid(column=3, row=1, sticky=(W,E))
        
        self.grid_config()
        
        self.root.mainloop()