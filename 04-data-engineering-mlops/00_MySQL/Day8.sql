--1. Write a function in SQL which sets the taxable income of all who have salary less than 30,000 to zeroblob
DELIMITER //
CREATE FUNCTION set_null_tax(salary INTEGER)
RETURNS char(12)
[NOT] DETERMINISTIC 
BEGIN 
	declare info char(12)
	IF salary < 30,000 THEN
		RETURN null;
END
//
DELIMITER ;
Select sal.emp_no, sal.salary, set_null_tax(sal.salary) as Tax_info from salaries sal;