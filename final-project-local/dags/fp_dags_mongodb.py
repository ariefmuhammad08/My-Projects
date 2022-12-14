from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from airflow.utils.dates import days_ago

default_args= {
    'owner' : 'admin'
}

with DAG(
    'dag_mongodb',
    start_date= days_ago(1),
    schedule_interval= None,
    default_args= default_args
) as dag:

    t1= DummyOperator(
        task_id= 'start'
    )

    t2= BashOperator(
        task_id= 'dump_data',
        bash_command= 'python3 /e/final-project-local/mongodb/dumpdata.py'
    )

    t3= DummyOperator(
        task_id= 'stop'
    )

    t1 >> t2 >> t3