import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Set up Faker
fake = Faker()

# Decide how many usage records you want to generate
NUM_USAGE_RECORDS = 100000  # 1 lakh usage records

# Define possible service types for banking
services = ['Mobile App', 'Website', 'ATM', 'Branch Visit']

# Load customer IDs from the customer master CSV
customer_df = pd.read_csv('data/customer_master.csv')
customer_ids = customer_df['CustomerID'].tolist()

# Prepare to store all usage records
usage_records = []
for _ in range(NUM_USAGE_RECORDS):
    record={
        'CustomerID':random.choice(customer_ids),
        'UsageDate':fake.date_between(start_date='-2y',end_date='today'),
        'Service':random.choice(services),
        'Amount':round(np.random.uniform(10,1000),2),
        'SessionDuration':np.random.randint(1,121)
    }
    usage_records.append(record)

usage_df=pd.DataFrame(usage_records)
os.makedirs('data',exist_ok=True)
usage_df.to_csv('data/usage_data.csv',index=False)
print(f"Generated {NUM_USAGE_RECORDS} usage records and saved to data/usage_data.csv")