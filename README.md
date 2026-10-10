# Titanic Data Cleaning and Preprocessing 🚢

## 📌 Project Overview
This project focuses on cleaning and preprocessing the Titanic dataset using Python and Pandas. It handles missing values, standardizes text data, converts data types, and checks for duplicate records.

## 🎯 Objectives
- Identify missing values in the dataset.
- Handle missing values using appropriate techniques.
- Standardize text data.
- Convert columns to suitable data types.
- Check and remove duplicate records.
- Save the cleaned dataset and cleaning report.

## 🛠️ Technologies Used
- Python
- Pandas
- VS Code

## 📂 Project Files
- `titanic.csv` — Original dataset
- `clean_titanic.py` — Python cleaning script
- `cleaned_titanic.csv` — Cleaned dataset
- `data_cleaning_report.txt` — Cleaning results report

## 📊 Results

| Check | Before Cleaning | After Cleaning |
|---|---:|---:|
| Missing Age values | 177 | 0 |
| Missing Cabin values | 687 | 0 |
| Missing Embarked values | 2 | 0 |
| Duplicate rows | 0 | 0 |
| Dataset size | 891 × 12 | 891 × 12 |

Missing Age values were filled with the median (28.0), missing Embarked values with the mode, and missing Cabin values with `Unknown`.

## ▶️ How to Run

1. Install Python.
2. Install Pandas:

   `python -m pip install pandas`

3. Open the project folder in VS Code.
4. Run the script using the correct path:

   `python data/clean_titanic.py`

## ✅ Conclusion
The Titanic dataset was successfully cleaned and preprocessed. The output is ready for further data analysis and machine learning tasks.
