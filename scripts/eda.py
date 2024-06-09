# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/mittulkumar/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(file_path)

# Data Overview
print("Shape of the dataset:", df.shape)
print("First few rows of the dataset:")
print(df.head())
print("Data types of columns:")
print(df.dtypes)

# Data Cleaning
# Check for missing values, duplicates, and incorrect data types
print("Missing values:")
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
# Handle missing values, duplicates, and convert data types if necessary
# For example, convert 'TotalCharges' to numeric if needed

# Exploratory Data Analysis (EDA)
# Univariate Analysis

# Demographic info about customers
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='gender')
plt.title('Gender Distribution')
plt.show()

# Customer account information
# Example: Plot count of contracts
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Contract')
plt.title('Contract Distribution')
plt.show()

# Services that each customer has signed up for
# Example: Plot count of internet service types
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='InternetService')
plt.title('Internet Service Distribution')
plt.show()

# Target Feature (Churn)
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Churn')
plt.title('Churn Distribution')
plt.show()

# Convert 'TotalCharges' to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Now, try plotting churn rate by gender
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='gender', hue='Churn')
plt.title('Churn Rate by Gender')
plt.show()




# Customer account info vs. Churn
#  plot churn rate by contract type
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Contract', hue='Churn')
plt.title('Churn Rate by Contract Type')
plt.show()

# Services vs. Churn
# Calculate churn rate by internet service type
churn_rate_by_internet = df.groupby('InternetService')['Churn'].value_counts(normalize=True).mul(100).rename('Churn Rate').reset_index()

# Plot churn rate by internet service type
plt.figure(figsize=(10, 6))
sns.barplot(data=churn_rate_by_internet, x='InternetService', y='Churn Rate', hue='Churn')
plt.title('Churn Rate by Internet Service Type')
plt.ylabel('Churn Rate (%)')
plt.show()


# Multivariate Analysis
# Calculate churn rate by internet service type and contract type
churn_rate_by_service_contract = df.groupby(['InternetService', 'Contract'])['Churn'].value_counts(normalize=True).mul(100).rename('Churn Rate').reset_index()

# Plot churn rate by internet service type and contract type
plt.figure(figsize=(12, 8))
sns.barplot(data=churn_rate_by_service_contract, x='InternetService', y='Churn Rate', hue='Contract')
plt.title('Churn Rate by Internet Service and Contract Type')
plt.ylabel('Churn Rate (%)')
plt.show()


# Conclusion
# Summarize key findings and insights

# Visualizations and Plots
# Additional plotting code for more detailed analysis

# Display plots
plt.show()
