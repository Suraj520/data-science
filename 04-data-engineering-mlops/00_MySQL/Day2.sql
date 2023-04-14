-- 1. We have a table called Shippers. Return all the fields from all the shippers
select * from employees;
-- 2 return certain fields from the same database
select emp_no as employee_no, first_name as FirstName from employees;
-- 3 Filter out only certain rows from a table using Where clause
select emp_no as employee_no from employees where emp_no > 15365;
--4 Display the same columns as above, but only where title is staff and have served more than 10 years
select * from titles where title = 'Staff' and strftime('%s', to_date) - strftime('%s',from_date) > 25000000000;
--5 Show all the records from dept_no 1
select * from dept_manager where dept_no='d001';
--6 Display all male employee's first_name and last_name along with their birth_date
select first_name, last_name, birth_date from employees where gender='M';
--7 Display all the records where first_name = 'Georgi' 
select * from employees where first_name = 'Georgi';
--8 Display all the records where title is either technique leader or senior engineer
select * from titles where title='Technique Leader' or title='Senior Engineer';
--9 Display all the employees sorted by age as per birth date
select * from employees ORDER BY birth_date ;
--10 Display all employees full name with ID in a single COLUMN
Select first_name || ' ' || last_name || ' Has Employee_No. ' || emp_no as Description from employees;