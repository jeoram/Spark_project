

def optimize_dataframe(df):
    """
    Optimisation Spark (cache, partitioning)
    """

    # cache
    df = df.cache()

    # repartition pour parallélisme
    df = df.repartition(8)

    return df


def show_execution_plan(df):
    """
    Affiche le plan Spark (important en entretien)
    """
    df.explain(True)