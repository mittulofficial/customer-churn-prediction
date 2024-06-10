import pandas as pd
import seaborn as sns

# Read the CSV file into a DataFrame
file_path = "/Users/mittulkumar/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

# Remove rows with non-numeric values in 'TotalCharges'
df = df[df['TotalCharges'].apply(lambda x: str(x).strip()).str.isnumeric()]

# Convert 'TotalCharges' to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])

# Now, let's proceed with feature engineering and analysis
# Assuming you want to sum up the service columns to get 'total_service_taken'
service_columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
                   'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 
                   'StreamingMovies']
df['total_service_taken'] = df[service_columns].apply(lambda row: row.sum(), axis=1)

# Visualize the distribution of 'total_service_taken' with respect to 'Churn'
sns.displot(x='total_service_taken', col='Churn', data=df)

# Calculate correlation for numerical columns
df_num = df[['tenure', 'MonthlyCharges', 'TotalCharges']]
df_num_corr = df_num.corr()

# For categorical columns, convert them into numerical using one-hot encoding
# Assuming you have categorical columns in df_cat DataFrame
# Let's assume all columns except numerical ones are categorical
categorical_columns = df.columns.difference(['tenure', 'MonthlyCharges', 'TotalCharges'])
df_cat = df[categorical_columns]
df_cat_encoded = pd.get_dummies(df_cat)

# Concatenate numerical and encoded categorical columns
df_final = pd.concat([df_num, df_cat_encoded], axis=1)
