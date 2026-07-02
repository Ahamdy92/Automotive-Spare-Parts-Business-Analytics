import pandas as pd


def supplier_cost(df):

    return (
        df.groupby("اسم المورد")["اجمالي التكلفة"]
        .sum()
        .sort_values(ascending=False)
    )


def average_unit_cost(df):

    return (
        df.groupby("الصنف")["تكلفة الوحدة"]
        .mean()
    )
