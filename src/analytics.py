from pyspark.sql.functions import col, avg, count, sum as _sum


def revenue_by_hour(df):
    return (
        df.groupBy("pickup_hour")
        .agg(_sum("total_amount").alias("revenue"))
        .orderBy("pickup_hour")
    )


def avg_trip_distance(df):
    return df.select(avg("trip_distance").alias("avg_distance"))


def top_pickup_zones(df):
    return (
        df.groupBy("PULocationID")
        .agg(count("*").alias("trips"))
        .orderBy(col("trips").desc())
        .limit(10)
    )


def avg_tip_by_hour(df):
    return (
        df.groupBy("pickup_hour")
        .agg(avg("tip_percent").alias("avg_tip_percent"))
        .orderBy("pickup_hour")
    )