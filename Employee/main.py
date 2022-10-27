from Database.database import initialise_tables
from GUI.employee_gui import GUI

def main():
    initialise_tables()
    GUI().run_mainloop()
    
if __name__ == '__main__':
    main()