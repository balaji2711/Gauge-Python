# Login Specification - Data Driven 

table: resources/login_testdata.csv

* When I navigated to Login Page

## Registered user login to the system - Data Driven

tags: sanity

* When I login as <user_name> using <password>
* Then login should be successful