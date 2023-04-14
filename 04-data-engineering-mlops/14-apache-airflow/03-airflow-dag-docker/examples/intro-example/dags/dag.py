from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# modification to context managers
default_args = {
    'owner':'suraj',#name of dag 
    'start_date': airflow.utils.dates.days_ago(2),
    #'end_date': datetime(2023,3,26),
    'depends_on_past': False,
    'email':['suraj@gmail.com'],
    'email_on_failure':False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting for 2 minutes
    'retries':1,
    'retry_delay': timedelta(minutes=2),
} 

#instantiate dag
dag = DAG(
    'dag', default_args = default_args,
    description = 'Docker dag',
    schedule_interval = timedelta(days=1),
)

# creating tasks
t1 = BashOperator(task_id = 'print_date',
                  bash_command ='date',
                  dag=dag)

t2 = BashOperator(
    task_id ='sleep',
    depends_on_past = False,
    bash_command= 'sleep 5',
    dag = dag,
)

# Ginger template
templated_command = """
{% for i in range(10) %}
    echo "{{ds}}"
    echo "{{macros.ds_add(ds,7)}}"
    echo "{{params.first}}"
{% endfor %}
"""

t3 = BashOperator(
    task_id = 'ginger_template_task',
    depends_on_past = False,
    bash_command = templated_command,
    params = {'first':'Hello World'},
    dag = dag
)

# order of the task
# using set_downstream and set_upstream
#t1.set_downstream(t2) # if t1 is completed then task 2 # alternatively t1 >> t2
t1.set_downstream([t2,t3])
