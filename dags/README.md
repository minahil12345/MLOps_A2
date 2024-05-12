# Data Pipeline with Apache Airflow

## Introduction
This README.md file provides detailed documentation on setting up and running a data pipeline using Apache Airflow. The data pipeline consists of several tasks, including data extraction, cleaning, integration with DVC, Google Drive, and GitHub.

## Setup
### 1. Installation
- Install Apache Airflow using the following command:
- Initialize the Airflow database:

### 2. Project Structure
- Create a new directory for the project.
- Inside the project directory, create the following subdirectories:
- `dags`: Contains the Airflow DAG definition files.
- `scripts`: Contains the Python scripts for data extraction, cleaning, and integration.
- `data`: Contains the raw data files.
- `cleanedData`: Contains the cleaned data files.
- `credentials`: Contains any necessary credentials files.

### 3. Configuration
- Configure Airflow settings, such as the executor, connections, and variables, in the `airflow.cfg` file.

## Running the Pipeline
### 1. Starting Airflow Webserver and Scheduler
- Start the Airflow webserver:
- Start the Airflow scheduler:

### 2. Triggering the DAG
- Access the Airflow web UI in your browser.
- Navigate to the DAGs page and locate the data pipeline DAG.
- Toggle the DAG to ON to enable scheduling.
- Trigger the DAG manually or wait for it to be triggered based on the schedule interval.

### 3. Monitoring the Pipeline
- Monitor the progress of the data pipeline in the Airflow web UI.
- View task logs, status, and dependencies to identify any issues or failures.


## Code Overview
The data pipeline consists of the following components:
- `scraper.py`: Python script for data scraping from websites.
- `dataCleaning.py`: Python script for cleaning the extracted data.
- `bbc.py`: Python script for extracting data from the BBC website.
- `DAGs`: Contains Airflow DAG definition files.
- `README.md`: Documentation file providing instructions for setting up and running the data pipeline with Apache Airflow.
