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
    'dag_dim',
    start_date= days_ago(1),
    schedule_interval= None,
    default_args= default_args
) as dag:

    t1= DummyOperator(
        task_id= 'start'
    )

    t2= PostgresOperator(
        task_id='dim_currency',
        postgres_conn_id="postgres_default",
        sql='sql/dim_currency.sql',
    )

    t3= PostgresOperator(
        task_id='dim_country',
        postgres_conn_id="postgres_default",
        sql='sql/dim_country.sql',
    )

    t4= PostgresOperator(
        task_id='dim_state',
        postgres_conn_id="postgres_default",
        sql='sql/dim_state.sql',
    )

    t5= PostgresOperator(
        task_id='dim_city',
        postgres_conn_id="postgres_default",
        sql='sql/dim_city.sql',
    )

    t6= DummyOperator(
        task_id= 'stop'
    )

    t2 
    t1 >> t3 >> t4 >> t5 >> t6