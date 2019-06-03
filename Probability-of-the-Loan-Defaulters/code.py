import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fractions import Fraction

# code starts here

df = pd.read_csv(path)
total = len(df)

# probability of  fico score greater than 700

p_a = len(df[df['fico']>=700])/total
print(p_a) 

# probability of purpose == debt_consolidation

p_b = len(df[df['purpose']=='debt_consolidation'])/total
print(p_b)

# Create new dataframe for condition ['purpose']== 'debt_consolidation' 

df1 = df['purpose']=='debt_consolidation'

# Calculate the P(A|B)

p_a_b = len(df.groupby('purpose')['fico'].value_counts())/p_a 
print(p_a_b) 

# Check whether the P(A) and P(B) are independent from each other

result = p_a_b == p_a
print(result) 


# probability of paid_back_loan is Yes
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/total
print(prob_lp) 

# create new dataframe for paid.back.loan == 'Yes'
new_df = df['paid.back.loan'] == 'Yes' 

# probability of the credit policy is Yes
prob_cs = len(df[df['credit.policy'] == 'Yes'])/total 
print(prob_cs)

# Calculate the P(B|A)

a = df.groupby('paid.back.loan')['credit.policy'].value_counts()/df.groupby('paid.back.loan')['credit.policy'].count()
print(a) 

prob_pd_cs = a.max()

# bayes theorem 
bayes = (prob_pd_cs * prob_lp) / prob_cs 
print(bayes) 

# Visualize 
# create bar plot for purpose
ax = df['purpose'].value_counts().plot.bar(rot=45) 
plt.title('Probability Distribution of Purpose')
plt.ylabel('Probability')
plt.xlabel('Number of Purpose')
plt.show()

#create new dataframe for paid.back.loan == 'No'
df1 = df[df['paid.back.loan'] == 'No']

# Plotting two DataFrame

df1.plot(ax=ax)
df1.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title('Probability Distribution of Purpose')
plt.ylabel('Probability')
plt.xlabel('Number of Purpose')
plt.show()

# Plot the histogram for visualization of the continuous variable
# Calculate median 
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

# histogram for installment
df['installment'].plot.hist(normed=True)
plt.show()

#histogram for log anual income
df['log.annual.inc'].plot.hist(normed=True) 
plt.show() 
