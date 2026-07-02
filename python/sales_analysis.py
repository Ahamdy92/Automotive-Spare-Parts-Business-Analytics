import pandas as pd


def total_sales(df):

    return df["الاجمالي"].sum()


def monthly_sales(df):

    return df.groupby("الشهر")["الاجمالي"].sum()


def top_products(df):

    return (
        df.groupby("الصنف")["الاجمالي"]
        .sum()
        .sort_values(ascending=False)
    )


def top_customers(df):

    return (
        df.groupby("اسم العميل / المورد")["الاجمالي"]
        .sum()
        .sort_values(ascending=False)
    )
