from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator



def print_hello():
    return 'Hello world!'

dag = DAG('hello_world', description='Simple tutorial DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2019, 7, 12), catchup=False)

bash_task = BashOperator(task_id='bash_task', bash_command="echo 'command executed from BashOperator'")

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

bash_task >> hello_operator
