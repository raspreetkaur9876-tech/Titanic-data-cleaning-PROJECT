
import pandas as pd
from pathlib import Path

# STEP 1: Set file paths
project_folder = Path(__file__).parent.parent
data_file = project_folder / "data" / "titanic.csv"

# STEP 2: Load the original dataset
df = pd.read_csv(data_file)

print("=" * 50)
print("TITANIC DATA CLEANING AND PREPROCESSING")
print("=" * 50)

# STEP 3: Display the original dataset
print("\n1. FIRST FIVE ROWS")
print(df.head())

print("\n2. ORIGINAL DATASET SHAPE")
print(df.shape)

# STEP 4: Check column information
print("\n3. COLUMN INFORMATION")
df.info()

# STEP 5: Check missing values
print("\n4. MISSING VALUES BEFORE CLEANING")
missing_before = df.isnull().sum()
print(missing_before)

# STEP 6: Check duplicate rows
print("\n5. DUPLICATE ROWS BEFORE CLEANING")
duplicates_before = int(df.duplicated().sum())
print(duplicates_before)

# Store changes for the report
changes = []

# STEP 7: Clean column names
df.columns = df.columns.str.strip()
changes.append("Removed extra spaces from column names.")

# STEP 8: Remove duplicate rows
df = df.drop_duplicates()
changes.append(f"Removed {duplicates_before} duplicate rows.")

# STEP 9: Remove extra spaces from text values
text_columns = df.select_dtypes(
    include=["object", "str", "string"]
).columns

for column in text_columns:
    df[column] = df[column].str.strip()

changes.append("Removed extra spaces from text columns.")

# STEP 10: Standardize text values
if "Sex" in df.columns:
    df["Sex"] = df["Sex"].str.lower()

if "Embarked" in df.columns:
    df["Embarked"] = df["Embarked"].str.upper()

changes.append("Standardized Sex and Embarked text values.")

# STEP 11: Convert numeric columns to numeric data types
numeric_columns = [
    "PassengerId", "Survived", "Pclass",
    "Age", "SibSp", "Parch", "Fare"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

changes.append("Checked and converted numeric columns.")

# STEP 12: Handle missing Age values using the median
if "Age" in df.columns:
    age_missing = int(df["Age"].isnull().sum())
    median_age = df["Age"].median()

    df["Age"] = df["Age"].fillna(median_age)

    changes.append(
        f"Filled {age_missing} missing Age values "
        f"with median age {median_age}."
    )

# STEP 13: Handle missing Fare values using the median
if "Fare" in df.columns:
    fare_missing = int(df["Fare"].isnull().sum())

    if fare_missing > 0:
        median_fare = df["Fare"].median()
        df["Fare"] = df["Fare"].fillna(median_fare)

        changes.append(
            f"Filled {fare_missing} missing Fare values "
            f"with median fare {median_fare}."
        )
    else:
        changes.append("Fare had no missing values.")

# STEP 14: Handle missing Embarked values
if "Embarked" in df.columns:
    embarked_missing = int(df["Embarked"].isnull().sum())

    if embarked_missing > 0:
        most_common_port = df["Embarked"].mode().iloc[0]
        df["Embarked"] = df["Embarked"].fillna(
            most_common_port
        )

        changes.append(
            f"Filled {embarked_missing} missing Embarked values "
            f"with the most common port {most_common_port}."
        )
    else:
        changes.append("Embarked had no missing values.")

# STEP 15: Handle missing Cabin values
if "Cabin" in df.columns:
    cabin_missing = int(df["Cabin"].isnull().sum())

    df["Cabin"] = df["Cabin"].fillna("Unknown")

    changes.append(
        f"Marked {cabin_missing} missing Cabin values as Unknown."
    )

# STEP 16: Check the cleaned dataset
print("\n6. MISSING VALUES AFTER CLEANING")
missing_after = df.isnull().sum()
print(missing_after)

print("\n7. DUPLICATES AFTER CLEANING")
print(df.duplicated().sum())

print("\n8. CLEANED DATASET SHAPE")
print(df.shape)

# STEP 17: Save the cleaned dataset
cleaned_file = project_folder / "cleaned_titanic.csv"
df.to_csv(cleaned_file, index=False)

# STEP 18: Save the data cleaning report
report_file = project_folder / "data_cleaning_report.txt"

with open(report_file, "w", encoding="utf-8") as report:
    report.write("TITANIC DATA CLEANING REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write("Original dataset shape: 891 rows, 12 columns\n")
    report.write(f"Final dataset shape: {df.shape}\n")
    report.write(
        f"Duplicate rows found: {duplicates_before}\n"
    )
    report.write(
        f"Duplicate rows remaining: {int(df.duplicated().sum())}\n\n"
    )

    report.write("MISSING VALUES BEFORE CLEANING:\n")
    report.write(missing_before.to_string())
    report.write("\n\n")

    report.write("CLEANING OPERATIONS:\n")
    for change in changes:
        report.write("- " + change + "\n")

    report.write("\nMISSING VALUES AFTER CLEANING:\n")
    report.write(missing_after.to_string())
    report.write("\n\n")

    report.write(
        f"Total missing values remaining: "
        f"{int(missing_after.sum())}\n"
    )

    report.write("\nCONCLUSION:\n")
    report.write(
        "The dataset was inspected, cleaned, and saved "
        "for further analysis.\n"
    )

# STEP 19: Display completion message
print("\n" + "=" * 50)
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("=" * 50)

print("\nCleaned dataset saved at:")
print(cleaned_file)

print("\nCleaning report saved at:")
print(report_file)
