import mysql.connector
from faker import Faker 
import random

fake = Faker()

states = ["AL", "AK", "AZ", "AR", "CA", "CO", 
"CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN",
"IA", "KS", "KY","LA", "ME", "MD", "MA", "MI",
"MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
 "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
"RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA",
"WA", "WV", "WI", "WY"
]
### Selects random state
def random_state():
    state_choice = random.choice(states)
    return state_choice




#selects random salary 
def random_salary():
    salary_list = random.randint(10000, 1000000)
    return salary_list

# selects random phone_number
def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

#selects random zip
def random_zip_generator():
    first = str(random.randint(0, 9))
    second = str(random.randint(0, 9))
    third = str(random.randint(0, 9))
    fourth = str(random.randint(0, 9))
    fifth = str(random.randint(0, 9))
    return '{}{}{}{}{}'.format(first, second, third, fourth, fifth)



# Selects random gender
def random_gender():
    gender_list = ["M", "F", "N"]
    gender = random.choice(gender_list)
    return gender

#Selects random department number
def dept_num():
    dno_numb = [1, 2, 3]
    dno_choice = random.choice(dno_numb)
    return dno_choice

#Select random age 
def age_num():
    age = random.randint(18, 100)
    return age

#Selects random degree
def random_degree():
    degree_list = ["PHD", "MS", "BA", "BS", "MD", "None"]
    degree_choice = random.choice(degree_list)
    return degree_choice

def random_hour():
    hour = random.randrange(20, 1000)
    return hour

def random_proj_num():
    proj = random.randrange(1, 26)
    return proj

def random_proj_name():
    proj_list = ["ProductA", "ProductB","ProductC","ProductD","ProductE","ProductF","ProductG","ProductH","ProductI","ProductJ","ProductK","ProductL",
    "ProductM","ProductN","ProductO","ProductP","ProductQ","ProductR","ProductS","ProductT","ProductU","ProductV","ProductW","ProductX",
    "ProductY","ProductZ"]
    proj_choice = random.choice(proj_list)
    return proj_choice

def random_relationship_choice():
    relation_list =["Son", "Mother", "Father", "Daughter"]
    relation = random.choice(relation_list)
    return relation

def random_university_choice():
    result = fake.state() + " University"
    return result


# Define your connection parameters
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Kek977977!",
    database="hr_system"
)

# Instantiate a cursor
mycursor = mydb.cursor()
"""
mycursor.execute("Drop database hr_system")

for x in mycursor:
    print(x)

mycursor.execute("CREATE DATABASE hr_system")

"""

#mycursor.execute("SHOW DATABASES")
#mycursor.execute("drop table project")
#mycursor.execute("alter table department drop constraint FK_SSN")
#mycursor.execute("ALTER TABLE department DROP constraint FK_EMP_ID")
#mycursor.execute("Alter table employees drop constraint FK_DNO")
#mycursor.execute("Drop table department")
#mycursor.execute("DROP Table employees")
#mycursor.execute("drop table dependent")
#mycursor.execute("drop table qualification")

# Creating employees table

mycursor.execute("CREATE TABLE employees (EMP_ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY, fname varchar(20) not null, lname varchar(20) not null, job_title varchar(100), salary INT, street varchar(100) NOT NULL, city varchar(50) NOT NULL, state varchar(2) NOT NULL, zip varchar(10) not null,  hire_date date NOT NULL, age INT NOT NULL, emp_phone varchar(40) not null, gender ENUM ('M', 'F', 'N') not null)")


mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

print()

mycursor.execute("describe employees")

for x in mycursor:
    print(x)


print()
mycursor.execute("Alter table employees ADD email varchar(50) not null")
mycursor.execute("Alter table employees ADD ssn varchar(30) not null UNIQUE")
mycursor.execute("describe employees")

for x in mycursor:
    print(x)

print()

mycursor.execute("CREATE TABLE department (DNO INT NOT NULL PRIMARY KEY, Dname varchar(30) not null)")

mycursor.execute("show tables")
for x in mycursor:
    print(x)

print()
mycursor.execute("describe department")

for x in mycursor:
    print(x)


print()
mycursor.execute("Create table project (PNO INT NOT NULL PRIMARY KEY auto_increment, PROJ_HR decimal NOT NULL, proj_name varchar(30) not null, proj_start_date date not null, proj_due_date date not null)")

mycursor.execute("Show tables")

for x in mycursor:
    print(x)

print()

mycursor.execute("describe project")

for x in mycursor:
    print(x)

print()

mycursor.execute("Create table dependent(dependent_name varchar(50) not null, dep_phone varchar(20) not null, relationship varchar(50) not null)")

mycursor.execute("Show tables")

for x in mycursor:
    print(x)

print()

mycursor.execute("describe dependent")

for x in mycursor:
    print(x)


print()

mycursor.execute("create table qualification(university varchar(50), degree varchar(20))")

