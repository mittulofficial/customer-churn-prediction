import numpy as np  # Importing numpy for linear algebra operations
import pandas as pd  # Importing pandas for data processing and CSV file I/O
import os
import matplotlib.pyplot as plt  # Importing matplotlib for plotting
import seaborn as sns  # Importing seaborn for visualization
from sklearn.model_selection import train_test_split  # Importing train_test_split for splitting data
from sklearn.feature_extraction import DictVectorizer  # Importing DictVectorizer for feature extraction
from sklearn.linear_model import LogisticRegression  # Importing LogisticRegression for model training
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, precision_score, recall_score, roc_curve  # Importing various metrics for model evaluation
import random  # Importing random for random operations

# Load the dataset
df = pd.read_csv("/Users/mittulkumar/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Preprocess the data
# Standardize column names by making them lowercase and replacing spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Get the list of categorical columns
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

# Standardize categorical column values by making them lowercase and replacing spaces with underscores
for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

# Convert 'totalcharges' to numeric, setting errors to 'coerce' to handle non-numeric values
df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)  # Fill any NaN values with 0

# Convert 'churn' to binary format (1 for 'yes', 0 for 'no')
df.churn = (df.churn == 'yes').astype(int)

# Split the data into training and test sets
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

# Reset indices for the splits
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# Separate target variable 'churn' from features
y_train = df_train.churn.values
y_val = df_val.churn.values
y_test = df_test.churn.values

# Remove 'churn' column from training, validation, and test sets
del df_train['churn']
del df_val['churn']
del df_test['churn']

# List of numerical and categorical columns
numerical = ['tenure', 'monthlycharges', 'totalcharges']
categorical = [
    'gender',
    'seniorcitizen',
    'partner',
    'dependents',
    'phoneservice',
    'multiplelines',
    'internetservice',
    'onlinesecurity',
    'onlinebackup',
    'deviceprotection',
    'techsupport',
    'streamingtv',
    'streamingmovies',
    'contract',
    'paperlessbilling',
    'paymentmethod',
]

# Feature engineering
# Calculate the total number of services taken by each customer
df['total_service_taken'] = df[['phoneservice', 'multiplelines', 'internetservice', 'onlinesecurity', 
                                'onlinebackup', 'deviceprotection', 'techsupport', 
                                'streamingtv', 'streamingmovies']].apply(lambda x: sum(x == 'yes'), axis=1)

# Plot the distribution of total services taken by churn status
sns.displot(x=df['total_service_taken'], col=df["churn"])

# Train the model
# Convert categorical and numerical columns to dictionary format
dv = DictVectorizer(sparse=False)
train_dict = df_train[categorical + numerical].to_dict(orient='records')

# Fit the DictVectorizer and transform the training data
X_train = dv.fit_transform(train_dict)

# Initialize and fit the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate the model on validation data
val_dict = df_val[categorical + numerical].to_dict(orient='records')
X_val = dv.transform(val_dict)

# Predict probabilities on validation set
y_pred = model.predict_proba(X_val)[:, 1]
churn_decision = (y_pred >= 0.5)

# Print validation accuracy
print("Validation Accuracy:", accuracy_score(y_val, churn_decision))

# Confusion matrix
confusion = confusion_matrix(y_val, churn_decision)
print("Confusion Matrix:\n", confusion)

# Calculate precision and recall
precision = precision_score(y_val, churn_decision)
recall = recall_score(y_val, churn_decision)
print("Precision:", precision)
print("Recall:", recall)

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_val, y_pred)
plt.figure(figsize=(5, 5))
plt.plot(fpr, tpr, label='Model')
plt.plot([0, 1], [0, 1], label='Random', linestyle='--')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.legend()
plt.show()

# ROC AUC score
roc_auc = roc_auc_score(y_val, y_pred)
print("Validation ROC AUC:", roc_auc)

# Functions for training and prediction
def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical + numerical].to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    
    return dv, model

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')
    
    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]
    
    return y_pred

# Evaluate the model on test data
dv, model = train(df_full_train, df_full_train.churn.values, C=1.0)
y_pred = predict(df_test, dv, model)

# Calculate and print ROC AUC score on test data
auc = roc_auc_score(y_test, y_pred)
print("Test ROC AUC:", auc)
