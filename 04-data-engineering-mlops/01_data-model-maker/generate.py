import sqlparse
from sql_metadata import Parser

strsql = """
SELECT
  e.employee_id AS "Employee #"
  , e.first_name || ' ' || e.last_name AS "Name"
  , e.email AS "Email"
  , e.phone_number AS "Phone"
  , TO_CHAR(e.hire_date, 'MM/DD/YYYY') AS "Hire Date"
  , TO_CHAR(e.salary, 'L99G999D99', 'NLS_NUMERIC_CHARACTERS = ''.,'' NLS_CURRENCY = ''$''') AS "Salary"
  , e.commission_pct AS "Comission %"
  , 'works as ' || j.job_title || ' in ' || d.department_name || ' department (manager: '
    || dm.first_name || ' ' || dm.last_name || ') and immediate supervisor: ' || m.first_name || ' ' || m.last_name AS "Current Job"
  , TO_CHAR(j.min_salary, 'L99G999D99', 'NLS_NUMERIC_CHARACTERS = ''.,'' NLS_CURRENCY = ''$''') || ' - ' ||
      TO_CHAR(j.max_salary, 'L99G999D99', 'NLS_NUMERIC_CHARACTERS = ''.,'' NLS_CURRENCY = ''$''') AS "Current Salary"
  , l.street_address || ', ' || l.postal_code || ', ' || l.city || ', ' || l.state_province || ', '
    || c.country_name || ' (' || r.region_name || ')' AS "Location"
  , jh.job_id AS "History Job ID"
  , 'worked from ' || TO_CHAR(jh.start_date, 'MM/DD/YYYY') || ' to ' || TO_CHAR(jh.end_date, 'MM/DD/YYYY') ||
    ' as ' || jj.job_title || ' in ' || dd.department_name || ' department' AS "History Job Title"
  
FROM employees e
-- to get title of current job_id
  JOIN jobs j 
    ON e.job_id = j.job_id
-- to get name of current manager_id
  LEFT JOIN employees m 
    ON e.manager_id = m.employee_id
-- to get name of current department_id
  LEFT JOIN departments d 
    ON d.department_id = e.department_id
-- to get name of manager of current department
-- (not equal to current manager and can be equal to the employee itself)
  LEFT JOIN employees dm 
    ON d.manager_id = dm.employee_id
-- to get name of location
  LEFT JOIN locations l
    ON d.location_id = l.location_id
  LEFT JOIN countries c
    ON l.country_id = c.country_id
  LEFT JOIN regions r
    ON c.region_id = r.region_id
-- to get job history of employee
  LEFT JOIN job_history jh
    ON e.employee_id = jh.employee_id
-- to get title of job history job_id
  LEFT JOIN jobs jj
    ON jj.job_id = jh.job_id
-- to get namee of department from job history
  LEFT JOIN departments dd
    ON dd.department_id = jh.department_id

ORDER BY e.employee_id;
"""

statements = sqlparse.split(strsql)
all_columns = list()
all_tables = list()
all_joins = ""

for stmt in statements:
    parser = Parser(stmt)
    for key,value in parser.columns_dict.items():
        if value is not None:
            all_columns.append(value)
    for j in parser.tables:
        all_tables.append(j.split())
    i=0
    join_cond=""
    if 'join' in parser.columns_dict:
        for j in parser.columns_dict['join']:
            if i%2 == 0:
                join_cond = join_cond + "" + "Ref: "+j
            else:
                join_cond = join_cond + " - " + j +"|"
            i = i + 1
        all_joins = all_joins + join_cond


all_joins_list = all_joins.split("|")
all_joins_list = list(set(all_joins_list))
all_joins = '|'.join(all_joins_list)


all_columns = sum(all_columns, [])
all_columns = list(set(all_columns))

all_tables = sum(all_tables, [])
all_tables = list(set(all_tables))


i=0
table_def=""
for j in all_tables:
    table_struct=""
    table_struct = "Table "+j+" {\nrowid bigint"
    for i in all_columns:
        if i.startswith(j+'.') :
            table_struct = table_struct +"\n"+ i.split('.')[-1] + " string "
    table_def = table_def + table_struct + "\n}\n|"


for i in table_def[:-1].split("|"):
    print (i)

for i in all_joins[1:].split("|"):
    print (i)

