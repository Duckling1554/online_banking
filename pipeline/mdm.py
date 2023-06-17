import pandas as pd
from pyspark.sql.functions import coalesce, split, when

def mdm(df1, df2, session):
    df1 = session.createDataFrame(df1)
    df2 = session.createDataFrame(df2)

    # Split the name column in df2 to get first name and last name
    df2 = df2.withColumn("first_name", split(df2["FIRST_NAME"], " ")[0])
    df2 = df2.withColumn("last_name", split(df2["FIRST_NAME"], " ")[1])

    # Join the DataFrames based on the specified columns
    joinedDF = df1.join(df2, ["BIRTH_DATE", "FIRST_NAME", "LAST_NAME"], "outer")

    # Determine the latest "EFF_FROM_DTTM" value between the two DataFrames
    latestEffFromDttm = when(df1["EFF_FROM_DTTM"].isNull(), df2["EFF_FROM_DTTM"]) \
        .when(df2["EFF_FROM_DTTM"].isNull(), df1["EFF_FROM_DTTM"]) \
        .otherwise(when(df1["EFF_FROM_DTTM"] > df2["EFF_FROM_DTTM"], df1["EFF_FROM_DTTM"]).otherwise(df2["EFF_FROM_DTTM"]))

    # Select the desired columns and apply the latestEffFromDttm logic
    finalDF = joinedDF.select(
        coalesce(df1["CUSTOMER_ID"], df2["CUSTOMER_ID"]).alias("CUSTOMER_ID"),
        coalesce(df1["EFF_TO_DTTM"], df2["EFF_TO_DTTM"]).alias("EFF_TO_DTTM"),
        coalesce(df1["CUSTOMER_TYPE"], df2["CUSTOMER_TYPE"]).alias("CUSTOMER_TYPE"),
        coalesce(df1["BIRTH_DATE"], df2["BIRTH_DATE"]).alias("BIRTH_DATE"),
        coalesce(df1["BIRTH_PLACE"], df2["BIRTH_PLACE"]).alias("BIRTH_PLACE"),
        coalesce(df1["FIRST_NAME"], df2["first_name"]).alias("FIRST_NAME"),
        coalesce(df1["LAST_NAME"], df2["last_name"]).alias("LAST_NAME"),
        coalesce(df1["GENDER"], df2["GENDER"]).alias("GENDER"),
        coalesce(df1["MARITAL_STATUS"], df2["MARITAL_STATUS"]).alias("MARITAL_STATUS"),
        coalesce(df1["COUNTRY"], df2["COUNTRY"]).alias("COUNTRY"),
        coalesce(df1["BLACK_LIST_FLG"], df2["BLACK_LIST_FLG"]).alias("BLACK_LIST_FLG"),
        coalesce(df1["REGISTRATION_ADDRESS"], df2["REGISTRATION_ADDRESS"]).alias("REGISTRATION_ADDRESS"),
        coalesce(df1["CHILDREN_CNT"], df2["CHILDREN_CNT"]).alias("CHILDREN_CNT"),
        coalesce(df1["EDUCATION_LVL"], df2["EDUCATION_LVL"]).alias("EDUCATION_LEVEL"),
        coalesce(df1["VIP_FLG"], df2["VIP_FLG"]).alias("VIP_FLG"),
        coalesce(df1["REGISTRATION_DATE"], df2["REGISTRATION_DATE"]).alias("REGISTRATION_DATE"),
        latestEffFromDttm.alias("EFF_FROM_DTTM"),
        coalesce(df1["DELETED_FLG"], df2["DELETED_FLG"]).alias("DELETED_FLG"),
        coalesce(df1["IS_EMPLOYEE"], df2["IS_EMPLOYEE"]).alias("IS_EMPLOYEE"),
        coalesce(df1["ACTUAL_ADDRESS"], df2["ACTUAL_ADDRESS"]).alias("ACTUAL_ADDRESS")

    )

    return finalDF