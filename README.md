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
7. **Version Control:** All code/scripts and config files are tracked and pushed to GitHub. Data files are ignored for efficiency.

## Customer Master Data Generation (Detailed)
The script `scripts/generate_customer_master.py` creates a large, realistic customer master dataset for analysis. Here’s what it does:

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
- **Prints a Message:** Lets you know the file was created and where it’s saved.

**Note:** The generated CSV is ignored by git and not uploaded to GitHub, keeping your repository clean.

## Usage/Activity Data Generation (Detailed)
The script `scripts/generate_usage_data.py` creates a large, realistic usage/activity dataset for analysis. Here’s what it does:

- **Imports Required Libraries:** Uses `pandas`, `numpy`, `faker`, and `random` for data generation and handling.
- **Sets Number of Usage Records:** You can choose how many usage/activity records to generate (e.g., 100,000).
- **Defines Usage Attributes:**
  - CustomerID: Randomly selected from real customers in the master data
  - UsageDate: Random date in the last 2 years
  - Service: Randomly chosen from ['Mobile App', 'Website', 'ATM', 'Branch Visit']
  - Amount: Random float between 10 and 1000 (2 decimal places)
  - SessionDuration: Random integer between 1 and 120 (minutes)
- **Generates Data:** Loops through the desired number of usage records, creating a dictionary for each with the above attributes.
- **Creates a DataFrame:** Converts the list of usage dictionaries into a pandas DataFrame.
- **Ensures Data Folder Exists:** Uses `os.makedirs('data', exist_ok=True)` to make sure the `data/` folder is present.
- **Saves as CSV:** Writes the DataFrame to `data/usage_data.csv`.
- **Prints a Message:** Lets you know the file was created and where it’s saved.

**Note:** The generated CSV is ignored by git and not uploaded to GitHub, keeping your repository clean.

## Getting Started
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the customer data generation script: `python scripts/generate_customer_master.py`
4. Run the usage/activity data generation script: `python scripts/generate_usage_data.py`
5. Generated data will be saved in the `data/` folder (not tracked by git).

---

*Update this README as the project progresses.* 