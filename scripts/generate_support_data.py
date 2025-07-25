import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake=Faker()
NUM_SUPPORT_RECORDS=8000

issue_types=['Transaction','Login','Card','Service','Other']
satisfaction_levels=['Satisfied','Neutral','Unsatisfied']

customer_df=pd.read_csv('data/customer_master.csv')
customer_ids=customer_df['CustomerID'].to_list()

support_records=[]

for i in range(NUM_SUPPORT_RECORDS):
    customer_id=random.choice(customer_ids)
    ticket_date=fake.date_between(start_date='-2y',end_date='today')
    issue_type=random.choice(issue_types)
    resolution_time=round(np.random.uniform(1,72),1)
    satisfaction=random.choice(satisfaction_levels)
    record={
        'CustomerID':customer_id,
        'TicketDate':ticket_date,
        'IssueType':issue_type,
        'ResolutionTime':resolution_time,
        'Satisfaction':satisfaction
    }
    support_records.append(record)
support_df=pd.DataFrame(support_records)
os.makedirs('data',exist_ok=True)
support_df.to_csv('data/support_data.csv',index=False)

print(f'Generated {NUM_SUPPORT_RECORDS} support records and saved to data/support_data.csv')



    