mycursor.execute("show tables")
for x in mycursor:
    print(x)

print()
mycursor.execute("describe qualification")
for x in mycursor:
    print(x)

print()

mycursor.execute("Alter table department ADD EMP_ID_DNO INT NOT NULL")
mycursor.execute("Alter table department ADD Constraint FK_EMP_ID_DNO FOREIGN KEY (EMP_ID_DNO) REFERENCES employees(EMP_ID) ON UPDATE CASCADE ON DELETE CASCADE")
mycursor.execute("describe department")


for x in mycursor:
    print(x)




print()

mycursor.execute("Alter table project add emp_id_proj INT not null, add constraint FK_proj_emp_id foreign key(emp_id_proj) references employees(emp_id) ON UPDATE CASCADE ON DELETE CASCADE")
mycursor.execute("Alter table project add DNO_proj int not null, add constraint FK_DNO_proj foreign key(DNO_proj) references department(DNO) ON UPDATE CASCADE ON DELETE CASCADE")
mycursor.execute("describe project")
for x in mycursor:
    print(x)

print()


mycursor.execute("Alter table qualification add emp_id_qual int not null auto_increment, add constraint FK_qual_emp_id foreign key(emp_id_qual) references employees(emp_id) ON UPDATE CASCADE ON DELETE CASCADE")
mycursor.execute("describe qualification")


for x in mycursor:
    print(x)

print()

mycursor.execute("describe employees")
for x in mycursor:
    print(x)


print()

mycursor.execute("Alter table employees Add DNO_emp INT not null")

mycursor.execute("describe employees")

for x in mycursor:
    print(x)

print()
insert = "INSERT INTO employees (emp_id, fname, lname, job_title, salary, street, city, state, zip, hire_date, age, emp_phone, email, ssn, gender, DNO_emp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

val = [
                                (1, "Joe", "Wong", "Project Manager", random_salary(), fake.street_name(), fake.city(), random_state(), random_zip_generator(),  
                                "1990-02-14", 55, random_phone_num_generator(), "joeWong@gmail.com" ,fake.ssn(), random_gender(), 1),
                                (2, "Marcellus", "Chello", "Project Manager", random_salary(), fake.street_name(), fake.city(), random_state(), 
                                random_zip_generator(), "1989-01-15", 65, random_phone_num_generator(), fake.email(), fake.ssn(), random_gender(), 2),
                                (3, "Jenny", "Paps", "Project Manager", random_salary(), fake.street_name(), fake.city(), random_state(), 
                                random_zip_generator(), "1995-01-20", 40, random_phone_num_generator(), fake.email(), fake.ssn(), random_gender(), 3)


]

mycursor.executemany(insert, val)


mydb.commit()



mycursor.execute("Select * from hr_system.employees")

for x in mycursor:
    print(x)

print()

mycursor.execute("describe department")
for x in mycursor:
    print(x)
print()


insert = "INSERT INTO department (DNO, Dname, emp_id_DNO) VALUES (%s, %s, %s)"

val = [
                                (1, "Research", 1),
                                (2, "Distribution", 2),
                                (3, "Branding", 3)


]

mycursor.executemany(insert, val)


mydb.commit()

mycursor.execute("Select * from hr_system.department")

for x in mycursor:
    print(x)

print()

mycursor.execute("Alter table employees add constraint FK_DNO_emp foreign key(DNO_emp) references department(DNO) ON UPDATE CASCADE ON DELETE CASCADE")
mycursor.execute("describe employees")
#mycursor.execute("describe department")

for x in mycursor:
    print(x)


print()

for x in range(9997):
    x = "INSERT INTO employees (fname, lname, job_title, salary, street, city, state, zip, hire_date, age, emp_phone, email, ssn, gender, DNO_emp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = [
        (fake.first_name(), fake.last_name(), fake.job(), random_salary(), fake.street_name(), fake.city(), random_state(), random_zip_generator(),  
        fake.date(), age_num(), random_phone_num_generator(), fake.email() ,fake.ssn(), random_gender(), dept_num()),
                               


    ]
    mycursor.executemany(x, val)


    mydb.commit()

print(mycursor.rowcount, "record inserted.")





mycursor.execute("Select * from hr_system.employees")

for x in mycursor:
    print(x)

print()


mycursor.execute("describe qualification")

for x in mycursor:
    print(x)

print()







mycursor.execute("describe qualification")
for x in mycursor:
    print(x)

print()




mycursor.execute("Select * from qualification")

for x in mycursor:
    print(x)

print()





for y in range(10000):
    y = "INSERT INTO qualification (degree, university) VALUES (%s, %s)"
    val = [
        (random_degree(), random_university_choice()) 
    ]
    mycursor.executemany(y, val)


    mydb.commit()

print(mycursor.rowcount, "record inserted.")


print()
mycursor.execute("Select * from qualification")

for x in mycursor:
    print(x)

print()





