import requests
import os
from pyspark.sql import SparkSession

NYC_TAXI_BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/"


def create_spark_session(app_name="NYC Taxi Project"):
    return (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .getOrCreate()
    )


def download_file(url, local_path):
    if not os.path.exists(local_path):
        print(f"Downloading {url}")
        r = requests.get(url)
        with open(local_path, "wb") as f:
            f.write(r.content)


def load_taxi_data(spark, months=None, year="2023"):
    if months is None:
        months = ["01"]

    dfs = []

    os.makedirs("data/raw", exist_ok=True)

    for m in months:
        url = f"{NYC_TAXI_BASE_URL}yellow_tripdata_{year}-{m}.parquet"
        local_path = f"data/raw/yellow_tripdata_{year}-{m}.parquet"

        download_file(url, local_path)

        df = spark.read.parquet(local_path)
        dfs.append(df)

    full_df = dfs[0]
    for df in dfs[1:]:
        full_df = full_df.unionByName(df)

    return full_df