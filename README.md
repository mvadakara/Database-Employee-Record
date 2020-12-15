# Database-Employee-Record
A database filled with 10,000 records of fake employee data using Python and mySQL

Instrucions: 
![database_schema.png](https://gitlab.com/ScarDemon/cs-517_database_project/-/raw/master/database_schema.png)

https://www.python.org/downloads/  -> To download Python on your computer




_________________________________________________________
Python packages on command prompt for this project to work.


pip install faker 

![pip_install_faker](https://gitlab.com/ScarDemon/cs-517_database_project/-/raw/master/pip_install_faker.PNG)


pip3 install faker



pip install mysql-connector-python

![pip_install_mysql_connector](https://gitlab.com/ScarDemon/cs-517_database_project/-/raw/master/pip_install_mysql_connector.PNG)

pip3 install mysql-connector-python
___________________________________________________________

https://dev.mysql.com/downloads/mysql/  -> Download mySQL community server 

in order to launch mySQL run 


mysql -uroot -p 
password should be blank should just press enter 
in mySQL 

![cmd__mysql_example.png](https://gitlab.com/ScarDemon/cs-517_database_project/-/raw/master/cmd_mysql_example.PNG)

In my mySQL run the following:
create database hr_system;  

which create hr_system.  

![create_hr_system](https://gitlab.com/ScarDemon/cs-517_database_project/-/raw/master/create_hr_system.PNG)
______________________________________________________________
After creating hr_system open up another command prompt and cd into the directory where the python files are located.
then run the python file as:
python script.py  - which creates the tables and inserts the the data as needed.

![running_script](https://gitlab.com/ScarDemon/cs-517_database_project/-/raw/master/running_script.py_in_command_prompt_to_insert_and_create_data_for_hr_System.PNG)

You may have to drop and create a few times the database 
because ssn has unqiue values and fake.ssn() gives a random ssn which may not be unique.  


Then run:  python script2.py in order to read, update, and delete the data within the database.
![script2_running](https://gitlab.com/ScarDemon/cs-517_database_project/-/raw/master/script2_running.PNG)

