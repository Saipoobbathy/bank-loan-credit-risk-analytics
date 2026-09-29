# 🏦 Bank Loan & Credit Risk Analytics

## 📊 End-to-End Data Analytics Project | MySQL + Power BI + DAX

An end-to-end **Bank Loan & Credit Risk Analytics** project designed to analyze loan portfolio performance, identify credit-risk patterns, monitor bad-loan exposure, and generate actionable business insights using **MySQL, Power BI, and DAX**.

The project transforms raw loan data into an interactive Power BI dashboard covering **portfolio performance, credit risk, customer insights, funding trends, loan grades, DTI, purpose, geographic distribution, interest rates, and verification status**.

---

## 🎯 Project Objective

The main objective of this project is to answer important business questions related to a bank's loan portfolio:

1. How large is the overall loan portfolio?
2. How much money has been funded?
3. What percentage of loans are classified as bad loans?
4. Which loan grades and purposes have higher default rates?
5. Where is bad-loan exposure concentrated?
6. How is loan funding changing over time?
7. How do DTI levels relate to loan default?
8. How does loan performance vary by state?
9. How do interest rates vary across loan grades?
10. How does verification status relate to loan performance?

---

## 🛠️ Tools & Technologies

| Technology      | Purpose                                               |
| --------------- | ----------------------------------------------------- |
| **MySQL**       | Data cleaning, transformation, analysis and SQL views |
| **Power BI**    | Interactive dashboard and data visualization          |
| **DAX**         | KPI calculations and analytical measures              |
| **Power Query** | Data transformation and preparation                   |
| **Excel/CSV**   | Source loan dataset                                   |
| **GitHub**      | Project documentation and portfolio                   |

---

## 📁 Project Structure

```text
Bank_Loan_Credit_Risk/
│
├── Data/
│   ├── financial_loan_raw.csv
│   └── financial_loan_cleaned.csv
│
├── Python/
│   └── etl_pipeline.py
│
├── SQL/
│   └── credit_risk_warehouse.sql
│
├── PowerBI/
│   └── Bank_Loan_Dashboard.pbix
│
├── Screenshots/
│   ├── executive_dashboard.png
│   ├── credit_risk_dashboard.png
│   ├── geographic_dashboard.png
│   └── grade_details.png
│
└── README.md
```

---

# 🔄 Project Workflow

```text
Raw Loan Dataset
       ↓
Data Cleaning & Transformation
       ↓
MySQL Database
       ↓
SQL Analysis & View Creation
       ↓
v_loan_data SQL View
       ↓
Power BI
       ↓
DAX Measures
       ↓
Interactive Dashboard
       ↓
Business Insights
```

---

# 🗄️ SQL & Data Preparation

The cleaned loan data is loaded into a MySQL database named:

```text
bank_loan_credit_risk
```

The primary analytical data source used in Power BI is:

```text
v_loan_data
```

The SQL layer prepares the data for portfolio and credit-risk analysis.

Key analytical dimensions include:

* Loan amount
* Funded amount
* Investor funded amount
* Loan status
* Loan condition
* Loan grade
* Sub-grade
* Interest rate
* Annual income
* DTI
* DTI band
* Home ownership
* Verification status
* Loan purpose
* State
* Loan term
* Loan year
* Loan month
* Total payment
* Principal received
* Interest received
* Recoveries
* Late fees

---

# 📊 Power BI Dashboard

The Power BI solution is organized into multiple analytical pages.

## 1️⃣ Executive Dashboard

### Key Performance Indicators

The executive dashboard provides an overview of the loan portfolio through KPI cards:

* 👥 Total Loans
* 💰 Total Loan Amount
* 🏦 Total Funded Amount
* 💵 Total Received
* ⚠️ Bad Loan %
* 📈 Recovery Rate

### Main Visualizations

* Good vs Bad Loans
* Default Rate by Loan Grade
* Monthly Funding Trend
* Default Rate by Loan Purpose
* Default Rate by DTI Band

---

## 2️⃣ Credit Risk Analysis

This page focuses on identifying credit-risk patterns.

### Visualizations

* Default Rate by Loan Grade
* Bad Loan Exposure by Grade
* Default Rate by Purpose
* DTI Band Risk Analysis
* Bad Loan Exposure by Home Ownership
* Interest Rate by Loan Grade
* Loan Term Analysis

---

## 3️⃣ Geographic & Customer Insights

