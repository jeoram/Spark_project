from src.ingestion import create_spark_session, load_taxi_data
from src.cleaning import clean_taxi_data
from src.feature_engineering import add_features
from src.optimization import optimize_dataframe, show_execution_plan


def main():

    spark = create_spark_session()

    # 1. ingestion
    df = load_taxi_data(spark, months=["01", "02", "03"])

    # 2. cleaning
    df = clean_taxi_data(df)

    # 3. features
    df = add_features(df)

    # 4. optimization
    df = optimize_dataframe(df)

    # 5. debug plan
    show_execution_plan(df)

    df.show(5)


if __name__ == "__main__":
    main()