from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import os

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define functions for ETL steps

def scrape_data():
    os.system("python3 scraper.py")

def clean_data():
    os.system("python3 dataCleaning.py")

def add_to_dvc():
    os.system("dvc add cleanedData/cleaned_bbc.txt cleanedData/cleaned_dawn.txt")

def commit_to_dvc():
    os.system("dvc commit")

def extract_bbc_data():
    os.system("python3 bbc.py")

def push_to_github():
    os.system("git add . && git commit -m 'Update data in bbc.txt' && git push origin master")

# Define the DAG
dag = DAG(
    'MLOps_dataPIPELINE',
    default_args=default_args,
    description='DAG for scraping, cleaning, and extracting data',
    schedule_interval=timedelta(days=1),  
)

# Define the tasks in the DAG

scrape_data_task = PythonOperator(
    task_id='scrape_data',
    python_callable=scrape_data,
    dag=dag,
)

clean_data_task = PythonOperator(
    task_id='clean_data',
    python_callable=clean_data,
    dag=dag,
)

add_to_dvc_task = PythonOperator(
    task_id='add_to_dvc',
    python_callable=add_to_dvc,
    dag=dag,
)

commit_to_dvc_task = PythonOperator(
    task_id='commit_to_dvc',
    python_callable=commit_to_dvc,
    dag=dag,
)

extract_bbc_data_task = PythonOperator(
    task_id='extract_bbc_data',
    python_callable=extract_bbc_data,
    dag=dag,
)

push_to_github_task = PythonOperator(
    task_id='push_to_github',
    python_callable=push_to_github,
    dag=dag,
)

# Define task dependencies
scrape_data_task >> clean_data_task >> add_to_dvc_task >> commit_to_dvc_task >> extract_bbc_data_task >> push_to_github_task
