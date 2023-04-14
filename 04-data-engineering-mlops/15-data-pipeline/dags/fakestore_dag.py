from datetime import datetime, timedelta
import requests
import pandas as pd
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define API URL
api_url = "https://fakestoreapi.com"

# Define function to get data from API
def get_data(endpoint):
    url = f"{api_url}/{endpoint}"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

# Define function to clean data
def clean_data(df, endpoint):
    if endpoint == "products":
        # Rename columns
        df.columns = ["product_id", "title", "price", "description", "category", "image"]

        # Convert price to float
        df["price"] = df["price"].astype(float)

    elif endpoint == "reviews":
        # Rename columns
        df.columns = ["review_id", "product_id", "user_id", "rating", "comment", "created_at"]

        # Convert created_at to datetime
        df["created_at"] = pd.to_datetime(df["created_at"])

    return df

# Define function to load data to database
def load_data(df, table_name):
    # Connect to database
    engine = create_engine("postgresql://username:password@localhost:5432/database")

    # Load data to database
    df.to_sql(table_name, engine, if_exists="append", index=False)

# Define function to run pipeline
def run_pipeline():
    # Get current date
    date = datetime.now().strftime("%Y-%m-%d")

    # Get data from API
    products_df = get_data("products")
    reviews_df = get_data("reviews")

    # Clean data
    products_df = clean_data(products_df, "products")
    reviews_df = clean_data(reviews_df, "reviews")

    # Add date column
    products_df["date"] = date
    reviews_df["date"] = date

    # Load data to database
    load_data(products_df, "products")
    load_data(reviews_df, "reviews")

# Define DAG arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define DAG
dag = DAG(
    'fakestore_dag',
    default_args=default_args,
    description='Collects and stores data from FakeStore API',
    schedule_interval=timedelta(days=1),
)

# Define tasks
t1 = PythonOperator(
    task_id='run_pipeline',
    python_callable=run_pipeline,
    dag=dag
)

# Set task dependencies
t1

