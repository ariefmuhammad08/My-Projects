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
    'dag_fact_daily',
    start_date= days_ago(1),
    schedule_interval= '@daily',
    default_args= default_args
) as dag:

    t1= DummyOperator(
        task_id= 'start'
    )

    t2= PostgresOperator(
        task_id='fact_total_state',
        postgres_conn_id="postgres_default",
        sql='fact_total_state.sql',
    )

    t3= PostgresOperator(
        task_id='fact_currency_daily',
        postgres_conn_id="postgres_default",
        sql='fact_currency_daily_avg.sql',
    )

    t4= DummyOperator(
        task_id= 'stop'
    )

     
    t1 >> t2 >> t3 >> t4