This page analyzes geographic and customer-related loan patterns.

### Visualizations

* State-wise Loan Risk Map
* Default Rate by State
* Funding by State
* Verification Status Analysis
* Home Ownership Analysis
* Loan Term Analysis

---

## 4️⃣ Loan Grade Details

A drill-through page is used to provide detailed analysis for individual loan grades.

The page includes:

* Total Loans
* Funded Amount
* Default Rate
* Average Interest Rate
* Bad Loan Exposure
* Purpose Analysis
* DTI Analysis
* Interest Rate Analysis

Users can select a loan grade from the main dashboard and drill through to detailed grade-level analysis.

---

# 🧮 Key DAX Measures

## Total Loans

```DAX
Total Loans =
COUNT(v_loan_data[id])
```

## Total Loan Amount

```DAX
Total Loan Amount =
SUM(v_loan_data[loan_amnt])
```

## Total Funded Amount

```DAX
Total Funded Amount =
SUM(v_loan_data[funded_amnt])
```

## Total Received

```DAX
Total Received =
SUM(v_loan_data[total_pymnt])
```

## Good Loans

```DAX
Good Loans =
CALCULATE(
    [Total Loans],
    v_loan_data[loan_condition] = "Good Loan"
)
```

## Bad Loans

```DAX
Bad Loans =
CALCULATE(
    [Total Loans],
    v_loan_data[loan_condition] = "Bad Loan"
)
```

## Good Loan %

```DAX
Good Loan % =
DIVIDE(
    [Good Loans],
    [Total Loans],
    0
)
```

## Bad Loan %

```DAX
Bad Loan % =
DIVIDE(
    [Bad Loans],
    [Total Loans],
    0
)
```

## Default Rate

```DAX
Default Rate =
DIVIDE(
    [Bad Loans],
    [Total Loans],
    0
)
```

## Bad Loan Exposure

```DAX
Bad Loan Exposure =
CALCULATE(
    [Total Funded Amount],
    v_loan_data[loan_condition] = "Bad Loan"
)
```

## Recovery Rate

```DAX
Recovery Rate =
DIVIDE(
    [Total Received],
    [Total Funded Amount],
    0
)
```

## Average Interest Rate

```DAX
Average Interest Rate =
AVERAGE(v_loan_data[int_rate])
```

## Average Loan Amount

```DAX
Average Loan Amount =
AVERAGE(v_loan_data[loan_amnt])
```

## Average DTI

```DAX
Average DTI =
AVERAGE(v_loan_data[dti])
```

## Total Interest Received

```DAX
Total Interest Received =
SUM(v_loan_data[total_rec_int])
```

---

# 📈 Key Dashboard Visualizations

### Good vs Bad Loans

**Visual:** Donut Chart

* Legend → `loan_condition`
* Values → `Total Loans`

---

### Default Rate by Grade

**Visual:** Clustered Column Chart

* X-axis → `grade`
* Y-axis → `Default Rate`
* Tooltips → Total Loans, Bad Loans, Average Interest Rate

---

### Monthly Funding Trend

**Visual:** Line Chart

* X-axis → `Year Month`
* Y-axis → `Total Funded Amount`

A Year-Month sorting column is used to maintain chronological order.

```DAX
Year Month =
FORMAT(
    DATE(
        v_loan_data[loan_year],
        v_loan_data[loan_month],
        1
    ),
    "MMM yyyy"
)
```

```DAX
Year Month Sort =
v_loan_data[loan_year] * 100 +
v_loan_data[loan_month]
```

---

### Default Rate by Purpose

**Visual:** Bar Chart

* Y-axis → `purpose`
* X-axis → `Default Rate`
* Tooltips → Total Loans, Total Funded Amount, Bad Loan Exposure

---

### DTI Risk Analysis

**Visual:** Column Chart

* X-axis → `dti_band`
* Y-axis → `Default Rate`
* Tooltips → Total Loans, Average DTI

---

### State-wise Loan Risk

**Visual:** Map

* Location → `addr_state`
* Size → `Total Funded Amount`
* Tooltips → Total Loans, Default Rate, Bad Loan Exposure

---

# 🎛️ Interactive Filters

The dashboard includes slicers for:

* Grade
* Loan Condition
* Purpose
* Home Ownership
* Verification Status
* Loan Year

These filters allow users to dynamically explore different segments of the loan portfolio.

For example, selecting a specific loan grade automatically updates the KPIs and visualizations according to the selected filter context.

