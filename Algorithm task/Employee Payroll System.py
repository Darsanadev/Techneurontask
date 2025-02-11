import json

class BaseEmployee: # Base class
    def __init__(self, name, emp_id, role, basic_pay, allowances, deductions):
        self.name = name
        self.emp_id = emp_id
        self.role = role
        self.basic_pay = basic_pay
        self.allowances = allowances
        self.deductions = deductions
    
    # Base salary 
    def salary(self):
        salary = self.basic_pay + self.allowances - self.deductions
        print(salary)


# Manager class inherit from Baseclass using override
class Manager(BaseEmployee): 
    def __init__(self, name, emp_id, role, basic_pay, allowances, deductions, gender):
        super().__init__(name, emp_id, role, basic_pay, allowances, deductions)
        self.gender = gender

    def display(self):
        print(self.name, self.emp_id, self.gender, self.allowances)

    def salary(self, bonus=500):  # Adding bonus to manager salary
        return super().salary() + bonus

    def salary(self, bonus):
        return super().salary()
    
mngr = Manager("Alexa", 101, "Manager", 2000, 1000, 500, "female")
mngr.display()
mngr.salary(1000)


# Developer class 
class Developer(BaseEmployee):
    def __init__(self, name, emp_id, role, basic_pay, allowances, deductions):
        super().__init__(name, emp_id, role, basic_pay, allowances, deductions)

devlpr = Developer("Darsh", 102, "Developer", 5000, 1000, 500)
devlpr.salary()


# Intern class and override the salary()
class Intern(BaseEmployee):
    def __init__(self, name, emp_id, role, basic_pay, allowances, deductions):
        super().__init__(name, emp_id, role, basic_pay, allowances, deductions)

    def salary(self):
        salary = self.basic_pay
        print(salary)

intrn = Intern("Aishu", 103, "Intern", 20000, 0, 0)
intrn.salary()


# Employee class to show the details you want
class Employee(BaseEmployee):
    employees=[]
    
    def add_employee(self):
        self.name = input("Enter Name: ")
        self.emp_id = int(input("Employee id : "))
        self.role = input("Role: ")
        self.basic_pay = int(input("Basic pay salary : "))
        self.allowance = int(input("Allowance : "))
    

    employee_data = BaseEmployee(name, emp_id, role, basic_pay, allowance)
    employee_data.add_employee()
    employees.append(employee_data)
    print("Employee SUccessfully addedd :)")

    def display_employee(self, ):
        if not employees:
            print("NO Employee heree :( ")
        else:
            print(f"Employee List: \n  ID: {emp_id}, Name: {name}, Role: {role}, Salary: {salary}" ) 
        # print(f"Name: {self.name}, Employee id: {self.emp_id}, Role: {self.role}, Basic pay: {self.basic_pay}, Allowance: {self.allowance}")

    def payroll_list(self):
        while True:
            print("1. Add Employee ")
            print("2. Display Employee")
            print("3. Salary")
            print("4. Exit")
            choice = input("Enter You wann : ")

            if choice=="1":
                empl.add_employee()
                break
            elif choice == "2":
                empl.display_employee()
                break
            elif choice == "3":
                empl.display_salary()
                break
            elif choice == '4':
                print('Exit Successfully..!')
                break
            else:
                print("Invalid choice. Please try again!")
            
emp = "Darshu", 201, "Developer", 50000, 500,0
empl = Employee()
empl.payroll_list()