mycursor.execute("Alter table dependent add emp_id_dependent int not null auto_increment, add constraint FK_dependent_emp_id foreign key(emp_id_dependent) references employees(emp_id) ON UPDATE CASCADE ON DELETE CASCADE")

mycursor.execute("describe dependent")

for x in mycursor:
    print(x)

print()


for x in range(10000):
    x = "INSERT INTO dependent (dependent_name, dep_phone, relationship) VALUES (%s, %s, %s)"

    val = [
        (fake.name(), random_phone_num_generator(), random_relationship_choice())
                               


    ]
    
    
    mycursor.executemany(x, val)


    mydb.commit()

print(mycursor.rowcount, "record inserted.")


print()


mycursor.execute("Select * from hr_system.dependent")

for x in mycursor:
    print(x)

print()



mycursor.execute("describe project")

for x in mycursor:
    print(x)

print()


mycursor.execute("ALTER table project drop constraint FK_proj_emp_id")
mycursor.execute("Alter table project drop column emp_id_proj")
mycursor.execute("Alter table project drop column proj_hr")
mycursor.execute("Alter table project drop column proj_start_date")
mycursor.execute("Alter table project drop column proj_due_date")



mycursor.execute("describe project")



for x in mycursor:
    print(x)

print()


insert = "INSERT INTO project (PNO, proj_name, DNO_proj) VALUES (%s, %s, %s)"

val = [
                                (1, "ProductA", 1),
                                (2, "ProductB", 2),
                                (3, "ProductC", 3),
                                (4, "ProductD", dept_num()),
                                (5, "ProductE", dept_num()),
                                (6, "ProductF", dept_num()),
                                (7, "ProductG", dept_num()),
                                (8, "ProductH", dept_num()),
                                (9, "ProductI", dept_num()),
                                (10, "ProductJ", dept_num()),
                                (11, "ProductK", dept_num()),
                                (12, "ProductL", dept_num()),
                                (13, "ProductM", dept_num()),
                                (14, "ProductN", dept_num()),
                                (15, "ProductO", dept_num()),
                                (16, "ProductP", dept_num()),
                                (17, "ProductQ", dept_num()),
                                (18, "ProductR", dept_num()),
                                (19, "ProductS", dept_num()),
                                (20, "ProductT", dept_num()),
                                (21, "ProductU", dept_num()),
                                (22, "ProductV", dept_num()),
                                (23, "ProductW", dept_num()),
                                (24, "ProductX", dept_num()),
                                (25, "ProductY", dept_num()),
                                (26, "ProductZ", dept_num())]

mycursor.executemany(insert, val)


mydb.commit()

mycursor.execute("Select * from hr_system.project")


for x in mycursor:
    print(x)


mycursor.execute("Create table works_for (hours int not null)")


mycursor.execute("describe works_for")
for x in mycursor:
    print(x)

print()


mycursor.execute("describe works_for")

for x in mycursor:
    print(x)

print()



mycursor.execute("Alter table works_for add emp_id_work_for int not null auto_increment, add constraint FK_work_emp_id foreign key(emp_id_work_for) references employees(emp_id) ON UPDATE CASCADE ON DELETE CASCADE")

for x in mycursor:
    print(x)


mycursor.execute("Alter table works_for add PNO_works_for int not null, add constraint FK_work_PNO foreign key(PNO_works_for) references project(PNO) ON UPDATE CASCADE ON DELETE CASCADE")

for x in mycursor:
    print(x)

mycursor.execute("describe works_for")

for x in mycursor:
    print(x)

for x in range(10000):
    x = "INSERT INTO works_for (hours, PNO_works_for) VALUES (%s, %s)"

    val = [
        (random_hour(), random_proj_num())
                               


    ]
    
    
    mycursor.executemany(x, val)


    mydb.commit()



"""



"""
mycursor.execute("select * from hr_system.works_for")

for x in mycursor:
    print(x)
print()


mycursor.execute("select * from hr_system.qualification")

for x in mycursor:
    print(x)
print()




# Dropping Tables and Foreign Keys
"""
mycursor.execute("alter table qualification drop constraint FK_qual_emp_id")
mycursor.execute("Alter table project drop constraint FK_DNO_proj")
mycursor.execute("ALTER table project drop constraint FK_proj_emp_id")
mycursor.execute("ALTER TABLE department DROP constraint FK_EMP_ID_DNO")
mycursor.execute("Alter table employees drop constraint FK_DNO_emp")
mycursor.execute("drop table qualification")
mycursor.execute("drop table dependent")
mycursor.execute("Drop table project")
mycursor.execute("DROP Table employees")
mycursor.execute("Drop table department")
mycursor.execute("Alter table works_for drop constraint FK_work_emp_id")
mycursor.execute("Alter table works_for drop column emp_id_work_for ")
mycursor.execute("Alter table works_for drop constraint FK_work_PNO")
mycursor.execute("Alter table works_For drop column PNO_works_for")

"""
#for x in mycursor:
 #   print(x)
