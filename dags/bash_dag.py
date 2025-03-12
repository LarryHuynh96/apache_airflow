from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {"owner": "airflow", "retries": 3, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="bash_dag_v3",
    default_args=default_args,
    description="This is the DAG that runs for BashOperator",
    start_date=datetime(2025, 3, 11, 6, 0),
    schedule_interval="0 6 * * *",
) as dag:

    task1 = BashOperator(
        task_id="say_hello_task",
        bash_command="echo hello world, this is the first task with airflow",
    )

    task2 = BashOperator(
        task_id="task_2",
        bash_command="echo This is task 2",
    )

    task3 = BashOperator(
        task_id="task_3",
        bash_command="echo This is task 3",
    )

    task1 >> [task2, task3]
