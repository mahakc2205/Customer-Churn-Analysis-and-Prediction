# Customer Churn Prediction & Retention Analytics Project

## Project Overview
Build a realistic, end-to-end data analytics platform that predicts customer churn and helps understand customer behavior, using simulated data and real data engineering/analytics tools.

## Why?
- Retaining customers is cheaper than acquiring new ones.
- Understanding churn helps improve products, services, and revenue.
- This project demonstrates real-world data engineering and analytics skills.

## Tools & Technologies
- Python (pandas, numpy, faker)
- Python scripts (no Jupyter notebooks)
- CSV files (for data storage and sharing)
- SQL (for querying and analysis)
- Git & GitHub (with .gitignore for large files)

## Project Structure
- `data/` - All CSVs (raw/generated, ignored by git)
- `scripts/` - Python scripts
- `notebooks/` - (Unused, placeholder only)

## .gitignore Explained
The project uses a .gitignore file to keep the repository clean and efficient. It ignores:
- All files in the `data/` folder (including large datasets)
- All `.csv` files anywhere in the project
- Python virtual environments (`venv/`, `.env/`)
- Python bytecode files (`__pycache__/`, `*.pyc`, `*.pyo`)
- VS Code settings (`.vscode/`)
- OS-specific junk files (`.DS_Store`, `Thumbs.db`)

## Workflow So Far
1. **Project Structure:** Set up folders for data, scripts, and (optionally) notebooks. Added `.gitkeep` files to track empty folders.
2. **.gitignore:** Configured to ignore all data files, CSVs, virtual environments, Python bytecode, and editor/system files. Jupyter-related ignores removed since not using Jupyter.
3. **requirements.txt:** Added `pandas`, `numpy`, and `faker` for data generation and analysis.
4. **README.md:** Maintained with project overview and instructions.
5. **Customer Data Generation Script:** Created `scripts/generate_customer_master.py` to generate fake customer data (10,000 or 1,000,000+ records) and save as `data/customer_master.csv` (which is ignored by git).
6. **Usage/Activity Data Generation Script:** Created `scripts/generate_usage_data.py` to generate fake usage/activity records (e.g., 100,000 records) and save as `data/usage_data.csv` (also ignored by git).
7. **Payment/Billing Data Generation Script:** Created `scripts/generate_payment_data.py` to generate fake payment/billing records (e.g., 20,000 records) and save as `data/payment_data.csv` (also ignored by git).
8. **Support/Complaint Data Generation Script:** Created `scripts/generate_support_data.py` to generate fake support/complaint records (e.g., 8,000 records) and save as `data/support_data.csv` (also ignored by git).
9. **Data Integration Script:** Created `scripts/data_integration.py` to read, clean, and merge all generated datasets into a unified customer dataset for analysis.
10. **Version Control:** All code/scripts and config files are tracked and pushed to GitHub. Data files are ignored for efficiency.

## Customer Master Data Generation (Detailed)
The script `scripts/generate_customer_master.py` creates a large, realistic customer master dataset for analysis. Here's what it does:

- **Imports Required Libraries:** Uses `pandas` for data handling, `faker` for generating fake but realistic data, and `random` for random choices.
- **Sets Number of Customers:** You can choose how many customers to generate (e.g., 10,000 or 1,000,000).
- **Defines Customer Attributes:**
  - CustomerID: Unique number for each customer
  - Name: Randomly generated name
  - Age: Random age between 18 and 80
  - Gender: Randomly chosen from Male, Female, Other
  - City/State: Randomly generated city and state
  - JoinDate: Random date in the last 10 years
  - Type: Randomly chosen from Regular, Premium, VIP
  - Status: Randomly chosen from Active, Inactive, Churned
- **Generates Data:** Loops through the desired number of customers, creating a dictionary for each with the above attributes.
- **Creates a DataFrame:** Converts the list of customer dictionaries into a pandas DataFrame (like a table).
- **Ensures Data Folder Exists:** Uses `os.makedirs('data', exist_ok=True)` to make sure the `data/` folder is present.
- **Saves as CSV:** Writes the DataFrame to `data/customer_master.csv`.
- **Prints a Message:** Lets you know the file was created and where it's saved.

**Note:** The generated CSV is ignored by git and not uploaded to GitHub, keeping your repository clean.

## Usage/Activity Data Generation (Detailed)
The script `scripts/generate_usage_data.py` creates a large, realistic usage/activity dataset for analysis. Here's what it does:

- **Imports Required Libraries:** Uses `pandas`, `numpy`, `faker`, and `random` for data generation and handling.
- **Sets Number of Usage Records:** You can choose how many usage/activity records to generate (e.g., 100,000).
- **Defines Usage Attributes:**
  - CustomerID: Randomly selected from real customers in the master data
  - UsageDate: Random date in the last 2 years
  - Service: Randomly chosen from ['Mobile App', 'Website', 'ATM', 'Branch Visit']
  - Amount: Random float between 10 and 1000 (2 decimal places) - represents service usage fees
  - SessionDuration: Random integer between 1 and 120 (minutes)
