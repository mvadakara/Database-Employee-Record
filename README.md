# Database-Employee-Record
A database filled with 10,000 records of fake employee data using Python and mySQL

Instrucions: 

https://www.python.org/downloads/  -> To download Python on your computer




_________________________________________________________
Python packages on command prompt for this project to work.


pip install faker 




pip3 install faker



pip install mysql-connector-python


pip3 install mysql-connector-python
___________________________________________________________

https://dev.mysql.com/downloads/mysql/  -> Download mySQL community server 

in order to launch mySQL run 


mysql -uroot -p 
password should be blank should just press enter 
in mySQL 


In my mySQL run the following:
create database hr_system;  

which create hr_system.  


______________________________________________________________
After creating hr_system open up another command prompt and cd into the directory where the python files are located.
then run the python file as:
python script.py  - which creates the tables and inserts the the data as needed.


You may have to drop and create a few times the database 
because ssn has unqiue values and fake.ssn() gives a random ssn which may not be unique.  


Then run:  python script2.py in order to read, update, and delete the data within the database.


