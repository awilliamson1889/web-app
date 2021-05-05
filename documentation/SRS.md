# <center>Human resource management</center>
***
## 1.Introduction
### 1.1 Purpose
The purpose of this document is to provide a detailed description of the web application "Human resource management".
It will explain the purpose of the web application, what it will do and the limitations under which it will work.
This document is intended for users of the application, as well as for potential developers.
### 1.2 Product Scope
"Human resource management" is a web application that can be used to manage employees and departments in an organization.
***
## 2.Overall Description
### 2.1 Product perspective
"Personnel management" is a web application that implements a client-server interaction model. "Personnel management" provides the user with a simple mechanism for working with 
a database that contains information about the organization. When processing user requests, the application displays or manipulates data in the database.
### 2.2 Product functions
With this web application, manager can manage the employees and departments of the organization. Manager has access to tables that store all the necessary information. 
Data manipulation functions such as adding, deleting, and editing are available to the user.
Also, for the convenience of working with tables in this web application, there is a table search and filtering.
***
## 3.Specific requirements
### 3.1 User interfaces
"Human resource management" - is a web application that automates the management of employees and departments in an organization.
The application must provide:

- Separation of user rights managers/regular users
- Displaying information about employees/departments;
- Adding new employees/department;
- Editing employee/department information;
- Deletion of information about employee/department.
### 3.2 Loggin/Sign in

***Main scenario:***

+ User logs in to the site;
+ Application displays Sign in page;
+ If the entered data is incorrect an authorization error message is displayed.
+ If the entered data is correct, the user is redirected to his profile page.

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/login_page.PNG">

Pic. 3.1 - Sign in page

### 3.3 Profile page

***Main scenario:***

+ User is successfully logged in or user clicks the "My Profile" button;
+ Application displays user profile page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/employee_account.PNG">

Pic. 3.2 - Employee profile page

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/manager_account.PNG">

Pic. 3.3 - Manager profile page

### 3.4 Departments page

***Main scenario:***

+ User clicks the "Departments" button;
+ Application displays departments page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/departments_page.PNG">

Pic. 3.4 - Departments page

***Filtering by country:***
+ In the department list view mode, user sets a country filter;
+ The application will display a form to view the list of departments with updated data.

### 3.5 Department page

***Main scenario:***

+ User select the "Department";
+ Application displays department information page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/info_department.PNG">

Pic. 3.5 - Department information page

### 3.6 People search page

***Main scenario:***

+ User clicks the "People search" button;
+ Application displays people search page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/people_search.PNG">

Pic. 3.6 - People search page

***Filtering by country/skill:***
+ In the people/employees list view mode, user sets a country filter;
+ The application will display a form to view the list of people/employees with updated data.
+ In the people/employees list view mode, user sets a primary skill filter;
+ The application will display a form to view the list of people/employees with updated data.

### 3.7 Managment/Departments page

***Main scenario:***

+ User clicks the "Managment/Departments" button;
+ Application displays Departments page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/manage_departments.PNG">

Pic. 3.7 - Departments page

### 3.8 Managment/Employees page

***Main scenario:***

+ User clicks the "Managment/Employees" button or "new" button on Add Employee page;
+ Application displays Employees page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/manage_employees.PNG">

Pic. 3.8 - Employees page

### 3.9 Managment/Locations page

***Main scenario:***

+ User clicks the "new" button;
+ Application displays add locations page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/add_location.PNG">

Pic. 3.9 - Locations page

### 3.10 Managment/Work address page

***Main scenario:***

+ User clicks the "new" button;
+ Application displays Work address page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/add_workaddress.PNG">

Pic. 3.10 - Work address page

### 3.11 Add department page

***Main scenario:***

+ User clicks the "Add department" button;
+ Application displays add department page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/add_department.PNG">

Pic. 3.11 - Add department page

### 3.12 Edit department page

***Main scenario:***

+ User clicks the "Edit" button;
+ Application displays edit department page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/edit_department.PNG">

Pic. 3.12 - Edit department page

### 3.13 Add Employee page

***Main scenario:***

+ User clicks the "Add Employee" button;
+ Application displays add employee page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/add_employee.PNG">

Pic. 3.13 - Edit department page

### 3.14 Edit employee page

***Main scenario:***

+ User clicks the "Edit" button;
+ Application displays edit employee page;

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/edit_employee.PNG">

Pic. 3.14 - Edit employee page

### 3.15 Delete employee

***Main scenario:***

+ User clicks the "Delete" button;
+ the application displays a dialog box;
+ If answer "OK", application delete employee from database;
+ If answer "Cancle", application rederect user to Manage/Employees page.

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/delete_employee.PNG">

Pic. 3.15 - Delete employee

### 3.16 Delete employee

***Main scenario:***

+ User clicks the "Delete" button;
+ the application displays a dialog box;
+ If answer "OK", application delete department from database;
+ If answer "Cancle", application rederect user to Manage/Departments page.

<img src="https://github.com/awilliamson1889/web-app/blob/main/documentation/pictures/delete_department.PNG">

Pic. 3.16 - Delete department
