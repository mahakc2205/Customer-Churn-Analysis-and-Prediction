import pandas as pd
import numpy as np
import os
print("Reading CSV files...")
customer_df=pd.read_csv('data/customer_master.csv')
print(f"Customer data :{len(customer_df)} records")

usage_df=pd.read_csv('data/usage_data.csv')
print(f"Usage data:{len(usage_df)} records")

payment_df=pd.read_csv('data/payment_data.csv')
print(f"Payment data :{len(payment_df)} records")

support_df=pd.read_csv('data/support_data.csv')
print(f"Support data:{len(support_df)} records")

print("All files read successfully")

print("\nCleaning and preparing data...")
customer_df['JoinDate']=pd.to_datetime(customer_df['JoinDate'])
usage_df['UsageDate']=pd.to_datetime(usage_df['UsageDate'])
payment_df['PaymentDate']=pd.to_datetime(payment_df['PaymentDate'])
support_df['TicketDate']=pd.to_datetime(support_df['TicketDate'])

payment_df['PaymentMethod']=payment_df['PaymentMethod'].fillna('Not Applicable')

print('Data Cleaning Completed')

print("\nMerging Data...")

merged_df=customer_df.copy()

usage_count=usage_df.groupby('CustomerID')['UsageDate'].count()
print("Number of usage records per customer")
print(usage_count.head())

print("Processing usage data ....")

usage_summary=usage_df.groupby('CustomerID').agg({
    'UsageDate':'count',
    'Amount':['sum','mean'],
    'SessionDuration':['sum','mean']
    
}).round(2)
print("Usage summary created")


usage_summary.columns=['Usage_Count','Total_Amount','Avg_Amount','Total_Duration','Avg_Duration']
usage_summary=usage_summary.reset_index()
print("Usage sumary column name fixed")

print("Processing payment data ...")
payment_summary=payment_df.groupby('CustomerID').agg({
    'BillAmount':['sum','mean'],
    'PaymentStatus':lambda x:(x=='Missed').sum()
}).round(2)
print("Payment summary created")

payment_summary.columns = ['Total_BillAmount', 'Avg_BillAmount', 'Missed_Payments']
payment_summary = payment_summary.reset_index()

print("Payment summary column names fixed")

print("Processing support data")
support_summary=support_df.groupby('CustomerID').agg({

    'TicketDate':'count',
    'ResolutionTime':'mean',
    'Satisfaction':lambda x:(x=='Unsatisfied').sum()
}).round(2)

print("Support summary created")


support_summary_columns=['Support_Tickets','Avg_ResolutionTime','Unsatisfied_Count']
support_summary=support_summary.reset_index()
print("Support summary column names fixed")

print("Merging all data...")

merged_df=merged_df.merge(usage_summary,on='CustomerID',how='left')
print("usage data added")

merged_df=merged_df.merge(payment_summary,on="CustomerID",how="left")
print("payment data added")


merged_df=merged_df.merge(support_summary,on="CustomerID",how="left")
print("support data added")


print(f"\nFinal merged data shape:{merged_df.shape}")
print("Column in merged data :")
print(merged_df.columns.tolist())

os.makedirs('data',exist_ok=True)
merged_df.to_csv('data/merged_customer_data.csv',index=False)

print("Merged data saved to data/merged_customer_data.csv")

print("Data integration completed!")



