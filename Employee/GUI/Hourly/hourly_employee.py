from tkinter import StringVar, W, E
from tkinter import ttk
from Database.database import insert_hourly_employee
from Enumerators.roles import Roles
from GUI.popup import Popup
from GUI.GUI_base import GUIBase

class HourlyEmployeeGUI(GUIBase):
    def __init__(self):
        super().__init__()
        self.root.title('Hourly Employee')
        
    def create_hourly_gui(self) -> None:
        """Create the GUI."""
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.hourly_pay_rate = StringVar()
        self.hours_worked = StringVar(value=0)
        self.role = StringVar()
        
        ttk.Label(self.frame, text='First Name').grid(column=0, row=0, sticky=(W,E))
        ttk.Entry(self.frame, width=20, textvariable=self.first_name).grid(column=0, row=1, sticky=(W,E))
        
        ttk.Label(self.frame, text='Last Name').grid(column=1, row=0, sticky=(W,E))
        ttk.Entry(self.frame, width=20, textvariable=self.last_name).grid(column=1, row=1, sticky=(W,E))
        
        ttk.Label(self.frame, text='Hourly Pay').grid(column=2, row=0, sticky=(W,E))
        ttk.Entry(self.frame, textvariable=self.hourly_pay_rate).grid(column=2, row=1, sticky=(W,E))
        
        ttk.Label(self.frame, text='Hours Worked').grid(column=3, row=0, sticky=(W,E))
        ttk.Entry(self.frame, textvariable=self.hours_worked).grid(column=3, row=1, sticky=(W,E))
        
        x = 0
        for i in Roles:
            ttk.Radiobutton(self.frame, text=i.name.capitalize(), variable=self.role, value=i.name).grid(column=x, row=3, sticky=(W,E))
            x += 1

        def submit_hourly_values() -> None:
            """Submit the values given to the database."""
            if not self.first_name.get() or not self.last_name.get():
                Popup('Please insert a first and last name.').show_popup()
                return
            
            if not self.hourly_pay_rate.get():
                Popup('Please insert an hourly pay rate.').show_popup()
                return
                
            if not self.role.get():
                Popup('Please select a role.').show_popup()
                return
            
            try:
                float(self.hourly_pay_rate.get())
                float(self.hours_worked.get())
            except ValueError:
                Popup('Please insert a valid number.').show_popup()
                return
            
            insert_hourly_employee(self.first_name.get(), self.last_name.get(), float(self.hourly_pay_rate.get()), float(self.hours_worked.get()), self.role.get())
            Popup('Successfully registered the new Employee.').show_popup()
        
        ttk.Button(self.frame, text='Submit', command=submit_hourly_values).grid(column=4, row=1, sticky=(W,E))
        
        self.grid_config()