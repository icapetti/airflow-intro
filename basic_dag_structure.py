######### Libraries #########

# Airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.email import send_email

# Python
from datetime import datetime, timedelta
from utils.email import notify_email
#from utils.db import insert_row, get_engine

######### args definition #########
args = {
    'owner':''
    , 'emails':['']
    , 'on_failure_callback':notify_email
    , 'depends_on_past': False
    , 'start_date': datetime(year=2021, month=3, day=20)
}

######### Functions definition #########
def first_function():
    print('Hello')

def last_function():
    print('Bye')

# DAG definition
dag = DAG(
    dag_id = ''
    , default_args = args
    , schedule_interval = '0 15 * * *'
)

######### Tasks definition #########
# One task for each python function defined on last step
first_function = PythonOperator(
    task_id = 'first_function'
    , python_callable = first_function
    , dag = dag
    , provide_context = True
)

last_function = PythonOperator(
    task_id = 'last_function'
    , python_callable = last_function
    , dag = dag
    , provide_context = True
)

######### Tasks order definition #########
first_function >> last_function