---

# 💡 Business Questions Addressed

The project focuses on six major business questions:

### 1. Portfolio Size

How large is the bank's overall loan portfolio?

### 2. Funding

How much capital has been funded through loans?

### 3. Credit Risk

What percentage of loans are classified as bad loans?

### 4. Risk Segmentation

Which grades, purposes, DTI bands and loan terms show different default patterns?

### 5. Geographic Risk

Where is loan funding and bad-loan exposure distributed geographically?

### 6. Funding Trend

How does loan funding change over time?

---

# 📌 Key Analytical Areas

The dashboard provides analysis across:

```text
Portfolio Performance
        │
        ├── Loan Amount
        ├── Funded Amount
        ├── Total Received
        └── Recovery Rate

Credit Risk
        │
        ├── Good vs Bad Loans
        ├── Default Rate
        ├── Loan Grade
        ├── DTI
        └── Loan Purpose

Customer Analysis
        │
        ├── Home Ownership
        ├── Verification Status
        ├── Annual Income
        └── Loan Term

Geographic Analysis
        │
        └── State-wise Performance

Time Analysis
        │
        └── Monthly Funding Trend
```

---

# 🎨 Dashboard Design

The dashboard follows a professional financial analytics design approach:

* Clean and minimal layout
* Consistent financial-dashboard theme
* KPI cards for important metrics
* Interactive slicers
* Charts focused on business questions
* Geographic visualization
* Drill-through analysis
* Limited use of decorative images
* Clear dashboard titles and section headings

---

# 📸 Dashboard Preview

Add your Power BI screenshots to the `Screenshots` folder and display them here.

### Executive Dashboard

```markdown
![Executive Dashboard](Screenshots/executive_dashboard.png)
```

### Credit Risk Analysis

```markdown
![Credit Risk Dashboard](Screenshots/credit_risk_dashboard.png)
```

### Geographic & Customer Insights

```markdown
![Geographic Dashboard](Screenshots/geographic_dashboard.png)
```

### Loan Grade Details

```markdown
![Loan Grade Details](Screenshots/grade_details.png)
```

---

# 🚀 How to Use This Project

## Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/Bank_Loan_Credit_Risk.git
```

## Step 2 — Set Up MySQL

Create the database:

```sql
CREATE DATABASE bank_loan_credit_risk;
```

Run the SQL script from:

```text
SQL/credit_risk_warehouse.sql
```

## Step 3 — Verify the SQL View

Make sure the analytical view exists:

```sql
SELECT *
FROM v_loan_data;
```

## Step 4 — Open Power BI

Open:

```text
PowerBI/Bank_Loan_Dashboard.pbix
```

Connect Power BI to:

```text
MySQL
    ↓
bank_loan_credit_risk
    ↓
v_loan_data
```

## Step 5 — Explore the Dashboard

Use the slicers, charts and drill-through functionality to analyze different segments of the loan portfolio.

---

# 📂 Repository Contents

| Folder/File    | Description                         |
| -------------- | ----------------------------------- |
| `Data/`        | Raw and cleaned loan datasets       |
| `Python/`      | ETL and data-processing scripts     |
| `SQL/`         | SQL database and analytical queries |
| `PowerBI/`     | Power BI dashboard                  |
| `Screenshots/` | Dashboard screenshots               |
| `README.md`    | Project documentation               |

---

# 👨‍💻 Skills Demonstrated

This project demonstrates practical skills in:

* SQL
* MySQL
* Data Cleaning
* Data Transformation
* Data Analysis
* Power BI
* DAX
* Power Query
* Data Visualization
* KPI Development
* Credit Risk Analysis
* Business Intelligence
* Dashboard Design
* Drill-through Analysis
* Interactive Reporting
* Business Problem Solving

---

# 🎓 Project Outcome

This project demonstrates an end-to-end analytics workflow, starting from raw loan data and transforming it into a structured analytical dataset and an interactive Power BI business intelligence dashboard.

The final solution combines **SQL data analysis, DAX calculations, KPI development, interactive visualizations, risk segmentation, geographic analysis, and business-focused reporting** into a single portfolio project.

---

## ⭐ Portfolio Project

**Project:** Bank Loan & Credit Risk Analytics
**Domain:** Banking & Financial Analytics
**Tools:** MySQL | Power BI | DAX | Power Query | Python
**Focus:** Loan Portfolio Performance | Credit Risk | Business Intelligence
