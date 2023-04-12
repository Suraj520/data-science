--1. Assuming each employee worked for atleast 2 years, Find the total salary earned by people during the course of the employment tenure.
select emp_no as EMPLOYEE_NO, salary * 24*0.013 as "NET SALARY(IN USD)" from salaries;
--2. Display number of employees in the DATABASE
select count(*) as "NUM_EMPLOYEES" from employees;
--3. Display the oldest employee in the DATABASE
select sal.emp_no as "EMPLOYEE_ID", MIN(sal.from_date), emp.title from salaries as sal, titles as emp;
--4. Display number of staffs per title in the table titles
select title, COUNT(title) as "NUMBER OF STAFFS" from titles group by title; 
--5. Display all employees's employee number, title and department number
select titles.emp_no,titles.title,dept_emp.dept_no from titles inner join dept_emp on titles.emp_no = dept_emp=emp_no;