# -*- coding: utf-8 -*-
"""Random Tree Regression on Car_Predication.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dxTI_qF8Qhwvuu9QOcsExXAVgVIdy9H8

#Random Tree Regression

#Import Libraries
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

"""# Load the dataset

"""

data = pd.read_csv('car.csv')

"""# Preview the dataset (optional)

"""

print(data.head())

"""# Preprocess the data
# Handling categorical variables by converting them into dummy variables

"""

data = pd.get_dummies(data, drop_first=True)

"""# Define features (X) and target (y)

"""

X = data.drop('Price', axis=1)
y = data['Price']

"""# Split the dataset into training and testing sets

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# Initialize the Decision Tree Regression model


"""

model = RandomForestRegressor(n_estimators=100, random_state=42)

"""# Train the model"""

model.fit(X_train, y_train)

"""# Make predictions on the training and test sets


"""

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

"""# Evaluate the model"""

# Evaluate the model on training data
mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)

# Evaluate the model on testing data
mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

print(f"Training Data - Mean Squared Error: {mse_train}")
print(f"Training Data - R-squared: {r2_train}")
print(f"Testing Data - Mean Squared Error: {mse_test}")
print(f"Testing Data - R-squared: {r2_test}")

"""#Compare actual vs predicted prices

"""

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
print(comparison.head())

"""# Visualization: Actual vs Predicted for Training Data

"""

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(x=y_train, y=y_train_pred, alpha=0.5)
plt.title('Training Data: Actual vs Predicted Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'r--', lw=2)

"""# Visualization: Actual vs Predicted for Testing Data

"""

plt.subplot(1, 2, 2)
sns.scatterplot(x=y_test, y=y_test_pred, alpha=0.5)
plt.title('Testing Data: Actual vs Predicted Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)

plt.tight_layout()
plt.show()

"""#EDA

# Display basic information
"""

print("Initial Data Info:\n", data.info())
print("\nInitial Data Description:\n", data.describe())

"""# 1. Summary Statistics"""

print("Summary Statistics:\n", data.describe())

"""
# 2. Missing Values Analysis
"""

print("Missing Values:\n", data.isnull().sum())

"""# 3. Distribution of the Target Variable (Price)

"""

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(data['Price'], kde=True, bins=30)
plt.title('Distribution of Prices in Full Dataset')
plt.xlabel('Price')
plt.ylabel('Frequency')

"""# 4. Correlation Matrix (only numerical features)

"""

plt.figure(figsize=(10, 8))
corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Features')
plt.show()

"""# 5. Pair Plot (Numerical Features)

"""

sns.pairplot(data[['Price', 'Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power', 'Seats']])
plt.title('Pair Plot of Numerical Features')
plt.show()

"""# 6. Box Plot for Outlier Detection

"""

plt.figure(figsize=(10, 6))
sns.boxplot(data=data[['Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power', 'Seats']])
plt.xticks(rotation=90)
plt.title('Box Plot of Numerical Features')
plt.show()

"""# 7. Count Plots for Categorical Features (Fuel_Type, Transmission, Owner_Type)

"""

plt.figure(figsize=(15, 5))

"""
# Plot for Fuel_Type,Transmission,Owner_type"""

# Plot for Fuel_Type
plt.subplot(1, 3, 1)
sns.countplot(x='Fuel_Type', data=data)
plt.title('Distribution of Fuel Type')

  # Plot for Transmission
plt.subplot(1, 3, 2)
sns.countplot(x='Transmission', data=data)
plt.title('Distribution of Transmission Type')

# Plot for Owner_Type
plt.subplot(1, 3, 3)
sns.countplot(x='Owner_Type', data=data)
plt.title('Distribution of Owner Type')

plt.tight_layout()
plt.show()

"""#Visiualization On Training and Testing Data"""

# 1. Distribution of the Target Variable (Price) in Training and Testing Sets
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
# Use y_train which should contain the 'Price' column
sns.histplot(y_train, kde=True, bins=30)
plt.title('Distribution of Prices in Training Set')
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
# Use y_test which should contain the 'Price' column
sns.histplot(y_test, kde=True, bins=30)
plt.title('Distribution of Prices in Testing Set')
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()