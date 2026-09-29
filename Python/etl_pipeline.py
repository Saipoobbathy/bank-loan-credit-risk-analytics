import pandas as pd
from pathlib import Path

# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "Output"
OUTPUT_FILE = OUTPUT_DIR / "financial_loan_cleaned.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD RAW DATA
# ============================================================

print("Loading dataset...")

df = pd.read_csv(r"C:\Users\saipo\OneDrive\Desktop\Bank_Loan_Credit_Risk\Data\financial_loan_raw.csv.csv")

print(f"Original rows: {len(df)}")
print(f"Original columns: {len(df.columns)}")
# ============================================================
# 3. CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


# ============================================================
# 4. REMOVE DUPLICATES
# ============================================================

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print(f"Duplicates removed: {before_duplicates - after_duplicates}")


# ============================================================
# 5. CLEAN INTEREST RATE
# ============================================================

if "int_rate" in df.columns:
    df["int_rate"] = (
        df["int_rate"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["int_rate"] = pd.to_numeric(
        df["int_rate"],
        errors="coerce"
    )


# ============================================================
# 6. CLEAN REVOLVING UTILIZATION
# ============================================================

if "revol_util" in df.columns:
    df["revol_util"] = (
        df["revol_util"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["revol_util"] = pd.to_numeric(
        df["revol_util"],
        errors="coerce"
    )


# ============================================================
# 7. CONVERT LOAN STATUS
# ============================================================

if "loan_status" in df.columns:
    df["loan_status"] = pd.to_numeric(
        df["loan_status"],
        errors="coerce"
    )


# ============================================================
# 8. CREATE LOAN CONDITION
# ============================================================

if "loan_status" in df.columns:

    df["loan_condition"] = df["loan_status"].map({
        0: "Good Loan",
        1: "Bad Loan"
    })


# ============================================================
# 9. CREATE DTI BAND
# ============================================================

if "dti" in df.columns:

    df["dti_band"] = pd.cut(
        df["dti"],
        bins=[-float("inf"), 10, 20, 30, 40, float("inf")],
        labels=[
            "Below 10%",
            "10% - 20%",
            "20% - 30%",
            "30% - 40%",
            "40%+"
        ]
    )


# ============================================================
# 10. CREATE LOAN YEAR
# ============================================================

if "issue_d" in df.columns:

    issue_date = pd.to_datetime(
        df["issue_d"],
        format="%b-%y",
        errors="coerce"
    )

    df["loan_year"] = issue_date.dt.year
    df["loan_month"] = issue_date.dt.month


# ============================================================
# 11. HANDLE NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    "loan_amnt",
    "funded_amnt",
    "funded_amnt_inv",
    "installment",
    "annual_inc",
    "dti",
    "delinq_2yrs",
    "inq_last_6mths",
    "open_acc",
    "pub_rec",
    "revol_bal",
    "total_acc",
    "out_prncp",
    "out_prncp_inv",
    "total_pymnt",
    "total_pymnt_inv",
    "total_rec_prncp",
    "total_rec_int",
    "total_rec_late_fee",
    "recoveries",
    "collection_recovery_fee",
    "last_pymnt_amnt",
    "pub_rec_bankruptcies"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# 12. HANDLE MISSING VALUES
# ============================================================

# Numeric columns → median
for column in numeric_columns:

    if column in df.columns:

        df[column] = df[column].fillna(
            df[column].median()
        )


# Categorical columns → Unknown
categorical_columns = [
    "term",
    "grade",
    "sub_grade",
    "emp_length",
    "home_ownership",
    "verification_status",
    "purpose",
    "title",
    "addr_state",
    "loan_condition",
    "dti_band"
]

for column in categorical_columns:

    if column in df.columns:

        df[column] = df[column].fillna("Unknown")


# ============================================================
# 13. VALIDATION
# ============================================================

print("\n========== VALIDATION ==========")

print("Rows after cleaning:", len(df))
print("Columns after cleaning:", len(df.columns))

print("\nRemaining missing values:")

missing_values = df.isnull().sum()

print(
    missing_values[missing_values > 0]
)


# ============================================================
# 14. LOAN CONDITION CHECK
# ============================================================

if "loan_condition" in df.columns:

    print("\nLoan Condition Distribution:")

    print(
        df["loan_condition"].value_counts()
    )


# ============================================================
# 15. SAVE CLEAN DATASET
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n================================")
print("ETL COMPLETED SUCCESSFULLY!")
print("================================")

print(f"Cleaned rows: {len(df)}")
print(f"Cleaned columns: {len(df.columns)}")

print("\nCleaned file saved to:")

print(OUTPUT_FILE)