
# 🧹 Data Cleaning and Visualization Toolkit

This project provides a Python-based utility to **clean and visualize structured datasets** (CSV or Excel) with a focus on missing values, duplicates, and categorical consistency. It also generates insightful visualizations before and after the cleaning process.

## 📂 Features

* Automatically detects and replaces missing values
* Drops columns with over 90% missing values
* Standardizes categorical data (e.g., uppercasing "Sex", "Embarked")
* Handles both `.csv` and `.xlsx` input/output files
* Removes duplicate records
* Generates visualizations including:

  * Missing value counts (before and after)
  * Row and column count comparison
  * Age and Fare distributions
  * Gender breakdown
  * Survival rate by passenger class

## 📊 Visual Outputs

The script generates a 3x3 grid of visualizations:

1. Missing Values (Before Cleaning)
2. Missing Values (After Cleaning)
3. Row Count Comparison
4. Column Count Comparison
5. Age Distribution
6. Gender Distribution
7. Survival Rate by Class
8. Fare Distribution

## 🛠️ Requirements

Install the required packages using:

```bash
pip install pandas matplotlib openpyxl
```

## 🚀 How to Use

1. Place your input file in the same directory. It can be:

   * A CSV file (e.g., `realistic_titanic_sample.csv`)
   * An Excel file (e.g., `data.xlsx`)

2. Modify the `input_file` and `output_file` variables in the script:

```python
input_file = "realistic_titanic_sample.csv"
output_file = "cleaned_titanic_data.csv"
```

3. Run the script:

```bash
python clean_and_visualize.py
```

4. The cleaned dataset will be saved, and visualizations will be displayed.

## 🧠 Smart Cleaning Rules

* **Numerical Columns**: Missing values are filled with the **median**
* **Categorical Columns**: Missing values are filled with **"UNKNOWN"**
* **Standardization**: Categorical values like `"male"`, `"FEMALE"`, `" "` are cleaned and capitalized
* **Empty Strings**: Treated as `NaN`
* **Highly Missing Columns**: Columns with more than 90% missing values are dropped

## 📁 Example Input

Use Titanic-style datasets or any structured data with mixed numerical and categorical columns for best results.

## 📤 Output

* Cleaned file in `.csv` or `.xlsx` format
* Summary statistics (via `df.describe`)
* Data cleaning report in the console
* Graphical representation via `matplotlib`

## 📌 Note

Ensure your input file is properly formatted. The script auto-detects format from the file extension.
