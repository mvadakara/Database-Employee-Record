import mysql.connector
from faker import Faker 
import random


fake = Faker()
# Define your connection parameters
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Kek977977!",
    database="hr_system"
)

# Instantiate a cursor
mycursor = mydb.cursor()






print("Number where none appears")
mycursor.execute("select count(degree) from qualification where degree = 'None'")

for x in mycursor:
    print(x)
print()

print("number where BA appears")
mycursor.execute("select count(degree) from qualification where degree = 'BA'")

for x in mycursor:
    print(x)
print()


#Updating degree None to BA
mycursor.execute("Update qualification set degree = 'BA' where degree = 'None'")
mydb.commit()

for x in mycursor:
    print(x)
print()


print("new number for BA")
mycursor.execute("select count(degree) from qualification where degree = 'BA'")

for x in mycursor:
    print(x)
print()



"""


mycursor.execute("select emp_id, fname, lname, age from hr_system.employees where age = 100")

for x in mycursor:
    print(x)
print()

"""
print("employees where age = 100")
mycursor.execute("select count(emp_id) from hr_system.employees where age = 100")

for x in mycursor:
    print(x)

print()

"""
#selects all data from department
mycursor.execute("select * from department")

for x in mycursor:
    print(x)

print()
mycursor.execute("describe department")

for x in mycursor:
    print(x)

print()

"""

print("Manager 1")
### Query selects manager of department 1
mycursor.execute("select emp_id_dno, fname, lname, emp_id, dname from department, employees where dno = 1 and emp_id_dno = emp_id")
for x in mycursor:
    print(x)
print()


"""
### Selects all employees part of department 1
mycursor.execute("select dno, fname, lname, emp_id, dname from department, employees where dno_emp = dno and dno = 1")

for x in mycursor:
    print(x)
print()
"""

print("Manager 1 employees how many")
#counts the number of employees from department 1
mycursor.execute("select count(emp_id) from department, employees where dno_emp = dno and dno = 1")

for x in mycursor:
    print(x)
print()

print("Manager 2")
# selects manager of department 2
mycursor.execute("select emp_id_dno, fname, lname, emp_id, dname from department, employees where dno = 2 and emp_id_dno = emp_id")
for x in mycursor:
    print(x)
print()


""""
### Selects all employees part of department 2
mycursor.execute("select dno, fname, lname, emp_id, dname from department, employees where dno_emp = dno and dno = 2")

for x in mycursor:
    print(x)
print()
"""


#counts the number of employees from department 2
print("Manager 2 employees how many")
mycursor.execute("select count(emp_id) from department, employees where dno_emp = dno and dno = 2")

for x in mycursor:
    print(x)
print()

# selects manager of department 3
print("Manager 3")
mycursor.execute("select emp_id_dno, fname, lname, emp_id, dname from department, employees where dno = 3 and emp_id_dno = emp_id")
for x in mycursor:
    print(x)
print()

"""
### Selects all employees part of department 3
mycursor.execute("select dno, fname, lname, emp_id, dname from department, employees where dno_emp = dno and dno = 3")

for x in mycursor:
    print(x)
print()
"""


print("Manager 3 employees how many")
#counts the number of employees from department 3
mycursor.execute("select count(emp_id) from department, employees where dno_emp = dno and dno = 3")

for x in mycursor:
    print(x)
print()

print("combined salary of all employees")
#total number of money spent for employees salary
mycursor.execute("select sum(salary) from employees")

for x in mycursor:
    print(x)
print()


#total average for employees salary
print("average salary of employees")
mycursor.execute("select avg(salary) from employees")

for x in mycursor:
    print(x)
print()

print("salary of all employees under DNO 1")
#total number of money spent for employees salary for department 1
mycursor.execute("select sum(salary) from employees, department where DNO_emp = DNO and emp_id = emp_id_DNO and DNO = 1")

for x in mycursor:
    print(x)
print()

print("salary of all employees under DNO 2")
#total number of money spent for employees salary for department 2
mycursor.execute("select sum(salary) from employees, department where DNO_emp = DNO and emp_id = emp_id_DNO and DNO = 2")

for x in mycursor:
    print(x)
print()

print("salary of all employees under DNO 3")
#total number of money spent for employees salary for department 3
mycursor.execute("select sum(salary) from employees, department where DNO_emp = DNO and emp_id = emp_id_DNO and DNO = 3")

for x in mycursor:
    print(x)
print()


print("average salary of all employees under DNO 1")
#total number of money spent for employees salary for department 1
mycursor.execute("select avg(salary) from employees, department where DNO_emp = DNO and emp_id = emp_id_DNO and DNO = 1")

for x in mycursor:
    print(x)
print()

mycursor.execute("describe project")

for x in mycursor:
    print(x)
print()


"""
### projects that each employee under department 1 works 
mycursor.execute("select pno, proj_name, dno_proj, fname, lname, dname, emp_id from employees, department, project where dno_proj = dno and dno_emp = dno and dno = 1")  #and emp_id = emp_id_dno



for x in mycursor:
    print(x)
print()
"""


#mycursor.execute("describe works_for")

print("all projects listed under department 1")
# all projects listed under department 1
mycursor.execute("select count(emp_id) from employees, department, project, works_for where emp_id_work_for = emp_id and dno_emp = dno and pno_works_for = pno and pno <= 26 and dno = 1")

for x in mycursor:
    print(x)
print()

