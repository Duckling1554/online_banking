from pyspark.sql import SparkSession
import pandas as pd
from mdm import mdm
from feature_creation import df_collector, feature_creator, data_preprocessing, prediction
import os


current_dir = os.getcwd()



spark = SparkSession \
    .builder \
    .appName("Python Spark SQL") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.2.10") \
    .getOrCreate()

df1_pandas = pd.read_excel(os.path.join(current_dir, 'onlinebank_customer.xlsx'))
df2_pandas = pd.read_excel(os.path.join(current_dir, 'branches_customer.xlsx'))

df = mdm(df1_pandas,df2_pandas, spark)

customer, transactions, credit_card, loan, account_balance, account = df_collector()

df = feature_creator(customer, transactions, credit_card, loan, account_balance, account)

df_scaled = data_preprocessing(df)

df = prediction(df, df_scaled)



print(df)
