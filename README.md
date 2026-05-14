# Tips Dataset Regression Analysis

## Overview
This project performs exploratory data analysis and simple linear regression on the Seaborn `tips` dataset to identify the variable that most strongly influences customer tipping behavior.

The analysis includes:
- Data inspection and cleaning
- Duplicate detection and removal
- Outlier visualization
- Correlation analysis
- Simple linear regression modeling
- Model evaluation
- Visualization of findings

---

## Objective
The goal of this analysis is to:
1. Identify the variable most strongly associated with tip amount
2. Build a simple regression model to predict tip values
3. Evaluate model performance using regression metrics
4. Visualize the relationship between the predictor and target variable

---

## Dataset
The dataset used is the publicly available Seaborn `tips` dataset.

Source:
https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
---

## Project Structure

```text
.
├── Int.ipynb                       # Main analysis notebook
├── Notes.md                        # Summary of findings and interpretations
├── tip_visualization.png           # Visualization explaining findings
├── tip_visualization_corr.png      # Visualization explaining the correlation between total bill and tip
├── README.md                       # Project documentation
└── .gitignore
```
---
## Run Instructions

Clone the repository, install the required dependencies, and open the notebook file.

```bash
git clone <repository_link>
cd <repository_name>
pip install pandas matplotlib seaborn scikit-learn notebook
jupyter notebook
```

Then open `Int.ipynb` and run all cells.

Alternatively, the notebook can also be opened and executed using VS Code with the Jupyter extension installed.
