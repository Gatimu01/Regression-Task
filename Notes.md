# Tips Dataset Analysis

## Objective
The objective of this analysis was to identify the variable that most strongly influences tip amount and to build a simple regression model to predict tips.

## Data Cleaning and Preprocessing
The following preprocessing steps were performed:
- Checked for missing values
- Identified and removed duplicate rows
- Checked for outliers using boxplots
- Encoded categorical variables using label encoding to support correlation analysis

A correlation heatmap was then generated against the target variable (`tip`) to identify the most influential predictor variable.

## Most Influential Variable
Based on the correlation analysis, `total_bill` appeared to be the most influential variable affecting tip amount.

Both the scatter plot and bar chart visualizations showed a clear positive relationship between total bill and tip size, suggesting that customers who spend more generally leave larger tips.

## Model
A simple linear regression model was built using:
- `total_bill` as the predictor variable
- `tip` as the target variable

## Model Equation

ŷ = 0.0998(total_bill) + 1.0354

### Interpretation
- `0.0998`: For every 1-unit increase in total bill, the predicted tip increases by approximately 0.10 units on average.
- `1.0354`: When the total bill is 0, the model predicts an approximate tip value of 1.0354.

## Evaluation
Model performance was evaluated using:
- Mean Squared Error (MSE): 1.1508
- R-squared (R²): 0.5277

### Interpretation of Results
The model explains approximately 52.8% of the variation in tip amounts using `total_bill` alone.

This indicates a moderately strong positive relationship between total bill and tipping behavior. However, approximately 47% of the variation remains unexplained, suggesting that additional variables may also influence tipping behavior.

The Mean Squared Error of 1.15 indicates that prediction errors remain relatively moderate, though the model does not fully capture all factors influencing tip size.