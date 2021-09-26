# import sys, os
# sys.path.append(os.getcwd())
# print(os.getcwd())

from datetime import timedelta 
from textwrap import dedent

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from func import func1

default_args = {
  'owner': 'airflow',
  'depends_on_past': False,
  'email': ['pjt3591oo@naver.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'reties': 1,
  'retry_delay': timedelta(minutes=3)
}

with DAG (
  'dag_id',
  default_args=default_args,
  description='PythonOperator',
  schedule_interval=timedelta(minutes=10),
  start_date=days_ago(2),
  tags=['example']
) as dag:

  t1 = PythonOperator(
    task_id='task_1',
    python_callable=func1,
    depends_on_past=True,
    provide_context=True,
    params={"a": 10, "b": 20}
  )

  t1