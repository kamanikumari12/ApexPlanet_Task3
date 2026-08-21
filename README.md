# ApexPlanet_Task3
# 📊 ApexPlanet Task 3 – Deep-Dive Analysis & Interactive Dashboarding

## Overview

This project is a part of the **ApexPlanet Data Analytics Internship – Task 3**. 
The objective is to perform a deep-dive analysis on a sales dataset, calculate key business KPIs, answer business questions using Python, and build an interactive dashboard for data-driven decision-making.

---

## Project Objectives

- Clean and prepare the dataset for analysis.
- Define and calculate business KPIs.
- Perform deep-dive sales analysis.
- Visualize insights using Python charts.
- Create an interactive Power BI dashboard.
- Present business findings in a professional GitHub project.

---

## Dataset Information

- **Records:** 1000
- **Columns:** 12
- **Year:** 2025

### Dataset Columns

- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales

---

## Data Cleaning

The following cleaning steps were performed:

- Removed duplicate records.
- Filled missing **Age** values with the median.
- Filled missing **City** values with "Unknown".
- Converted **Order_Date** into Date format.
- Created a Month column for trend analysis.

---

## Key Performance Indicators (KPIs)

| KPI | Value |
|------|-------:|
| Total Sales | ₹139,399,439.65 |
| Total Orders | 1000 |
| Average Order Value | ₹139,399.44 |
| Unique Customers | 947 |
| Average Customer Spend | ₹147,201.10 |

---

## Business Questions & Insights

### 1. Which products generate the highest revenue?

**Finding:** Laptop generated the highest total sales.

### 2. Which city performs best?

**Finding:** Patna recorded the highest sales.

### 3. What is the monthly sales trend?

**Finding:** Sales remained strong throughout the year, with March showing one of the highest sales periods.

### 4. Which category performs best?

**Finding:** Electronics contributed the highest revenue.

### 5. Customer Segmentation

Customers were grouped into:

- High Value
- Medium Value
- Low Value

High-value customers formed the largest customer segment.

---

## Visualizations

The project includes the following charts:

- Top Products by Sales
- Top Cities by Sales
- Monthly Sales Trend
- Sales by Category
- Customer Segmentation

These visualizations are available inside the **graphs/** folder.

---

## Dashboard

An interactive dashboard was created using **Power BI** featuring:

- KPI Cards
- Product Sales Analysis
- City-wise Sales
- Monthly Sales Trend
- Category Distribution
- Interactive Filters (City, Category, Month)

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Power BI
- GitHub

---

## Project Structure

```text
ApexPlanet-Task3/
│
├── Cleaned_Data.xlsx
├── analysis.py
├── README.md
├── dashboard/
│   └── PowerBI_Dashboard.pbix
└── graphs/
    ├── top_products.png
    ├── city_sales.png
    ├── monthly_sales.png
    ├── category.png
    └── segment.png
```

---

## How to Run

1. Clone or download the repository.
2. Install the required libraries:

```bash
pip install pandas matplotlib openpyxl
```

3. Run the Python script:

```bash
python analysis.py
```

4. Open **Power BI Desktop** and load `Cleaned_Data.xlsx` to explore the interactive dashboard.

---

## Key Learnings

Through this project, I learned how to:

- Clean real-world datasets.
- Calculate business KPIs.
- Perform sales trend analysis.
- Create data visualizations using Python.
- Build an interactive Power BI dashboard.
- Document and publish a professional analytics project on GitHub.

---

## Author
**Kamani Kumari**
- ApexPlanet Data Analytics Internship
