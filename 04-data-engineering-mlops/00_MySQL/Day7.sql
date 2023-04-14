--1. Cut off 30% tax on all employees whose salary is greater than 60000, 20% for all those whose salary is between 30,000 to 60,000 and none if less than 30,000 INR. Display the net salary in a new COLUMN
 SELECT sal.emp_no,sal.salary, sal.from_date, sal.to_date, 
    CASE WHEN sal.salary > 60000
    THEN round(sal.salary-sal.salary*0.2)
    WHEN sal.salary > 60000 AND sal.salary > 30000
    THEN round(sal.salary-sal.salary*0.2)
    ELSE sal.salary
    END AS NET_SALARY
    FROM salaries sal;
-- 2. Assign grades to each employee based on their salary
-- Grade A for salary >90000, grade B for salary <90000 and >80000, repeat till 30,000 range.
Select sal.emp_no, sal.salary, sal.from_date, sal.to_date, 
   CASE WHEN sal.salary>90000
   THEN 'A'
   WHEN sal.salary>80000 and sal.salary<90000
   THEN 'B'
   WHEN sal.salary>70000 and sal.salary<80000
   THEN 'C'
   WHEN sal.salary>60000 and sal.salary<70000
   THEN 'D'
   WHEN sal.salary>50000 and sal.salary<60000
   THEN 'E'
   WHEN sal.salary>40000 and sal.salary<50000
   THEN 'F'
   WHEN sal.salary>30000 and sal.salary<40000
   THEN 'G'
   ELSE
   'AVERAGE'
   END AS GRADE
   from salaries sal;
