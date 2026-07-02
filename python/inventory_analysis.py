import pandas as pd


def inventory_value(df):

    return df["التكلفة"].sum()


def low_stock(df):

    return df[df["الحالة"] == "إعادة طلب"]
