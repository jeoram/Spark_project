from pyspark.sql.functions import (
    hour, dayofweek, month, col
)


def add_features(df):
    """
    Feature engineering sur les trajets taxi
    """

    df = df.withColumn("pickup_hour", hour("tpep_pickup_datetime"))
    df = df.withColumn("pickup_day", dayofweek("tpep_pickup_datetime"))
    df = df.withColumn("pickup_month", month("tpep_pickup_datetime"))

    # vitesse km/min
    df = df.withColumn(
        "speed",
        col("trip_distance") / col("trip_duration_min")
    )

    # pourboire %
    df = df.withColumn(
        "tip_percent",
        (col("tip_amount") / col("total_amount")) * 100
    )

    # filtre valeurs extrêmes
    df = df.filter(col("speed") < 200)

    return df