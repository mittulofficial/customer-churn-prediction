import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset according to file location
data = pd.read_csv('/Users/mittulkumar/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Drop 'customerID' column
data.drop(['customerID'], axis=1, inplace=True)

# Convert 'Churn' to binary format
data['Churn'] = data['Churn'].map(lambda s: 1 if s == 'Yes' else 0)

# Handle Categorical Variables
data = pd.get_dummies(data=data, columns=['gender'])

data['Partner'] = data['Partner'].map(lambda s: 1 if s == 'Yes' else 0)
data['Dependents'] = data['Dependents'].map(lambda s: 1 if s == 'Yes' else 0)
data['PhoneService'] = data['PhoneService'].map(lambda s: 1 if s == 'Yes' else 0)
data['PaperlessBilling'] = data['PaperlessBilling'].map(lambda s: 1 if s == 'Yes' else 0)

data['MultipleLines'].replace('No phone service', 'No', inplace=True)
data['MultipleLines'] = data['MultipleLines'].map(lambda s: 1 if s == 'Yes' else 0)

data['Has_InternetService'] = data['InternetService'].map(lambda s: 0 if s == 'No' else 1)
data['Fiber_optic'] = data['InternetService'].map(lambda s: 1 if s == 'Fiber optic' else 0)
data['DSL'] = data['InternetService'].map(lambda s: 1 if s == 'DSL' else 0)
data.drop(['InternetService'], axis=1, inplace=True)

columns_to_convert = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
for column in columns_to_convert:
    data[column] = data[column].map(lambda s: 1 if s == 'Yes' else 0)

data = pd.get_dummies(data=data, columns=['PaymentMethod', 'Contract'])

# Handle Numerical Variables
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data.dropna(subset=['TotalCharges'], inplace=True)

# Data Cleaning
total = data.isnull().sum().sort_values(ascending=False)
percent = (data.isnull().sum() / data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

# Visualization
g = sns.catplot(x="Churn", y="MonthlyCharges", data=data, kind="box", palette="Pastel1")
g = sns.catplot(x="Churn", y="TotalCharges", data=data, kind="boxen", palette="Pastel2")

# Final dataset after preprocessing
data.info()

