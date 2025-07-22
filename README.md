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
5. **Data Generation Script:** Created `scripts/generate_customer_master.py` to generate fake customer data (10,000 or 1,000,000+ records) and save as `data/customer_master.csv` (which is ignored by git).
6. **Version Control:** All code/scripts and config files are tracked and pushed to GitHub. Data files are ignored for efficiency.

## Getting Started
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the data generation script: `python scripts/generate_customer_master.py`
4. Generated data will be saved in the `data/` folder (not tracked by git).

---

*Update this README as the project progresses.* 