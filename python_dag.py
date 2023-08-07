from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from time import sleep
from datetime import datetime
def my_func(*op_args):
  print(op_args)
  return op_args[0]

dag = DAG('python_dag', description='Simple tutorial DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2019, 7, 12), catchup=False)
dummy_task      = DummyOperator(task_id='dummy_task', retries=3, dag=dag)
python_task     = PythonOperator(task_id='python_task', python_callable=my_func, op_args=['one', 'two', 'three'], dag=dag)
dummy_task >> python_task
