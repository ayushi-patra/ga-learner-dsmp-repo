# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

df = pd.read_csv(path)
# print(df.head())
total = len(df)

p_a = len(df[df['fico']>=700])/total
print(p_a) 
p_b = len(df[df['purpose']=='debt_consolidation'])/total
df1 = df['purpose']=='debt_consolidation'

p_a_b = len(df.groupby('purpose')['fico'].value_counts())/p_b 
print(p_a_b) 
result = p_a_b == p_a
print(result) 
# print(p_b_a == p_a)

# code ends here


# --------------
# code starts here
from fractions import Fraction
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/total
print(prob_lp) 


new_df = df['paid.back.loan'] == 'Yes' 
# print(new_df) 

prob_cs = len(df[df['credit.policy'] == 'Yes'])/total 
print(prob_cs)

a = df.groupby('paid.back.loan')['credit.policy'].value_counts()/df.groupby('paid.back.loan')['credit.policy'].count()
print(a) 

prob_pd_cs = 0.832318

bayes = 0.868482 
print(bayes) 

# code ends here 


# --------------
# code starts here
import matplotlib.pyplot as plt

ax = df['purpose'].value_counts().plot.bar(rot=45) 


df1 = df[df['paid.back.loan'] == 'No']
# ax = df.plot()
df1.plot(ax=ax)
# df.plot(x=df['purpose'].value_counts(), y=["A", "B", "C"], kind="bar")




# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
df['installment'].plot.hist()
df['log.annual.inc'].plot.hist() 


# code ends here


