Laptop Market Analysis
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Pandas-1.3%252B-orange
https://img.shields.io/badge/Jupyter-Notebook-orange

A comprehensive data analysis project exploring laptop specifications, pricing trends, and market patterns using Python.

📊 Project Overview
This project performs exploratory data analysis on a dataset containing detailed information about various laptop models, their technical specifications, and pricing. The analysis reveals insights about what factors most significantly impact laptop prices and identifies trends in the laptop market.

🎯 Objectives
Analyze the relationship between laptop specifications and pricing

Identify which components (CPU, RAM, GPU, etc.) contribute most to price variations

Compare pricing and features across different brands and product categories

Discover market trends and value propositions in the laptop industry

Create informative visualizations to communicate findings effectively

📁 Dataset
The analysis uses laptop_data.csv which includes the following features:

Company: Manufacturer brand (HP, Dell, Lenovo, etc.)

TypeName: Product category (Gaming, Ultrabook, Notebook, etc.)

Inches: Screen size

ScreenResolution: Display resolution and technology

Cpu: Processor specifications

Ram: Memory capacity

Memory: Storage configuration (SSD, HDD, or hybrid)

Gpu: Graphics processing unit

OpSys: Operating system

Weight: Product weight

Price: Retail price

🛠️ Technologies Used
Python 3.8+

Pandas - Data manipulation and analysis

NumPy - Numerical computations

Matplotlib - Data visualization

Seaborn - Statistical data visualization

Jupyter Notebook - Interactive development environment

📋 Project Structure
text
laptop-analysis/
│
├── data/
│   └── laptop_data.csv          # Raw dataset
│
├── notebooks/
│   └── laptop_analysis.ipynb    # Main analysis notebook
│
├── src/
│   ├── data_cleaning.py         # Data preprocessing functions
│   ├── visualization.py         # Plotting functions
│   └── analysis.py              # Analytical functions
│
├── results/
│   ├── figures/                 # Generated visualizations
│   └── insights.md              # Key findings
│
└── requirements.txt             # Project dependencies
🚀 Installation & Setup
Clone the repository:

bash
git clone https://github.com/yourusername/laptop-market-analysis.git
cd laptop-market-analysis
Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required packages:

bash
pip install -r requirements.txt
💻 Usage
Start Jupyter Notebook:

bash
jupyter notebook
Open and run notebooks/laptop_analysis.ipynb to execute the full analysis

Alternatively, run individual modules from the src/ directory:

python
from src.data_cleaning import load_and_clean_data
df = load_and_clean_data('data/laptop_data.csv')
📈 Key Analyses Performed
Price Distribution Analysis: Examined how laptop prices are distributed across different brands and categories

Correlation Study: Identified which specifications have the strongest relationship with price

Brand Comparison: Analyzed price premiums and value propositions across manufacturers

Component Analysis: Evaluated how CPU, RAM, GPU, and storage affect pricing

Category Insights: Compared specifications and pricing across product types (Gaming, Ultrabooks, Workstations, etc.)

📊 Sample Insights
Gaming laptops command a significant price premium compared to standard notebooks

SSDs have a substantial impact on pricing, especially in ultrabooks

Certain brands maintain consistent pricing strategies across their product lines

There are noticeable price thresholds at specific RAM and storage configurations

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👥 Authors
Your Name -Ahmedalgaor

🙏 Acknowledgments
Dataset sourced from RTC 

Inspired by the need for better consumer understanding of laptop value propositions
