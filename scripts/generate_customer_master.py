import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Set up Faker
fake = Faker()

# Number of customers to generate
NUM_CUSTOMERS = 1000000  # You can increase this number as needed

# Customer types and statuses
customer_types = ['Regular', 'Premium', 'VIP']
customer_statuses = ['Active', 'Inactive', 'Churned']
genders = ['Male', 'Female', 'Other']

# Generate customer data
customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    customer = {
        'CustomerID': i,
        'Name': fake.name(),
        'Age': random.randint(18, 80),
        'Gender': random.choice(genders),
        'City': fake.city(),
        'State': fake.state(),
        'JoinDate': fake.date_between(start_date='-10y', end_date='today'),
        'Type': random.choice(customer_types),
        'Status': random.choice(customer_statuses)
    }
    customers.append(customer)

# Create DataFrame
customer_df = pd.DataFrame(customers)

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# Save to CSV
customer_df.to_csv('data/customer_master.csv', index=False)

print(f"Generated {NUM_CUSTOMERS} customers and saved to data/customer_master.csv") 