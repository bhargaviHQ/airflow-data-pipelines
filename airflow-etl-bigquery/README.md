
### Airflow Setup and Commands for Big query project

## Description

- **`airflow_env/`**: Contains the setup for the Airflow environment including binaries, configuration files, and logs (will be created after initializing the environment).
  - **`bin/`**: Directory for Airflow binaries.
  - **`etc/`**: Directory for configuration files.
  - **`logs/`**: Directory where Airflow logs are stored.
  - **`airflow.cfg`**: The main configuration file for Airflow.

- **`DAG/`**: Directory for Airflow Directed Acyclic Graphs (This is included in the repository).
  - **`bigquery_data_pipeline.py`**: DAG file for a data pipeline involving BigQuery.

- **`requirements.txt`**: List Python dependencies required for the project.

## Setup Instructions

1. **Airflow Environment Setup**
   - Ensure that the Airflow environment is properly configured and set up using the files in `airflow_env/`.

    - Provide Path to Google Credentials
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS=""
    ```

    - Set Airflow Home
    ```bash
    export AIRFLOW_HOME=airflow-etl-bigquery/airflow_env
    ```

    - Activate Virtual Environment
    ```bash
    source /airflow-etl-bigquery/airflow_env/bin/activate
    pip install -r requirements.txt
    ```

2. **Dependencies**
    - Install any additional Python packages listed in `requirements.txt`:

     ```bash
     pip install -r requirements.txt
     ```
    - Install Dependencies

    - pip install 'apache-airflow[google]'
    - pip install 'apache-airflow[gcp]'
    - pip install google-cloud-bigquery

3. **Configuration**

    - Reset and Initialize Airflow Database

    ```bash
    airflow db reset
    airflow db init
    ```

    - Create a User
    ```bash
    airflow users create \
        --username admin \
        --firstname First \
        --lastname Last \
        --role Admin \
        --email admin@example.com
    ```


4. **Deploying DAGs**
   - DAG file `bigquery_data_pipeline.py` is present in `airflow_env/dags/` directory.

5. **Running Airflow**
   - Start the Airflow scheduler and web server using the binaries located in `airflow_env/bin/`.
   - To run Airflow Standalone
    ```bash
    airflow standalone
    ```
   - Or Run the following commands : 


   - Start the Webserver
    ```bash
    airflow webserver
    ```

   - Start the Scheduler
    ```bash
    airflow scheduler
    ```

    - Access the Airflow UI: http://localhost:8080 (or other port configured).


### Other commands
- To view the list of DAGs, use:
```bash
airflow dags list
```

- View the Airflow processes

```bash
ps aux | grep airflow
```
