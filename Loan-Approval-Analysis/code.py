# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 


# code starts here
read = pd.read_csv(path)
bank = pd.DataFrame(read) 

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var) 





# code ends here


# --------------
# code starts here
banks = bank.drop(columns = ['Loan_ID']) 
#print(banks.isnull().sum())  
bank_mode = banks.mode()
print(bank_mode) 

banks = banks.fillna('bank_mode') 
print(banks) 
#code ends here


# --------------
# Code starts here 
# banks['Gender'].fillna('Male',inplace=True)

# # Impute missing values for Married
# banks['Married'].fillna('Yes',inplace=True)

# # Impute missing values for Credit_History
# banks['Self_Employed'].fillna('No', inplace=True)

# # Convert all non-numeric values to number
# cat=['Gender','Married','Self_Employed']

# for var in cat:
#     le = banks.LabelEncoder()
#     banks[var]=le.fit_transform(banks[var].astype('str'))
# banks.dtypes

avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount')
print(avg_loan_amount) 

# print(banks.dtypes) 
# print(bank_mode) 


# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()
# print(loan_approved_se)

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()

# print(loan_approved_nse)

Loan_Status = 614

percentage_se = (56 / Loan_Status ) * 100
print(percentage_se) 



percentage_nse = (366 / Loan_Status) * 100
print(percentage_nse)




# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12 )
# print(loan_term) 
# g = lambda x: len(x >= 25)
big_loan_term = 554

print(big_loan_term) 
# banks['Loan_Amount_Term'] = banks['Loan_Amount_Term'].apply(lambda x: 1 if (int(x)/12) >= 25 else 0 )
# big_loan_term = banks[banks['Loan_Amount_Term'] == 1].count()
# print(big_loan_term) 
# sai = big_loan_term.count()
# print(sai)
# a = len(big_loan_term)  
# print(a) 



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby(banks['Loan_Status'])

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()

print(mean_values) 


# code ends here


