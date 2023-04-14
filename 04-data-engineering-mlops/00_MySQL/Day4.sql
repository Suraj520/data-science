--1. Sort the various department names alphabetically from table departments
select * from departments order by dept_name;
--2 . Sort the various department names alphabetically by the penultimate letter of their second string separated by a blankspace
select * from departments order by substr(dept_name,-2) DESC;
--3. Return the records of top 3 highest paid employees
select  * from salaries order by salary desc limit 3;
--4 Return the records of top 3 highest paid employees who joined after 2010
select * from salaries where date(from_date) >= '2011-1-1' order by salary desc limit 3 ;
--5 Return the top 3 highest paid employees for 2002-2010 on an average. (To:DO)
--5. Display a sorted table after joining salaries and titles using salary
Select sal.emp_no, sal.salary, t.from_date, t.to_date, t.title
from salaries sal
JOIN titles t
ON sal.emp_no = t.emp_no ORDER BY salary desc;
