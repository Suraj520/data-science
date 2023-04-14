#### About
1. Tasks are nodes in an Airflow DAG.
2. Directed edges between the nodes describe the dependency between the tasks.
3. DAGs are created to execute complex flow of tasks where data maybe shared between each.
4. An operator is a task in the data pipeline. Let's suppose that T2 executes a bash command, T3 execute a python function and T4 wishes to append data into a database then T2 invokes a bashoperator, T3 invokes a python operator and T4 invokes a postgresoperator.


> Steps to create a dag
1. Create a folder dags or equivalent name and inside each create a dag file with python extension.
2. Ensure mandatory imports are being made at starting in the dag file.
3. Create a dag object using context manager 'with', Put dag id i.e unique identifier inside the dag object along with start date which denotes the date when dag will be scheduled. One can also define schedule_interval like daily. Add catchup = False to avoid multiple dag runs between current date and start date.
4. Import operators like python operators, bash opertators to create a task inside the dag object. Ensure each task has a unique identifier i.e task_id. Pass python callable function that needs to be executed via the task.
5. Create the python function which's being called in python callable function outside the dag object. 
6. Choose branch python operator to choose task from multiple tasks based on a criterion.
7. x-coms are used to share data or metrics between tasks in a DAG.
8. To define the order of tasks, bit shift operator are used. Right bit shift operator(>>) are used to define downstream task and (<<)left bit shift operator for defining upstream task. Usually, This is defined at the end of the dag file.

#### Information about basic dag
1. We'll execute 5 dummy python tasks(model training) that yield accuracy and choose the most accurate one to further execute.
2. Login to airflow ui at localhost:8080, Turn on the task and monitor the progress in graphview.