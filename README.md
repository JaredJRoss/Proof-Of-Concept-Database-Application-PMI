# Proof-Of-Concept-Database-Application-PMI
**Basic Info**

The test database uploaded on the GitLab consists of a Django Web Application that is connected to a MySql database that is currently hosted on the same computer as the one that is running the Django Web Application.
This bare-bones application will be used to test the possibility of using a local server to host both the database and web application, and to find the best way to connect to the server and use the web application from an external device. 


**Database Info**

The test database was developed with MariaDB as the database, and it works identically as a MySQL database.
The database holds Persons objects, which will be used to store Constituents in the finalized version of the application. Each Person object contains the fields:
```
“person_lastname”
“person_firstname”
“person_title”
“person_date”
```
The “person_title” field is of interest, and should be taken a look at because it implements a scroll down option for the field instead of a standard textbox. Will be very useful in making the application user friendly. 


**Connecting MySQL/ MariaDB to Django**

In order to use the web application, there must be an active session of MySQL or MariaDB. This should not be an issue when the server is up and running, but for the time being, to start an instance of MySQL / MariaDB on your local device, follow the steps below: [[steps with $ in front is to be typed into the command terminal. With the “$” excluded]]
```
Install MySQL or MariaDB
$ mysql -u root -p
$ CREATE DATABASE basicdb CHARACTER SET UTF8;
$ CREATE USER admin@localhost IDENTIFIED BY ‘admin’;
$ GRANT ALL PRIVILEGES ON basicdb.* TO admin@localhost;
$ FLUSH PRIVILEGES;
$ exit
Run the server from the basicdatabase directory by typing:
$ python manage.py runserver
```
After this you should be able to go to: http://localhost:8000/ogdb/home to view the table and add employee form. 


**About**

Frameworks used in this app that will be useful for the full app development were:
```
 Django_table2
 ModelForms 
```


Frameworks that will be used in the full application are:
```
Django filters
Django's authentication
```

Front End template from: http://www.tooplate.com/view/2082-pure-mix
