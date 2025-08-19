# Customer Purchase Behavior Analysis

## Project Overview

This project analyzes customer purchase data from an online retail dataset from kaggle to uncover insights about customer behavior, purchase patterns. The analysis involves data cleaning, feature engineering, visualization. 
---

## Dataset

- The main dataset contains transactional data including invoice numbers, product descriptions, quantities, StockCode, invoice dates, unit prices, customer IDs, and countries.

- A summarized customer dataset aggregates key metrics per customer: total amount spent, purchase frequency, and average order value.

---

## Project Structure and Steps

### 1. Data Cleaning and Preprocessing
- Loaded raw transactional data (`Online_Retail.xlsx`).
- Checked for missing values; found missing values mainly in `Description` and `CustomerID`.
- Filled missing `Description` with "Description not available" and missing `CustomerID` with "Unknown".
- Removed duplicate rows to ensure data integrity.
- Converted data types of relevant columns:
  - Converted `InvoiceDate` to datetime.
  - Converted `CustomerID`, `InvoiceNo`, and `StockCode` to string for consistent processing.
- Removed rows with zero or negative `UnitPrice` and `Quantity`.
- Dropped `StockCode` column as it was unnecessary for the analysis.
- Saved cleaned data to `Cleaned_Online_Retail.xlsx`.

### 2. Feature Engineering and Customer Summary
- Loaded cleaned transactional data.
- Calculated revenue per transaction as `Quantity * UnitPrice`.
- Aggregated data per customer, computing:
  - **Total Amount Spent**: Sum of revenue for each customer.
  - **Purchase Frequency**: Number of unique invoices per customer.
  - **Average Order Value**: Total amount spent divided by purchase frequency.
- Saved the customer summary to `Customer_Summary.xlsx`.

### 3. Data Visualization
- Loaded cleaned data to explore the data distributions and customer spending patterns.
- Created visualizations such as bar plots to examine:
  - Revenue distribution across countries.
  - Variations in total spend, purchase frequency, and average order values.
- These visual insights help identify distinct customer behaviors and potential segmentation strategies.

---

## Key Insights

- Customers display a wide range of purchase behavior, from single transactions with high value to frequent small purchases.
- Total spending varies significantly among customers, highlighting the existence of high-value customers.
- Purchase frequency and average order value metrics provide complementary views of customer engagement.
- Cleaning and preprocessing improved data quality by handling missing values and duplicates, enabling more accurate analysis.

---



## Files Included

- `Online_Retail.xlsx`: Original transactional dataset.
- `cs_clean_data.ipynb`: Jupyter notebook performing data cleaning and preprocessing.
- `cs_feature_engineering.ipynb`: Notebook for creating customer-level summarized features.
- `Customer_Summary.xlsx`: Output Excel file with aggregated customer metrics.
- `cs_visualize_data1.ipynb`: Notebook containing data visualization and exploratory analysis.

---

## How to Use

1. Run `cs_clean_data.ipynb` to clean and preprocess the raw data.
2. Run `cs_feature_engineering.ipynb` to generate customer summary features.
3. Explore visualizations in `cs_visualize_data1.ipynb` for insights into customer purchase patterns.
4. Use the `Customer_Summary.xlsx` file as input for further analysis or customer segmentation techniques.

---

## Dependencies

- Python (version 3.x)
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# Customer-Purchase-Behavior-Analysis
