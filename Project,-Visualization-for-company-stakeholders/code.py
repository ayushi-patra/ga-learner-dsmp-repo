# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot.bar()
#Code starts here


# --------------
#Code starts here
# print(data.head()) 


property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()

property_and_loan.plot(kind = 'bar', stacked=False) 

print(property_and_loan) 
# property_and_loan.dtype 
# property_and_loan.set(xlabel='Property Area', ylabel='Loan Status') 
# property_and_loan.set_xticklabels(data['Property_Area'], rotation=45)



# --------------
#Code starts here
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind = 'bar', stacked=False) 
plt.xlabel('Education Status')
plt.ylabel('Loan Status') 

plt.xticks(rotation=45) 


# --------------
#Code starts here
graduate = data[data['Education']=='Graduate']

not_graduate = data[data['Education']=='Not Graduate']


graduate['LoanAmount'].plot(kind='density', label='Graduate') 
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate') 









#Code ends here

#For automatic legend display
# plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1) 

ax_1.plot(data['ApplicantIncome'], data['LoanAmount']) 
ax_1.set_title('Applicant Income') 

ax_2.plot(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.plot(data['TotalIncome'], data['LoanAmount'])
ax_3.set_title('Total Income') 


