import random
import pandas as pd
from faker import Faker

fake = Faker()

class Customer:
    def __init__(self):
        self.id = fake.unique.random_number(digits=5)
        self.name = fake.name()
        self.email = fake.email()
        self.join_date = fake.date_between(start_date='-3y', end_date='today')

class Account:
    def __init__(self, customer):
        self.id = fake.unique.random_number(digits=5)
        self.customer = customer
        self.balance = round(random.uniform(1000, 50000), 2)

class Transaction:
    def __init__(self, account):
        self.id = fake.unique.random_number(digits=5)
        self.account = account
        self.amount = round(random.uniform(10, 2000), 2)

class Loan:
    def __init__(self, customer):
        self.id = fake.unique.random_number(digits=5)
        self.customer = customer
        self.amount = round(random.uniform(5000, 50000), 2)
        self.term = random.randint(12, 60)  # loan term in months

class Insurance:
    def __init__(self, customer):
        self.id = fake.unique.random_number(digits=5)
        self.customer = customer
        self.type = random.choice(['home', 'auto', 'life'])
        self.premium = round(random.uniform(100, 1000), 2)

class DepositContract:
    def __init__(self, customer):
        self.id = fake.unique.random_number(digits=5)
        self.customer = customer
        self.amount = round(random.uniform(1000, 50000), 2)
        self.term = random.randint(12, 60)  # deposit term in months

def generate_data(n_customers=1000, n_transactions=5000, n_loans=2000, n_insurances=1000, n_deposits=1000):
    # generate customer data
    customers = [Customer() for _ in range(n_customers)]

    # generate account data
    accounts = [Account(customer) for customer in customers]

    # generate transaction data
    transactions = [Transaction(random.choice(accounts)) for _ in range(n_transactions)]

    # generate loan data
    loans = [Loan(random.choice(customers)) for _ in range(n_loans)]

    # generate insurance data
    insurances = [Insurance(random.choice(customers)) for _ in range(n_insurances)]

    # generate deposit contract data
    deposits = [DepositContract(random.choice(customers)) for _ in range(n_deposits)]

    # convert data to pandas DataFrame
    customer_df = pd.DataFrame([customer.__dict__ for customer in customers])
    account_df = pd.DataFrame([account.__dict__ for account in accounts])
    transaction_df = pd.DataFrame([transaction.__dict__ for transaction in transactions])
    loan_df = pd.DataFrame([loan.__dict__ for loan in loans])
    insurance_df = pd.DataFrame([insurance.__dict__ for insurance in insurances])
    deposit_df = pd.DataFrame([deposit.__dict__ for deposit in deposits])

    return customer_df, account_df, transaction_df, loan_df, insurance_df, deposit_df

# generating data
customer_df, account_df, transaction_df, loan_df, insurance_df, deposit_df = generate_data()