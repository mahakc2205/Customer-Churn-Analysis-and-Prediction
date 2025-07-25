import pandas as pd
import numpy as np
from faker import Faker
import random
import os
from pandas import Timedelta

fake=Faker()

NUM_PAYMENTS=20000

payment_statuses=['Paid','Late','Missed']
payment_methods=['Card','NetBanking','UPI','Cash','Cheque']
customer_df=pd.read_csv('data/customer_master.csv')
customer_ids=customer_df['CustomerID'].tolist()

payment_records=[]
for i in range(NUM_PAYMENTS):
    customer_id=np.random.choice(customer_ids)
    bill_date=pd.to_datetime(fake.date_between(start_date='-2y',end_date='today'))
    bill_amount=round(np.random.uniform(100,10000),2)
    payment_status=random.choice(payment_statuses)

    if payment_status=='Paid':
        payment_date=bill_date+Timedelta(days=random.randint(0,10))
        payment_method=random.choice(payment_methods)
    
    elif payment_status=='Late':
        payment_date=bill_date+Timedelta(days=random.randint(11,30))
        payment_method=random.choice(payment_methods)

    else:
        payment_date=None
        payment_method=None
    
    record={
        'CustomerID':customer_id,
        'BillDate':bill_date,
        'BillAmount':bill_amount,
        'PaymentStatus':payment_status,
        'PaymentDate':payment_date,
        'PaymentMethod':payment_method
    }
    payment_records.append(record)
    if i %100==0:
        print(f'Generated{i} records')

payment_df=pd.DataFrame(payment_records)
os.makedirs('data',exist_ok=True)
payment_df.to_csv('data/payment_data.csv',index=False)
print(f"Generated {NUM_PAYMENTS} payment records and saved to data/payment_data.csv")