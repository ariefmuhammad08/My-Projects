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
    'dag_mysql',
    start_date= days_ago(1),
    schedule_interval= None,
    default_args= default_args
) as dag:

    t1= DummyOperator(
        task_id= 'start'
    )

    t2= BashOperator(
        task_id= 'dump_data',
        bash_command= 'spark-submit --jars /e/final-project-local/spark/driver/mysql-connector-java-8.0.30.jar --name example_job /e/final-project-local/spark/dumpdata.py'
    )

    t3= BashOperator(
        task_id= 'import_data',
        bash_command= 'spark-submit --jars /e/final-project-local/spark/driver/postgresql-42.5.1.jar,/e/final-project-local/spark/driver/mysql-connector-java-8.0.30.jar --name example_job /e/final-project-local/spark/importdata.py'
    )

    t4= DummyOperator(
        task_id= 'stop'
    )

    t1 >> t2 >> t3 >> t4