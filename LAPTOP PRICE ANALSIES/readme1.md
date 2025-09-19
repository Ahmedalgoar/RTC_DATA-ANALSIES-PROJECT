Laptop Pricing Dataset - Initial Data Analysis (EDA)
Project Overview
This Jupyter Notebook performs an initial exploratory data analysis (EDA) on a laptop pricing dataset containing 1,303 records with 12 features. The primary goal is to understand the dataset's structure, perform preliminary cleaning, and begin exploring relationships between laptop specifications and their prices.

Dataset Information
Source: laptop_data.csv

Dimensions: 1303 rows × 12 columns

Target Variable: Price (numerical)

Code Implementation & Analysis
1. Importing Libraries
python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
Essential data manipulation and visualization libraries are imported:

Pandas for data handling

Matplotlib and Seaborn for visualizations

NumPy for numerical operations

2. Data Loading
python
df = pd.read_csv(r"D:\DEPI\Technical\4- Machine Learning\Laptop Pricing\laptop_data.csv")
The dataset is loaded from a CSV file into a Pandas DataFrame.

3. Initial Data Inspection
Basic Exploration:

python
df.shape  # (1303, 12)
df.head()
df.tail()
df.info()
df.describe()
Key Findings:

Dataset contains 1303 entries with 12 features

Features include both numerical (Price, Inches) and categorical (Company, TypeName) data

No missing values detected (df.isnull().sum())

No duplicate entries (df.duplicated().sum())

4. Data Cleaning
Text Standardization:

python
df['Ram'] = df['Ram'].str.replace('GB','')
df['Weight'] = df["Weight"].str.replace("KG","")
Removes unit specifications ('GB' from RAM, 'KG' from Weight)

Prepares these columns for numerical conversion in subsequent analysis

5. Exploratory Data Analysis
Price Distribution:

python
sns.displot(df['Price'])
Reveals right-skewed distribution indicating most laptops are moderately priced with some high-end outliers

Brand Distribution:

python
df['Company'].value_counts().plot(kind='bar')
Shows Dell, Lenovo, and HP as the most represented brands

Apple has fewer entries but typically represents premium segment

Key Insights
Data Quality: Excellent initial quality with no missing values or duplicates

Data Types: Mixed numerical and categorical features requiring further processing

Price Distribution: Right-skewed suggesting need for potential transformation in modeling

Brand Representation: Uneven distribution across manufacturers

Next Steps
Advanced Data Cleaning:

Convert RAM and Weight to numerical formats

Extract features from composite columns (ScreenResolution, CPU, Memory)

Handle categorical variables through encoding

Comprehensive EDA:

Correlation analysis between features and price

Brand-wise price distribution analysis

Operational system impact on pricing

Hardware specification trends (RAM, storage type)

Feature Engineering:

Create new features from existing data

Standardize measurement units

Handle potential outliers

Predictive Modeling Preparation:

Train-test split

Feature scaling

Model selection and evaluation

This initial EDA provides a solid foundation for deeper analysis and future modeling efforts to understand laptop pricing dynamics.
