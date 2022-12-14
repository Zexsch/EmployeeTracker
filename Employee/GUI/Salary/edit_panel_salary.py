from tkinter import StringVar, E, W
from tkinter import ttk
from GUI.GUI_base import GUIBase
from Database.database import update_info
from Database.database import fetch_employee_by_value
from Enumerators.tables import Tables
from Enumerators.roles import Roles
from GUI.popup import Popup

class SalaryEditPanel(GUIBase):
    def __init__(self, id):
        super().__init__()
        self.root.title('Edit Info')
        self.id = id
    
    def run_edit_panel(self) -> None:
        """Create the GUI."""
        self.employee_list = fetch_employee_by_value('id', self.id, Tables.SALARYTABLE.value)
        try:
            self.employee = self.employee_list[0]
        except IndexError:
            Popup(f'No Employee with ID {self.id} found.').show_popup()
            return
        
        self.new_first_name = StringVar(value=self.employee[1])
        self.new_last_name = StringVar(value=self.employee[2])
        self.new_email = StringVar(value=self.employee[3])
        self.new_role = StringVar(value=self.employee[4])
        self.new_date = StringVar(value=self.employee[5])
        self.new_salary = StringVar(value=self.employee[6])
        
        
        ttk.Label(self.frame, text='ID').grid(column=0, row=0, sticky=(E,W))
        ttk.Label(self.frame, text=self.id).grid(column=0, row=1, sticky=(E,W))
        
        ttk.Label(self.frame, text='First Name').grid(column=1, row=0, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.new_first_name).grid(column=1, row=1, sticky=(E,W))
        
        ttk.Label(self.frame, text='Last Name').grid(column=2, row=0, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.new_last_name).grid(column=2, row=1, sticky=(E,W))
        
        ttk.Label(self.frame, text='Email').grid(column=3, row=0, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.new_email).grid(column=3, row=1, sticky=(E,W))
        
        x = 0
        for i in Roles:
            ttk.Radiobutton(self.frame, text=i.name.capitalize(), variable=self.new_role, 
                            value=i.name).grid(column=x, row=2, sticky=(W,E))
            x += 1
        
        ttk.Label(self.frame, text='Salary').grid(column=4, row=0, sticky=(E,W))
        ttk.Entry(self.frame, textvariable=self.new_salary).grid(column=4, row=1, sticky=(E,W))
    
        def submit_edits():
            """Submit the new values given to the database."""
            if not self.new_first_name.get() or not self.new_last_name.get():
                Popup('Please insert a first and last name.').show_popup()
                return

            if not self.new_salary.get():
                Popup('Please insert a Salary.').show_popup()
                return

            if not self.new_role.get():
                Popup('Please select a role.').show_popup()
                return

            try:
                float(self.new_salary.get())
            except ValueError:
                Popup('Please insert a valid Salary.').show_popup()
                return
            
            update_info(Tables.SALARYTABLE.value, self.id, self.new_first_name.get(), 
                        self.new_last_name.get(), self.new_email.get(), None, None, self.new_salary.get())
            Popup('Successfully updated Employee.').show_popup()
        
        ttk.Button(self.frame, text='Submit New Values', 
                   command=submit_edits).grid(column=6, row=1, sticky=(W,E))
        
        self.grid_config()