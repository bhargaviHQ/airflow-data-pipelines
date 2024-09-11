
### Airflow Setup and Commands for Big query project

## View the DAGs List

To view the list of DAGs, use:
```bash
airflow dags list
```

View the Airflow processes

```bash
ps aux | grep airflow
```
Reset and Initialize Airflow Database

```bash
airflow db reset
airflow db init
```

Create a User
```bash
airflow users create \
    --username admin \
    --firstname First \
    --lastname Last \
    --role Admin \
    --email admin@example.com
```

Path to Google Credentials
```bash
export GOOGLE_APPLICATION_CREDENTIALS=""
```

Set Airflow Home
```bash
export AIRFLOW_HOME=airflow-etl-bigquery/airflow_env
```
To run Airflow Standalone
```bash
airflow standalone
```
Or Run the following commands : 


Start the Webserver
```bash
airflow webserver
```

Start the Scheduler
```bash
airflow scheduler
```

Access the Airflow UI: 
http://localhost:8080 (or other port configured).

Install Dependencies

- pip install 'apache-airflow[google]'
- pip install 'apache-airflow[gcp]'
- pip install google-cloud-bigquery

Activate Your Virtual Environment
```bash
source /airflow-etl-bigquery/airflow_env/bin/activate
pip install -r requirements.txt
```