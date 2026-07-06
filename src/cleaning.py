from pyspark.sql.functions import col, unix_timestamp


def clean_taxi_data(df):
    """
    Nettoyage des données NYC Taxi
    """

    df_clean = (
        df
        .filter(col("trip_distance") > 0)
        .filter(col("fare_amount") > 0)
        .filter(col("total_amount") > 0)
        .filter(col("tpep_pickup_datetime").isNotNull())
        .filter(col("tpep_dropoff_datetime").isNotNull())
    )

    # durée du trajet (en minutes)
    df_clean = df_clean.withColumn(
        "trip_duration_min",
        (unix_timestamp("tpep_dropoff_datetime") -
         unix_timestamp("tpep_pickup_datetime")) / 60
    )

    # filtre durée aberrante
    df_clean = df_clean.filter(
        (col("trip_duration_min") > 1) &
        (col("trip_duration_min") < 180)
    )

    return df_clean