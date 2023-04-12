> Contents
1. Airflow DAG - Basic.
2. Airflow Dockers

#### About
1. Apache Airflow is an opensource tool to create, schedule, monitor and execute complex workflows. 
2. It is used in scenarios where tasks in workflow are required to be executed in periodically over a specific order.
3. It is a key components for DataOps workflow and can easily be extended to MLOps workflow to create a unified data pipeline.
4. It is a python based efficient workflow management tool also known as Orchestrator.
5. DAGs(Directed Acyclic Graphs) are used to handle long running tasks and dependencies. Each workflow in Airflow is also known as DAGs. Every node in a DAG executes only once and every node has only one set of I/O.
6. Airflow's WebUI can be used to monitor tasks that are in queue to be run, which are running etc.
7. When jobs fail in DAGs, Alerts via Email or Slacks can be instantiated.
8. Airflow uses Executors to scale the jobs when it gets complex. Celery or Kubernetes are used to handle complex ones.
9. Airflow is netither a data streaming solution nor a facilitator for moving huge data between tasks. 
10. Workflows are defined in python but Airflow can invoke frameworks built out of other languages.
11. Operators are classified into three categories - Sensors, Operators and Transfers.
12. Sensors are a certain type of operator that will keep running until a certain criteria is met. Example include waiting for a certain time, external file or upstream data source.
13. HdfsSensor waits for a file or folder to land in HDFS.
14. NamedHivePartitionSensor checks whether the most recent partition of a hive table is available for downstream processing.
15. Operators triggers a certain action. In ETL, It represents the transform step. Examples include BashOperator, PythonOperator, HiveOperator or BigQueryOperator.
16. Transfers move data from one location to another. MySqlToHiveTransfer  and S3ToRedshiftTransfer are examples of it.
17. Custom operators can be written by extending base operators in Airflow.
18. set_upstream(>>), set_downstream(<<) are used to define task execution order.
