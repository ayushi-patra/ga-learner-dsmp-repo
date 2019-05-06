# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 


# Create dataframe bank by passing the path of the file
read = pd.read_csv(path)
bank = pd.DataFrame(read) 

# Check all categorical values
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

# Check all categorical values
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var) 

# From the dataframe 'bank', drop the column 'Loan_ID' to create a new dataframe 'banks'
banks = bank.drop(columns = ['Loan_ID']) 

# To see the null values
print(banks.isnull().sum())  

# Calculate mode for the dataframe 'banks'
bank_mode = banks.mode()

# Fill missing(NaN) values of 'banks' with 'bank_mode'

# ALTERNATIVELY, banks['Gender'].fillna(banks['Gender'].mode(),inplace=True), mode() to find the maximum frequency of the value in a column
banks['Gender'].fillna('Male',inplace=True)
banks['Married'].fillna('Yes',inplace=True)
banks['Dependents'].fillna(0,inplace=True) 
banks['Education'].fillna('Graduate',inplace=True)
banks['Self_Employed'].fillna('No', inplace=True)
banks['ApplicantIncome'].fillna(2500,inplace=True)
banks['CoapplicantIncome'].fillna(0.0,inplace=True)
banks['LoanAmount'].fillna(120.0,inplace=True)
banks['Loan_Amount_Term'].fillna(360.0,inplace=True)
banks['Credit_History'].fillna(1.0,inplace=True)
banks['Property_Area'].fillna('Semiurban',inplace=True)
banks['Loan_Status'].fillna('Y',inplace=True)

print(banks) 

# Generate a pivot table with index as 'Gender', 'Married', 'Self_Employed' and values as 'LoanAmount' , using mean aggregation
avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount')
 
# Count where Self_Employed == Yes and Loan_Status == Y
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])

# Count where Self_Employed == No and Loan_Status == Y
loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])

# Given
Loan_Status = 614

# Calculate percentage of loan approval for self employed people 
percentage_se = (loan_approved_se / Loan_Status ) * 100

# Calculate percentage of loan approval for people who are not self-employed
percentage_nse = (loan_approved_nse / Loan_Status) * 100

# Convert Loan_Amount_Term which is in months to year
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12 )

# Find the number of applicants having loan amount term greater than or equal to 25 years 
big_loan_term = banks['Loan_Amount_Term'].loc[(loan_term >= 25)].count() 

# Groupby the 'banks' dataframe by Loan_Status
loan_groupby = banks.groupby(banks['Loan_Status'])

# Subset 'loan_groupby' to include only ['ApplicantIncome', 'Credit_History']
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

# Find the mean of 'loan_groupby'
mean_values = loan_groupby.mean()
print(mean_values) 

# -----------------
