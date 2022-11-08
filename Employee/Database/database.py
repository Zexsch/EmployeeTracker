import sqlite3
from datetime import date
from Enumerators.tables import Tables
from Enumerators.company import Databases
from Enumerators.company import Company
from pathlib import PurePath
from enum import Enum

PATH = PurePath(__file__).parent / Databases.EMPLOYEEDB.value

def initialise_tables() -> None:
    """Initialise all DB tables."""
    with sqlite3.connect(PATH) as con:
        cur = con.cursor()
        try:
            cur.execute(f'CREATE TABLE {Tables.HOURLYTABLE.value}(id INTEGER PRIMARY KEY, FirstName, LastName, Email, Role, Date, HourlyPay REAL, HoursWorked REAL)')
            cur.execute(f'CREATE TABLE {Tables.SALARYTABLE.value}(id INTEGER PRIMARY KEY, FirstName, LastName, Email, Role, Date, Salary REAL)')
        except sqlite3.OperationalError:
            pass

def insert_hourly_employee(first_name: str, last_name: str, hourly_pay_rate: float, 
                           hours_worked: float, role: Enum) -> None:
    """Insert a new hourly employee into the database."""
    email = f'{first_name}.{last_name}@{Company.COMPANY_NAME.value}.com'
    today = date.today()
    with sqlite3.connect(PATH) as con:
        cur = con.cursor()
        
        cur.execute(f'INSERT INTO {Tables.HOURLYTABLE.value}(FirstName, LastName, Email, Role, Date, HourlyPay, HoursWorked) VALUES(?,?,?,?,?,?,?)', 
                    (first_name.capitalize(), last_name.capitalize(), email, role, today, hourly_pay_rate, hours_worked))

def insert_salary_employee(first_name: str, last_name: str, salary: float, role: Enum) -> None:
    """Insert a new salary employee into the database."""
    email = f'{first_name}.{last_name}@{Company.COMPANY_NAME.value}.com'
    today = date.today()
    with sqlite3.connect(PATH) as con:
        cur = con.cursor()
        
        cur.execute(f'INSERT INTO {Tables.SALARYTABLE.value}(FirstName, LastName, Email, Role, Date, Salary) VALUES(?,?,?,?,?,?)', 
                    (first_name.capitalize(), last_name.capitalize(), email, role, today, salary))
        
def fetch_all_employees(table: str) -> list:
    """Fetch all employees in a table in the database."""
    with sqlite3.connect(PATH) as con:
        cur = con.cursor()
        
        res = cur.execute(f'SELECT * FROM {table}').fetchall()
        return res

def fetch_employee_by_name(full_name: str, table: str) -> list:
    """Return a list of all employees that match the given name."""
    with sqlite3.connect(PATH) as con:
        cur = con.cursor()
        
        try:
            first_name = full_name[0].capitalize()
            last_name = full_name[1].capitalize()
            res = cur.execute(f'SELECT * FROM {table} WHERE FirstName=:first_name AND LastName=:last_name', 
                              {'first_name': first_name, 'last_name': last_name})
            
            return res.fetchall()
        except IndexError:
            name = full_name[0].capitalize()
            res = cur.execute(f'SELECT * FROM {table} WHERE FirstName=:name', {'name': name}).fetchall()
            
            if not res:
                res = cur.execute(f'SELECT * FROM {table} WHERE LastName=:name', {'name': name}).fetchall()
                
            return res

def fetch_employee_by_value(key: str, value: str | int, table: str) -> list:
    """Return a list of all employees that match the given key:value pair."""
    with sqlite3.connect(PATH) as con:
        cur = con.cursor()
        
        res = cur.execute(f'SELECT * FROM {table} WHERE {key}=?', (value,))
        return res.fetchall()

def update_info(table: str, id: int,  first_name: str, last_name: str, email: str, hourly_pay: int | None,
                hours_worked: int | None, salary: int | None) -> None:
    """Update employee info in the database."""
    with sqlite3.connect(PATH) as con:
        cur = con.cursor()
        
        if salary is None:
            cur.execute(f'UPDATE {table} SET FirstName=?, LastName=?, Email=?, HourlyPay=?, HoursWorked=? WHERE id=?', 
                        (first_name,last_name,email,hourly_pay,hours_worked,id))
        else:
            cur.execute(f'UPDATE {table} SET FirstName=?, LastName=?, Email=?, Salary=?, WHERE id=?', 
                        (first_name,last_name,email,salary,id))

class DeleteException(Exception):
    """Throw an Exception when the ID is out of range."""
    pass

def delete_employee(id: int, table: str) -> None:
    """Remove an employee from the database."""
    with sqlite3.connect(PATH) as con:
        cur = con.cursor()
        
        res = cur.execute(f'SELECT * FROM {table} WHERE id=?', (id,)).fetchall()
        if res:
            cur.execute(f'DELETE FROM {table} WHERE id=?', (id,))
        else:
            raise DeleteException