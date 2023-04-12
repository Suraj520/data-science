-- 1. visualize all the data in the database
Select * from departments;
Select * from dept_emp;
Select * from dept_manager;
Select * from employees;
Select * from salaries;
Select * from titles;
-- You have a table and want to see only rows that satisfy a specific condition. 
--- 2. Use the WHERE clause to specify which rows to keep. For example, to view all employees assigned to department number 10 
Select * from titles WHERE title='Engineer';
-- 3. Use the WHERE clause along with the OR and AND clauses. For example, if you would like to find all the employees in department 10, along with any employees who earn a commission, along with any employees in department 20 who earn at most $2000
--Select * from titles WHERE title='Engineer'
Select * from employees WHERE first_name ='Georgi' or gender='M' and emp_no >=10045;
-- 4. Specify the columns you are interested in. For example, to see only name, department number, and salary for employees 
Select emp_no, birth_date, gender from employees;
-- 5  To change the names of your query results use the AS keyword In the form: original_name AS new_name.  
Select emp_no as employee_id from employees;
--6 You have used aliases to provide more meaningful column names for your result set and would like to exclude some of the rows using the WHERE clause. However, your attempt to reference alias names in the WHERE clause fails:  
Select * from ( Select emp_no as employee_id, gender as Gender from employees) where employee_id>12465;
--7 You want to return values in multiple columns as one column. For example, you would like to produce this result set from a query against the EMP table: CLARK WORKS AS A MANAGER KING WORKS AS A PRESIDENT MILLER WORKS AS A CLERK 
-- Like Georgi Facello is Male
Select first_name ||' ' || last_name || 'is a' || '' || gender AS description  from employees;
--8 You want to perform IF-ELSE operations on values in your SELECT statement. For example, you would like to produce a result set such that, if an employee is paid $2000 or less, a message of “UNDERPAID” is returned, if an employee is paid $4000 or more, a message of “OVERPAID” is returned, if they make somewhere in between, then “OK” is returned. T 
Select emp_no as Employee_ID, salary, 
CASE 
	WHEN salary < 50000 then 'UNDERPAID'
	WHEN salary >=50000 then 'OVERPAID'
	Else 'OK'
End AS Information
FROM salaries; 
-- 9 You want to limit the number of rows returned in your query. You are not concerned with order; any n rows will do. 
Select * from titles limit 100;
--10 Returning n Random Records from a Table 
Select emp_no as Employee_ID from employees order by random() limit 10;
