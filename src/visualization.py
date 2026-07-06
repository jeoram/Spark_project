import os
import matplotlib.pyplot as plt

from src.analytics import revenue_by_hour, avg_tip_by_hour
from src.ingestion import create_spark_session, load_taxi_data
from src.cleaning import clean_taxi_data
from src.feature_engineering import add_features


def build_taxi_pipeline(months=None):
    spark = create_spark_session()
    df = load_taxi_data(spark, months=months or ["01"])
    df = clean_taxi_data(df)
    df = add_features(df)
    return df


def save_hourly_insights(df, output_path="reports/spark_taxi_insights.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    revenue_df = revenue_by_hour(df).toPandas()
    tip_df = avg_tip_by_hour(df).toPandas()

    fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    axes[0].plot(revenue_df["pickup_hour"], revenue_df["revenue"], marker="o", linewidth=2)
    axes[0].set_title("NYC Taxi Total Revenue by Pickup Hour")
    axes[0].set_xlabel("")
    axes[0].set_ylabel("Revenue (USD)")
    axes[0].grid(True, linestyle="--", alpha=0.4)

    axes[1].plot(tip_df["pickup_hour"], tip_df["avg_tip_percent"], marker="o", linewidth=2, color="#2ca02c")
    axes[1].set_title("Average Tip Percentage by Pickup Hour")
    axes[1].set_xlabel("Pickup Hour of Day")
    axes[1].set_ylabel("Average Tip %")
    axes[1].grid(True, linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    print(f"Saved visualization to {output_path}")


def main():
    df = build_taxi_pipeline(months=["01"])
    save_hourly_insights(df)


if __name__ == "__main__":
    main()
