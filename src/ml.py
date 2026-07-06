from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression


def prepare_ml_data(df):
    """
    Prépare features pour ML
    """

    assembler = VectorAssembler(
        inputCols=[
            "trip_distance",
            "trip_duration_min",
            "pickup_hour",
            "passenger_count"
        ],
        outputCol="features"
    )

    return assembler.transform(df).select("features", "total_amount")


def train_price_model(df):
    """
    Modèle de régression pour prédire le prix
    """

    lr = LinearRegression(
        featuresCol="features",
        labelCol="total_amount"
    )

    model = lr.fit(df)

    return model


def evaluate_model(model, df):
    """
    Évaluation simple du modèle
    """

    predictions = model.transform(df)

    return predictions.select("prediction", "total_amount")