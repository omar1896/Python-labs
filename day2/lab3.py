#!/usr/bin/env python3
import mysql.connector
from mysql.connector import errorcode



class Employee:



    all_employee = []
    db_config = {'user': 'root',
                 'password': '1896',
                 'host': '127.0.0.1',
                 'database': 'employee'
                 }
    



    def __init__(self, first_name, last_name, age, department, salary):
        # assign values to instance variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

        # add new object in list of employees
        self.all_employee.append(self)
        print(self.all_employee)

        self.insert_into_db()





    def insert_into_db(self):
        try:
            cnx = self.connect_to_mysql()
            cursor = cnx.cursor()
            cursor.execute(f"insert into `employee` (`first_name`,`last_name`,`age`,`department`,`salary`) VALUES (%s, %s, %s, %s, %s)",
                           (self.first_name, self.last_name, self.age, self.department, self.salary))
           
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
            cnx.close()





    def connect_to_mysql(self):
        try:
            cnx = mysql.connector.connect(**Employee.db_config)
            print(cnx)
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)




  
    def transfer(self, dep, name):

        cnx = self.connect_to_mysql()
        cursor = cnx.cursor()
        self.department = dep
        cursor.execute(
            f'Update employee set department=%s where first_name=%s', (dep, self.first_name))
        cnx.commit()
        cnx.close




    def fire(self):
        cnx = self.connect_to_mysql()
        cursor = cnx.cursor()
        if self in self.all_employee:
       
            cursor.execute(
                "delete from employee where first_name = %s", (self.first_name,))
            cnx.commit()
            cnx.close()



    def print_employee_details(self):
        """
      Prints the employee's details.
      """
        print("Employee:", Employee.all_employee)
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Salary:", self)

    def get_employee(self):
        return self


# emp2 = Employee("omar", "alaa", 25, "bio", 2000)
# print(Employee.all_employee)



class Manager(Employee):

    managed_department = ""

    def __init__(self, first_name, last_name, age, department, salary):
        super().__init__(first_name, last_name, age, department, salary)
        # self.insert_into_db()




    def print_employee_details(self):
        """
      Prints the employee's details.
      """
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", "hidden")


    def insert_into_db(self):
        try:
            cnx = self.connect_to_mysql()
            cursor = cnx.cursor()
            cursor.execute(f"insert into `employee` (`first_name`,`last_name`,`age`,`department`,`salary`,`managed_department`) VALUES (%s, %s, %s, %s, %s, %s)",
                           (self.first_name, self.last_name, self.age, self.department, self.salary, self.department))
            # print(cursor)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
            cnx.close()


# manager = Manager("ali","alaa",25,"bio")
# manager.print_employee_details()

flag = True
while(flag):



 user_input = input("""WELCOME :
                TO add user enter add-e
                TO add Manager enter add-m
                TO exit enter q
                """)

 if user_input=='q':
    flag=False  
 
 



 if user_input == 'add-e':
    fname = input("enter employee name:")
    lname = input("enterlast name:")
    age = input("enter age:")
    department = input("enter department:")
    salary = input("enter salary:")
    new_emp = Employee(fname, lname, age, department, salary)




if user_input == "add-m":
    fname = input("enter  name:")
    lname = input("enterlast name:")
    age = input("enter age:")
    department = input("enter department:")
    salary = input("enter salary:")
    new_emp = Manager(fname, lname, age, department, salary)