- **Generates Data:** Loops through the desired number of usage records, creating a dictionary for each with the above attributes.
- **Creates a DataFrame:** Converts the list of usage dictionaries into a pandas DataFrame.
- **Ensures Data Folder Exists:** Uses `os.makedirs('data', exist_ok=True)` to make sure the `data/` folder is present.
- **Saves as CSV:** Writes the DataFrame to `data/usage_data.csv`.
- **Prints a Message:** Lets you know the file was created and where it's saved.

**Note:** The generated CSV is ignored by git and not uploaded to GitHub, keeping your repository clean.

## Payment/Billing Data Generation (Detailed)
The script `scripts/generate_payment_data.py` creates a large, realistic payment/billing dataset for analysis. Here's what it does:

- **Imports Required Libraries:** Uses `pandas`, `numpy`, `faker`, and `random` for data generation and handling.
- **Sets Number of Payment Records:** You can choose how many payment/billing records to generate (e.g., 20,000).
- **Defines Payment Attributes:**
  - CustomerID: Randomly selected from real customers in the master data
  - BillDate: Random date in the last 2 years
  - BillAmount: Random float between 100 and 10,000 (2 decimal places)
  - PaymentStatus: Randomly chosen from ['Paid', 'Late', 'Missed']
  - PaymentDate: If Paid, 0–10 days after BillDate; if Late, 11–30 days after BillDate; if Missed, left empty
  - PaymentMethod: Randomly chosen from ['Card', 'NetBanking', 'UPI', 'Cash', 'Cheque'] if Paid or Late; left empty if Missed
- **Generates Data:** Loops through the desired number of payment records, creating a dictionary for each with the above attributes and logic for payment status.
- **Creates a DataFrame:** Converts the list of payment dictionaries into a pandas DataFrame.
- **Ensures Data Folder Exists:** Uses `os.makedirs('data', exist_ok=True)` to make sure the `data/` folder is present.
- **Saves as CSV:** Writes the DataFrame to `data/payment_data.csv`.
- **Prints a Message:** Lets you know the file was created and where it's saved.

**Note:** The generated CSV is ignored by git and not uploaded to GitHub, keeping your repository clean.

## Support/Complaint Data Generation (Detailed)
The script `scripts/generate_support_data.py` creates a large, realistic support/complaint dataset for analysis. Here's what it does:

- **Imports Required Libraries:** Uses `pandas`, `numpy`, `faker`, and `random` for data generation and handling.
- **Sets Number of Support/Complaint Records:** You can choose how many support/complaint records to generate (e.g., 8,000).
- **Defines Support Attributes:**
  - CustomerID: Randomly selected from real customers in the master data
  - TicketDate: Random date in the last 2 years
  - IssueType: Randomly chosen from ['Transaction', 'Login', 'Card', 'Service', 'Other']
  - ResolutionTime: Random float between 1 and 72 (hours)
  - Satisfaction: Randomly chosen from ['Satisfied', 'Neutral', 'Unsatisfied']
- **Generates Data:** Loops through the desired number of support/complaint records, creating a dictionary for each with the above attributes.
- **Creates a DataFrame:** Converts the list of support dictionaries into a pandas DataFrame.
- **Ensures Data Folder Exists:** Uses `os.makedirs('data', exist_ok=True)` to make sure the `data/` folder is present.
- **Saves as CSV:** Writes the DataFrame to `data/support_data.csv`.
- **Prints a Message:** Lets you know the file was created and where it's saved.

**Note:** The generated CSV is ignored by git and not uploaded to GitHub, keeping your repository clean.

## Data Integration (Detailed)
The script `scripts/data_integration.py` reads, cleans, and merges all generated datasets into a unified customer dataset for analysis. Here's what it does:

- **Imports Required Libraries:** Uses `pandas` and `numpy` for data manipulation and cleaning.
- **Reads All CSV Files:** Loads customer_master.csv, usage_data.csv, payment_data.csv, and support_data.csv into pandas DataFrames.
- **Data Cleaning:**
  - Converts all date columns to proper datetime format
  - Handles missing values in payment data (fills missing payment methods with 'Not Applicable')
- **Creates Summary Statistics:**
  - **Usage Summary:** For each customer, calculates usage count, total amount spent on services, average amount per usage, total session duration, and average duration per session
  - **Payment Summary:** For each customer, calculates total bill amount, average bill amount, and count of missed payments
  - **Support Summary:** For each customer, calculates number of support tickets, average resolution time, and count of unsatisfied tickets
- **Merges All Data:** Combines customer master data with usage, payment, and support summaries using CustomerID as the common field.
- **Saves Merged Dataset:** Creates a unified CSV file (`merged_customer_data.csv`) containing all customer information and their behavioral patterns.
- **Output:** A comprehensive dataset ready for churn analysis and machine learning modeling.

**Note:** The merged CSV is ignored by git and not uploaded to GitHub, keeping your repository clean.

## Getting Started
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the customer data generation script: `python scripts/generate_customer_master.py`
4. Run the usage/activity data generation script: `python scripts/generate_usage_data.py`
5. Run the payment/billing data generation script: `python scripts/generate_payment_data.py`
6. Run the support/complaint data generation script: `python scripts/generate_support_data.py`
7. Run the data integration script: `python scripts/data_integration.py`
8. Generated data will be saved in the `data/` folder (not tracked by git).

---

*Update this README as the project progresses.* 