-- Abbreviation
-- dept_emp(emp_no, dept_no, from_date, to_date) as depe, 
-- dept_manager(dept_no, emp_no, from_date, to_date) as depm
--, employees(emp_no, birth_date, first_name, last_name, gender) as emp, 
-- salaries(emp_no, salary, from_date, to_date) as sal, 
-- titles(emp_no, title, from_date, to_date) as tis.

--1. We'd like to offer ESOPs to all the top performing employees
-- Criterion: Income >= 71046 and have worked atleast 10 years at the firm as a Senior Engineer.
-- Approach : 1st join the tables : salaries and titles then sort by salary and difference between the dates.

select sal.emp_no, tis.title, sal.salary, sal.from_date, sal.to_date
FROM salaries as sal
INNER JOIN titles tis ON sal.emp_no = tis.emp_no
WHERE tis.title='Senior Engineer' and sal.salary>71046 and date(sal.to_date) - date(sal.from_date)> 365*10;
--2. The ESOPs granting criterion has now been changed slightly w,r,t 1. Offering ESOPs only to those who have earned more than 71046*5 INR between 2002 and 2004. Needless to say ignore the employees who are not there.
select sal.emp_no, tis.title, sal.salary, sal.from_date, sal.to_date
FROM salaries as sal
INNER JOIN titles tis ON sal.emp_no = tis.emp_no
WHERE sal.salary * (date(sal.to_date) - date(sal.from_date))> 71046*5 and tis.title='Senior Engineer' and `sal.to_date` BETWEEN '2002-01-01' AND '2004-12-31' and `sal.from_date` BETWEEN '2002-01-01' AND '2004-12-31';

 
