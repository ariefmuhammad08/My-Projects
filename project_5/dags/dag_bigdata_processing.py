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
    'bigdata_processings',
    start_date= days_ago(1),
    schedule_interval= '*/10 * * * *',
    default_args= default_args
) as dag:

    t1= DummyOperator(
        task_id= 'start'
    )

    t2= BashOperator(
        task_id= 'dump_data',
        bash_command= 'python3 /home/ariefmuhammad08/airflow/dags/script/dump.py',
    )

    t3= BashOperator(
        task_id= 'mapreduce_etl',
        bash_command= 'python3 /home/ariefmuhammad08/airflow/dags/script/mapreduce_etl.py',
    )

    t4= DummyOperator(
        task_id= 'stop'
    )

    t1 >> t2 >> t3 >> t4