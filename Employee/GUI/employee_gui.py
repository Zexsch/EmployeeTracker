from tkinter import StringVar, Tk, N, E, S, W
from tkinter import ttk
from GUI.Hourly.hourly_employee import HourlyEmployeeGUI
from GUI.Hourly.find_hourly_employee import FindHourlyEmployee
from GUI.Salary.salary_employee import SalaryEmployeeGUI
from GUI.Salary.find_salary_employee import FindSalaryEmployee
from GUI.delete_gui import DeletePanel
from Database.database import fetch_all_employees
from .find_edit import EditPanel

class GUI:
    def __init__(self):
        """GUI with all buttons necessary to modify and manage the database."""
        self.root = Tk()
        self.root.title('Employee')

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.hourly_id = StringVar()
        self.salary_id = StringVar()
    
    def create_hourly_employee_gui(self) -> None:
        self.hourly_gui = HourlyEmployeeGUI()
        self.hourly_gui.create_hourly_gui()
    
    def create_find_hourly_gui(self) -> None:
        self.find_hourly_gui = FindHourlyEmployee()
        self.find_hourly_gui.run_find_hourly_mainloop()
    
    def create_edit_gui(self) -> None:
        self.edit_hourly_gui = EditPanel()
        self.edit_hourly_gui.run_edit_mainloop()
    
    def create_salary_employee_gui(self) -> None:
        self.salary_gui = SalaryEmployeeGUI()
        self.salary_gui.create_salary_gui()
    
    def create_find_salary_gui(self) -> None:
        self.find_salary_gui = FindSalaryEmployee()
        self.find_salary_gui.run_find_salary_mainloop()
    
    def create_delete_gui(self) -> None:
        self.delete_gui = DeletePanel()
        self.delete_gui.run_delete_mainloop()
        
    def print_all_hourly_employees(self) -> None:
        """Print out all hourly employees to the console."""
        table = fetch_all_employees('HourlyTable')
        for i in table:
            # print(f'ID: {i[0]}, First Name: {i[1]}, Last Name: {i[2]}, Email: {i[3]}, Role: {i[4]}, Date: {i[5]}, HourlyPay: {i[6]}, HoursWorked: {i[7]}')
            print(i)
            
    def print_all_salary_employees(self) -> None:
        """Print out all salary employees to the console."""
        table = fetch_all_employees('SalaryTable')
        for i in table:
            # print(f'ID: {i[0]}, First Name: {i[1]}, Last Name: {i[2]}, Email: {i[3]}, Role: {i[4]}, Date: {i[5]}, Salary: {i[6]}')
            print(i)
        

    def run_mainloop(self):
        """Create the GUI."""
        #  hourly employee
        ttk.Button(self.mainframe, text='New Hourly Employee', command=self.create_hourly_employee_gui).grid(column=0, row=0, sticky=(W,E))
        ttk.Button(self.mainframe, text='Print All Hourly Employees', command=self.print_all_hourly_employees).grid(column=0, row=1, sticky=(W,E))
        ttk.Button(self.mainframe, text='Find Hourly Employees', command=self.create_find_hourly_gui).grid(column=0, row=2, sticky=(W,E))
        
        #  salary employee
        ttk.Button(self.mainframe, text='New Salary Employee', command=self.create_salary_employee_gui).grid(column=1, row=0, sticky=(W,E))
        ttk.Button(self.mainframe, text='Print All Salary Employees', command=self.print_all_salary_employees).grid(column=1, row=1, sticky=(W,E))
        ttk.Button(self.mainframe, text='Find Salary Employees', command=self.create_find_salary_gui).grid(column=1, row=2, sticky=(W,E))
        
        #  general
        ttk.Button(self.mainframe, text='Edit Employee', command=self.create_edit_gui).grid(column=0, row=3, sticky=(W,E))
        ttk.Button(self.mainframe, text='Delete Employee', command=self.create_delete_gui).grid(column=1, row=3, sticky=(W,E))
        
        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.root.mainloop()