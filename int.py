# %%
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


# %%


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

df = pd.read_csv(url)

df.head()
# len(df)

# %% [markdown]
# Do some data cleaning to see if we have any missing data or any duplicated rows of data

# %%
#Checking for null values
df.isnull().sum()

# %%
#Check for duplicates

print(df.duplicated().sum())
duplicates = df[df.duplicated(keep=False)]
print(duplicates)

# %%
df = df.drop_duplicates()
len(df)

# %%
#Do label encoding for the categorical variables
from sklearn.preprocessing import LabelEncoder  

le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex']) 
df['smoker'] = le.fit_transform(df['smoker'])
df['day'] = le.fit_transform(df['day'])
df['time'] = le.fit_transform(df['time'])
    

# %%
X= df[['total_bill', 'size' , 'sex', 'smoker', 'day', 'time']]
y = df['tip']

# %%
#Check for outliers using boxplot for all features on one graph


# Checking for outliers using boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=X)
plt.title("Boxplot of Features")
plt.show()

# %%
#Check for correlation using heatmap against the target variable 'tip'

df_corr = df.corr(numeric_only=True)[['tip']]

plt.figure(figsize=(8, 6))

sns.heatmap(
    df_corr,
    annot=True,
    cmap="RdBu",
    linewidths=0.5
)

plt.ylabel("Features")
plt.title("Correlation Matrix with Tip")

plt.show()

# %% [markdown]
# From the correlation graph the total bill has a high correlation with the tip. So we will use it for the simple linear regression model

# %%
#Do simple linear regression to predict tip amount based on total bill amount
#Define the features and target variable...Goal is to predict the tip based of the total bill paid
X = df[['total_bill']]
y = df['tip']

#Split the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Build the linear regression model

model = LinearRegression()

#Train the model on the training data
model.fit(X_train, y_train)


# %%
#DO prediction on the test set
y_pred = model.predict(X_test)

print("Predicted values:", y_pred)


# %%
#Evaluate the model using mean squared error and R-squared
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# %%



