-- Tables being departments(dept_no, dept_name) as deps, 
-- dept_emp(emp_no, dept_no, from_date, to_date) as depe, 
-- dept_manager(dept_no, emp_no, from_date, to_date) as depm
--, employees(emp_no, birth_date, first_name, last_name, gender) as emp, 
-- salaries(emp_no, salary, from_date, to_date) as sal, 
-- titles(emp_no, title, from_date, to_date) as tis.
--1, Join three tables dept_manager, departments, dept_emp;
Select deps.dept_no, deps.dept_name, depe.emp_no, depe.from_date, depe.to_date
FROM departments deps
INNER JOIN dept_manager depm ON deps.dept_no=depm.dept_no
INNER JOIN dept_emp depe ON deps.dept_no = depe.dept_no; 
--2. Join all the tables in the database and create a master table
Select deps.dept_no, deps.dept_name, depe.emp_no, depe.from_date, depe.to_date, sal.salary, tis.title
FROM departments deps, salaries sal, titles tis
INNER JOIN dept_manager depm ON deps.dept_no= depm.dept_no
INNER JOIN dept_emp depe ON deps.dept_no = depe.dept_no
INNER JOIN dept_emp ON depe.emp_no = sal.emp_no
INNER JOIN dept_emp ON depe.emp_no = tis.emp_no;
-- Good luck, It takes a lot of time to execute; Just in case you thought to execute :)
