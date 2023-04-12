#### About
> Task Description

To build a data pipeline that ingests, processes, and stores data from an online retail store's website product and reviews records. The data should be transformed and stored in a data warehouse for analysis and reporting purposes.

> Requirements
1. Data should be collected from the website logs and sales records on a daily basis.
2. The data pipeline should be scalable and capable of handling large volumes of data.
3. The pipeline should include data cleaning and transformation steps.
4. The pipeline should be automated and scheduled to run at specific intervals.
5. The data warehouse should be easily accessible to analysts and data scientists.

Fake E-commerce Data API
Link - https://fakestoreapi.com/

> Steps

1. Installed all the required dependencies via
```
pip3 install -r requirements.txt
```

2. Initialise the airflow database

airflow db init 

If error persists - 
> Add DAGBAG_IMPORT_TIMEOUT = 30(integer not float) under [core] section to ~/airflow/airflow.cfg and pip install --upgrade sqlalchemy flask-admin and run airflow db check to ensure it's fixed.

3. Create fakestore_dag.py in dags directory. In the code, A DAG named fakestore_dag that executes run_pipeline using a PythonOperator is quoted. The DAG is set to run daily at midnight defined via schedule_interval arg.

4. Start the airflow web server and scheduler

airflow scheduler
airflow webserver --port 8000

5. Open a web browser and navigate to localhost:8080 to access the airflow WebUI.

6. Click DAGs tab and fakestore_dag
7. Click on "Graph View" to see the DAG's structure.
8. Click on the "Trigger DAG" button to manually trigger the DAG and run the pipeline.
9. Monitor the progress in Airflow WebUI. 
10. Access PostgreSQL databse using PostgreSQL client.

> Conclusion

The fakestore_pipeline.py script will be automatically executed by Airflow every day at midnight to collect and store data from the FakeStore API. The data pipeline is scalable and capable of handling large volumes of data, and includes data cleaning and transformation steps. The data warehouse is easily accessible to analysts and data scientists through the PostgreSQL database.
