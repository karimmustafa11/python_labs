import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost", user="root", password="2002", database="company")

cursor = mydb.cursor()
class Employee:
    employees = []

    @staticmethod
    def findEmp(id):
        for item in Employee.employees:
            if item.id == id:
                return item
        
        return None

    def __init__(self, fname, lname, age, department, salary):
        self.id = int(time.time())
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.department = department
        self.salary = salary 
        Employee.employees.append(self)
        query = 'INSERT INTO employees (id, first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s, %s)'
        data = (self.id, fname, lname, age, department, salary)
        cursor.execute(query, data)
        mydb.commit()
        print("User has been added successfully!")

    def transfer(self,id, new_department):
        old = ''
        emp = Employee.findEmp(id)
        if emp is not None:
            emp.department = new_department
            query = f'UPDATE employees SET department = "{new_department}" WHERE id = {id}'

            cursor.execute(query)
            mydb.commit()

            print(f"Department for {emp.first_name} has been changed from {old} to {new_department}")        
        else:
            print(f"There is no match for id = {id}")

    def fire(self, id):
        emp = Employee.findEmp(id)
        if emp is not None:
            Employee.employees.remove(emp)
            query = f'DELETE FROM employees WHERE id = "{emp.id}"'
            cursor.execute(query)
            mydb.commit()
            print("User has been deleted successfully")
        else:
            print(f"No match for id = {id}")

    def show(self, id):
        emp = Employee.findEmp(id)
        if emp is not None:
            print(f"First name: {emp.first_name}")
            print(f"Last name: {emp.last_name}")
            print(f"Age: {emp.age}")
            print(f"Department: {emp.department}")
            print(f"Salary: {emp.salary}")
            print("#####################")
        else:
            print(f"No match for id = {id}")

    def list_employees(self):
        print("Current Employees:")
        query = 'SELECT * From employees'
        cursor.execute(query)

        result = cursor.fetchall()
        for item in result:
            print (item)
     
class Manager(Employee):
    def __init__(self, fname, lname, age, department, salary, managed_dept):
        super().__init__(fname, lname, age, department, salary)
        self.managed_department = managed_dept
        query = f'UPDATE employees SET managed_department = "{managed_dept}" WHERE id = {self.id}'
        cursor.execute(query)
        mydb.commit()

    def show(self,id):
        emp = Employee.findEmp(id)
        if emp is not None:
            print(f"First name: {self.first_name}")
            print(f"Last name: {self.last_name}")
            print(f"Age: {self.age}")
            print(f"Department: {self.department}")
            print(f"Salary: ******")
            print(f"Managed Department: {self.managed_department}")
            print("#####################")
        else:
            print(f"No match for id = {id}")


operation =""
currentEmployee = None
while(not operation == 'q'):
    print("- (add) for adding new employee")
    print("- (transfer) to change the department of an employee")
    print("- (show) show current employee data")
    print("- (list) to list all employees data in the company")
    print("- (fire) to fire an employee from the company")
    print("- (q) to quit program")
    operation = input("Enter your operation: ")

    if operation == 'add':
        type = input('If manager press “m”/ if employee press ‘e’ ')
        print("Please insert data")
        fname = input("First Name >> ")
        lname = input("Last Name >> ")
        age = input("age >> ")
        department = input("department >> ")
        salary = input("salary >> ")

        if type == 'm':
            managed_department = input('Managed Department >> ')
            currentEmployee = Manager(fname, lname, age, department, salary, managed_department)
        else:
            currentEmployee = Employee(fname, lname, age, department, salary)
    elif operation == 'transfer':
        currentEmployee.list_employees()
        id = int(input("Enter the id of the employee >> "))
        newDept = input("Enter the new department >> ")
        currentEmployee.transfer(id, newDept)
    elif operation == 'show':
        currentEmployee.list_employees()
        id = int(input("Enter the id of the employee >> "))
        currentEmployee.show(id)
    elif operation == 'list':
        currentEmployee.list_employees()
    elif operation == 'fire':
        currentEmployee.list_employees()
        id = int(input("Enter the id of the employee >> "))
        currentEmployee.fire(id)
    elif operation == 'q':
        pass
    else:
        print("Enter a valid operation!")
        