print("all projects listed under department 2")
#all projects under department 2
mycursor.execute("select count(emp_id) from employees, department, project, works_for where emp_id_work_for = emp_id and dno_emp = dno and pno_works_for = pno and pno <= 26 and dno = 2")
for x in mycursor:
    print(x)
print()

print("all projects listed under department 3")
#all projects under department 3
mycursor.execute("select count(emp_id) from employees, department, project, works_for where emp_id_work_for = emp_id and dno_emp = dno and pno_works_for = pno and pno <= 26 and dno = 3")






for x in mycursor:
    print(x)
print()



# sum of all hours of employees under department 1
print("# sum of all hours of employees under department 1")
mycursor.execute("select sum(hours) from employees, department, project, works_for where emp_id_work_for = emp_id and dno_emp = dno and pno_works_for = pno and pno <= 26 and dno = 1")

for x in mycursor:
    print(x)
print()

#lists project and hrs work for emp 1
print("#lists project and hrs work for emp 1")
mycursor.execute("select sum(hours), emp_id, fname, lname, pno, proj_name, dname from employees, department, project, works_for where emp_id_work_for = emp_id and dno_emp = dno and pno_works_For = pno and pno <= 26 and emp_id = 1")



for x in mycursor:
    print(x)
print()

# Select information about dependent and employee where emp_id = 1
print("# Select information about dependent and employee where emp_id = 1")
mycursor.execute("select * from dependent, employees where emp_id_dependent = emp_id and emp_id = 1")

for x in mycursor:
    print(x)
print()

print("emp_id dependent where emp_id = 10000")
mycursor.execute("select * from dependent where  emp_id_dependent = 10000")

for x in mycursor:
    print(x)
print()

"""
mycursor.execute("select * from dependent")

for x in mycursor:
    print(x)
print()

mycursor.execute("describe qualification")

for x in mycursor:
    print(x)
print()
"""

print("select emp_id where 10000")
mycursor.execute("select * from employees where emp_id = 10000")

for x in mycursor:
    print(x)
print()

mycursor = mydb.cursor()

sql = "UPDATE employees SET fname = %s, lname = %s WHERE emp_id = %s"
val = ("Marvin", "Gaye", 10000)

mycursor.execute(sql, val)

mydb.commit()


print("new employee = 10000")
mycursor.execute("select * from employees where emp_id = 10000")

for x in mycursor:
    print(x)
print()

mycursor.execute("describe employees")

for x in mycursor:
    print(x)
print()



"""
# Deletes all employees from NJ
mycursor.execute("select count(emp_id) from employees where state = 'NJ'")


for x in mycursor:
    print(x)
print()

sql = "DELETE FROM employees where state = 'NJ'"

mycursor.execute(sql)

mydb.commit()
"""


mycursor.execute("select count(emp_id) from employees")

for x in mycursor:
    print(x)
print()

mycursor.execute("select count(emp_id) from employees where state = 'NJ'")

for x in mycursor:
    print(x)
print()


mycursor.execute("select * from project")

for x in mycursor:
    print(x)
print()



mycursor.execute("select count(pno) from project")

for x in mycursor:
    print(x)
print()

# deletes projects greater than 10
sql = "Delete from project where pno > 10"

mycursor.execute(sql)

mydb.commit()

mycursor.execute("select * from project")

for x in mycursor:
    print(x)
print()

mycursor.execute("select count(pno) from project")

for x in mycursor:
    print(x)
print()


mycursor.execute("select count(emp_id) from employees, department where DNO_emp = DNO and DNO = 3")

for x in mycursor:
    print(x)
print()

"""
#Deletes all values associated with Research
sql = "DELETE FROM department WHERE dname = %s"
adr = ("Research", )

mycursor.execute(sql, adr)

mydb.commit()

"""

mycursor.execute("select count(emp_id) from employees, department where DNO_emp = DNO and DNO = 3")

for x in mycursor:
    print(x)
print()

mycursor.execute("select count(emp_id) from employees ")

for x in mycursor:
    print(x)
print()



mycursor.execute("select count(emp_id) from employees where state = 'NJ'")

for x in mycursor:
    print(x)
print()

#Update values CO to NJ


sql = "Update employees set state = %s where state = %s"
val = ("NJ", "CO")

mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("select count(emp_id) from employees where state = 'NJ'")

for x in mycursor:
    print(x)
print()

mycursor.execute("select DNO, emp_id, fname, lname, dname from department, employees where emp_id = emp_id_DNO and dno <= 4")

for x in mycursor:
    print(x)
print()

sql = "Update department, employees set emp_id_DNO = %s where emp_id = emp_id_DNO and emp_id_DNO = %s"
val = (10000,  1)

mycursor.execute(sql, val)

mydb.commit()


mycursor.execute("select DNO, emp_id, fname, lname, dname from department, employees where emp_id = emp_id_DNO and dno  <= 4")

for x in mycursor:
    print(x)
print()

mycursor.execute("select * from hr_system.employees where emp_id = 2")
for x in mycursor:
    print(x)
print()

mycursor.execute("describe employees")

for x in mycursor:
    print(x)
print()





sql = "Update employees set fname = %s, lname = %s, job_title = %s, street = %s, city = %s, email = %s, ssn = %s,  hire_date = %s where emp_id = %s"
val = (fake.first_name(), fake.last_name(), "Programmer", fake.street_name(), fake.city(), fake.email(), fake.ssn(), fake.date(), 2)

mycursor.execute(sql, val)

mydb.commit()

print("new employee for department heads")
mycursor.execute("select * from department, employees where emp_id = emp_id_dno and dno  <= 3")

for x in mycursor:
    print(x)
print()