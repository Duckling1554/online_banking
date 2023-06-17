from pyspark.sql import SparkSession
import pandas as pd
from mdm import mdm
from feature_creation import df_collector, feature_creator, data_preprocessing, prediction
import os
import psycopg2

import sys

from set_vars import set_vars

# set_vars()

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

current_dir = os.getcwd()



spark = SparkSession \
    .builder \
    .appName("Python Spark SQL") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.2.10") \
    .getOrCreate()

df1_pandas = pd.read_excel(os.path.join(current_dir, 'onlinebank_customer.xlsx'))
df2_pandas = pd.read_excel(os.path.join(current_dir, 'branches_customer.xlsx'))

df = mdm(df1_pandas,df2_pandas, spark)

customer, transactions, credit_card, loan, account_balance, account = df_collector(df)

df = feature_creator(customer, transactions, credit_card, loan, account_balance, account)

df_scaled = data_preprocessing(df)

df = prediction(df, df_scaled)

print('Successful clustering')

# Drop table
conn = psycopg2.connect(
    database="Bank",
    user=os.environ.get('USER_NAME',''),
    password=os.environ.get('PASSWORD',''),
    host="localhost",
    port="5434"
)

cursor = conn.cursor()
sql = '''DROP TABLE customer '''
cursor.execute(sql)
conn.commit()
conn.close()

print("Table dropped !")


# Add table with new columns
sparkDF = spark.createDataFrame(df)

sparkDF.select("CUSTOMER_ID", "CUSTOMER_TYPE", "up_to_18", "18_to_30", "30_to_45", "after_45", "GENDER", "MARITAL_STATUS", "COUNTRY", "BLACK_LIST_FLG", "CHILDREN_CNT","VIP_FLG", "IS_EMPLOYEE", "CUSTOMER_TRANSACTIONS_CNT", "CUSTOMER_TRANSACTIONS_SUM", "CREDIT_FLG", "CARDS_CNT", "CONTRACT_STATUS (text)", "CONTRACT_TYPE (text)", "CREDIT_CLASS (text)", "MEAN_LOAN_AMT_x", "MEAN_TRANSACTION_x", "TRANSACTION_TO_BALANCE_RATIO", "TRANSACTION_TO_LOAN_RATIO", "Cluster")\
    .write.format("jdbc")\
    .option("url", "jdbc:postgresql://localhost:5434/Bank")\
    .option("driver", "org.postgresql.Driver")\
    .option("dbtable", "customer").option("user", os.environ.get('USER_NAME',''))\
    .option("password", os.environ.get('PASSWORD','')).save()

print("Table uploaded !")