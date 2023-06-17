import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from config import settings
import os

current_dir = os.getcwd()



def df_collector():
    customer = pd.read_excel(os.path.join(current_dir, 'Данные.xlsx'), sheet_name='CUSTOMER')
    transactions = pd.read_excel(os.path.join(current_dir, 'Данные.xlsx'), sheet_name='TRANSACTION')
    credit_card = pd.read_excel(os.path.join(current_dir, 'Данные.xlsx'), sheet_name='CARD')
    loan =  pd.read_excel(os.path.join(current_dir, 'Данные.xlsx'), sheet_name='Loan')
    account_balance =  pd.read_excel(os.path.join(current_dir, 'Данные.xlsx'), sheet_name='ACCOUNT_BALANCE')
    account = pd.read_excel(os.path.join(current_dir, 'Данные.xlsx'), sheet_name='ACCOUNT')

    return customer, transactions, credit_card, loan, account_balance, account


def feature_creator(customer, transactions, credit_card, loan, account_balance, account):

    customer['AGE_CATEGORY'] = datetime.now().year - pd.to_datetime(customer[' BIRTH_DATE (date']).dt.year
    customer['up_to_18'] = customer['AGE_CATEGORY'].apply(lambda x: 1 if x <= 18 else 0)
    customer['18_to_30'] = customer['AGE_CATEGORY'].apply(lambda x: 1 if x in range(19, 30) else 0)
    customer['30_to_45'] = customer['AGE_CATEGORY'].apply(lambda x: 1 if x in range(31, 45) else 0)
    customer['after_45'] = customer['AGE_CATEGORY'].apply(lambda x: 1 if x > 45 else 0)

    amount_of_transactions = transactions.groupby('CUSTOMER_ID (int')['TRANSACTION_ID (int) '].count().reset_index()
    sum_of_transactions = transactions.groupby('CUSTOMER_ID (int')[' TRANSACTION_AMT (decimal(24,4'].sum().rename('CUSTOMER_TRANSACTIONS_SUM').reset_index()
    mean_of_transactions = transactions.groupby('CUSTOMER_ID (int')[' TRANSACTION_AMT (decimal(24,4'].mean().rename('MEAN_TRANSACTION').reset_index()
    transactions_agg = pd.merge(amount_of_transactions, sum_of_transactions, on='CUSTOMER_ID (int'\
                                , how='inner')
    transactions_agg = pd.merge(transactions_agg, mean_of_transactions, on='CUSTOMER_ID (int'\
                                , how='inner')
    transactions_agg.rename(columns={'TRANSACTION_ID (int) ': 'CUSTOMER_TRANSACTIONS_CNT'}\
                        ,inplace= True)
    
    credit_card['CREDIT_FLG'] = credit_card['CARD_TYPE (text'].apply(lambda x : 1 if x == "C" else 0)
    card_agg = credit_card.groupby('CUSTOMER_ID (int)')['CARD_ID (int) '].count().reset_index()
    card_agg = pd.merge(card_agg, credit_card[['CUSTOMER_ID (int)', 'CREDIT_FLG']], on='CUSTOMER_ID (int)'\
                        , how='inner')
    card_agg.rename(columns={'CARD_ID (int) ':'CARDS_CNT'}, inplace=True)

    loan_agg = loan.groupby('CUSTOMER_ID (int)')['LOAN_AMT (decimal(24,4))'].mean().reset_index()
    loan_agg.rename(columns={'LOAN_AMT (decimal(24,4))':'MEAN_LOAN_AMT'}, inplace=True)

    balance_agg = account_balance.groupby('ACCOUNT_ID (int')[' BALANCE_AMT (decimal(24,4'].mean().rename('MEAN_BALANCE').reset_index()
    balance_agg = pd.merge(balance_agg, account[['ACCOUNT_ID (int', ' CUSTOMER_ID (int']], how='left', on='ACCOUNT_ID (int')
    balance_agg = pd.merge(balance_agg, transactions_agg[['MEAN_TRANSACTION', 'CUSTOMER_ID (int']], how='left', left_on=' CUSTOMER_ID (int',\
                        right_on='CUSTOMER_ID (int')
    balance_agg = pd.merge(balance_agg, loan_agg[['MEAN_LOAN_AMT', 'CUSTOMER_ID (int)']], how='left', left_on=' CUSTOMER_ID (int',\
                        right_on='CUSTOMER_ID (int)')
    balance_agg['TRANSACTION_TO_BALANCE_RATIO'] = balance_agg['MEAN_TRANSACTION']/balance_agg['MEAN_BALANCE']
    balance_agg['TRANSACTION_TO_LOAN_RATIO'] = balance_agg['MEAN_LOAN_AMT']/balance_agg['MEAN_BALANCE']
    df = pd.merge(customer, transactions_agg, right_on='CUSTOMER_ID (int', left_on='CUSTOMER_ID (int) ', how='left')
    df = pd.merge(df, card_agg, right_on='CUSTOMER_ID (int)', left_on='CUSTOMER_ID (int) ', how='left')
    df = pd.merge(df, loan_agg, right_on='CUSTOMER_ID (int)', left_on='CUSTOMER_ID (int) ', how='left')
    df = pd.merge(df, balance_agg, right_on='CUSTOMER_ID (int', left_on='CUSTOMER_ID (int) ', how='left')
    df = pd.merge(df, loan, right_on='CUSTOMER_ID (int)', left_on='CUSTOMER_ID (int) ', how='left')

    return df[settings.TRAIN_FEATURES.TRAIN_FEATURES]


def data_preprocessing(df):
    df_dummies = pd.get_dummies(df[settings.TRAIN_FEATURES.CATEGORICAL_COLUMNS])
    df = pd.concat([df, df_dummies], axis=1)
    df.drop(settings.TRAIN_FEATURES.CATEGORICAL_COLUMNS, axis=1, inplace=True)
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df)

    return scaled_features
    

def prediction(df, normalized_df):
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(normalized_df)
    cluster_labels = kmeans.labels_
    df['Cluster'] = cluster_labels

    return df



