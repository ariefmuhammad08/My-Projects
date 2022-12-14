from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.utils.dates import days_ago

default_args= {
    'owner' : 'admin'
}

with DAG(
    'dag_fact_monthly',
    start_date= days_ago(1),
    schedule_interval= '@monthly',
    default_args= default_args
) as dag:

    t1= DummyOperator(
        task_id= 'start'
    )

    t2= PostgresOperator(
        task_id='fact_currency_monthly',
        postgres_conn_id="postgres_default",
        sql='fact_currency_monthly_avg.sql',
    )

    t3= DummyOperator(
        task_id= 'stop'
    )

     
    t1 >> t2 >> t3