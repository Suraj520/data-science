# mandatory imports
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint
def pick_best_model(task_id):
    accuracies = task_id.xcom_pull(task_id=[
        'training_model_A',
        'training_model_B',
        'training_model_C'
    ])

    if max(accuracies)>9:
        return 'accurate'
    return 'inaccurate'

def train_model(model):
    return randint(1,10) # dummy accuracy of model

with DAG("train",start_date= datetime(2023,3,26), schedule_interval="@daily", catchup=False) as dag:
        training_model_A = PythonOperator(
                    task_id="training_model_A",
                    python_callable=train_model
        )

        training_model_B = PythonOperator(
            task_id="training_model_B",
            python_callable=train_model
        )

        training_model_C = PythonOperator(
            task_id="training_model_C",
            python_callable=train_model
        )

        training_model_D = PythonOperator(
            task_id="training_model_D",
            python_callable=train_model
        )

        training_model_E = PythonOperator(
            task_id="training_model_E",
            python_callable=train_model
        )

        choose_best_model = BranchPythonOperator(
             task_id ="Pick_best_model",
             python_callable = pick_best_model,
        )

        accurate = BashOperator(
             task_id = "accurate",
             bash_command = "echo 'accurate'"
        )
        inaccurate = BashOperator(
             task_id = "inaccurate",
             bash_command = "echo 'inaccurate'"
        )


        [training_model_A,training_model_B,training_model_C,training_model_D,training_model_E]>> pick_best_model >> [accurate,inaccurate]


        #Reference - https://www.youtube.com/watch?v=IH1-0hwFZRQ