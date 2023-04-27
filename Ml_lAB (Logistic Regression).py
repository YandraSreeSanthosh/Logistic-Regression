# -*- coding: utf-8 -*-
"""diabetes[RA2011030010214].ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PstaaNZtrPCYhqpX_wVlqLEhE5k-G3YZ
"""

import pandas as pd
import numpy as np

# Load dataset
from google.colab import files
uploaded=files.upload()
data = pd.read_excel('diabetes.xlsx')

# Display first 5 rows
data.head()

from sklearn.model_selection import train_test_split

# Split dataset into features and target variable
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Predict on the testing set
lr_preds = lr_model.predict(X_test)

from sklearn.metrics import classification_report

# Print classification report
print(classification_report(y_test, lr_preds))