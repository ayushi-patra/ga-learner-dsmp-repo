# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

# ======================
#   Confidence Interval
# ======================

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# path [File location variable]

#Code starts here
data = pd.read_csv(path)

# Creating sample data 
data_sample = data.sample(n=sample_size, random_state=0)

# Calculating Sample Mean for Installment column in sample data 
sample_mean = data_sample['installment'].mean()

# Calculating Sample Standard Deviation for Installment column in sample data 
sample_std = data_sample['installment'].std() 

# Calculating Margin of error 
margin_of_error = z_critical * (sample_std/math.sqrt(sample_size)) 

# Calculating Confidence Interval
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Calculating True Mean 
true_mean = data['installment'].mean() 

print(f'True Mean value is {true_mean}')
print(f'Confidence Interval value is {confidence_interval}')

if confidence_interval[0] < true_mean < confidence_interval[1]:
    print('Yes True Mean falls in the range of Confidence Interval')
else:
    print('No True Mean does not fall in the range of Confidence Interval') 

# =================
#       CLT
# =================
# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here

#Creating different subplots
fig, axes = plt.subplots(nrows=3, ncols=1)  


#Running loop to iterate through rows
for i in range(len(sample_size)):
    
    #Initialising a list
    m = []
    #Loop to implement the no. of samples
    for j in range(1000):
        sample_data = data.sample(sample_size[i])
        
        #Finding mean of a random sample
        sample_mean = sample_data['installment'].mean() 
        
        #Appending the mean to the list
        m.append(sample_mean)
        
    #Converting the list to series
    mean_series = pd.Series(m) 
    
    #Plotting the histogram for the series
    axes[i].hist(mean_series, bins=1000)
    

#Displaying the plot
plt.show()

# ==========================
#   Small Business Interest
# ==========================

# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here

# Removing the last character from the values in column and dividing by 100
data['int.rate'] = data['int.rate'].str.replace('%', '').astype(float)/100

#Applying ztest for the hypothesis
z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'], x2=None, value=data['int.rate'].mean(), alternative='larger')

if p_value<0.05:
    print('Reject the null hypothesis')
else:
    print('Accept the null hypothesis')

# ===================================
#   Installment and Loan Defaulting
# ===================================

# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here

#Applying ztest for the hypothesis
z_statistic, p_value = ztest(data[data['paid.back.loan']=='No']['installment'], data[data['paid.back.loan']=='Yes']['installment'])

if p_value<0.05:
    print('Reject the null hypothesis')
else:
    print('Accept the null hypothesis')

# ==============================
#   Purpose and Loan Defaulting
# ==============================

# --------------
#Importing header files
import pandas as pd
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here

# Subsetting the dataframe
yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()

#Concating yes and no into a single dataframe
observed = pd.concat([yes.T, no.T], axis=1, keys=['Yes', 'No'])
chi2, p, dof, ex = chi2_contingency(observed) 

print(f'The chi square value is {chi2} whereas the Critical Value is {critical_value}')

if chi2>critical_value:
    print('Reject the Null Hypothesis')
else: 
    print('Accept the Null Hypothesis')

