from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from google.cloud import bigquery
import os
import pandas as pd

# Set default arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

# Define the DAG and schedule to run daily
with DAG(
    'BQ_table_to_csv_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Fetch Data from BigQuery and Write to local CSV
    def download_and_process_data():

        # Set Google Cloud credentials using environment variable or by absolute path
        google_credentials = "/path/to/service_account.json"
        if google_credentials is None:
            raise ValueError("The environment variable GOOGLE_APPLICATION_CREDENTIALS is not set.")
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_credentials

        # Initialize BigQuery client
        client = bigquery.Client()

        # Query BigQuery Table on Google trends
        # Running example query...
        table_id = "bigquery-public-data.google_trends.international_top_rising_terms" 
        query = f"SELECT * FROM `{table_id}` limit 1000"
        dataframe = client.query(query).to_dataframe()

        # Write to CSV 
        output_path = 'output_BQdata.csv' 
        dataframe.to_csv(output_path, index=False)
        print(f"Data exported to CSV at {output_path}.")

    download_and_process = PythonOperator(
        task_id='download_and_process',
        python_callable=download_and_process_data,
    )

    download_and_process
