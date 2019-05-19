# --------------
# Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# path of the data file, 
path

# Code starts here 
data = pd.read_csv(path) 

data['Gender'].replace('-', 'Agender', inplace = True)
gender_count = data['Gender'].value_counts() 
plt.bar(gender_count, height = 0.5, align='center', alpha=0.5)  

# What's the stand of the members of 'ASB'. Does good overpower evil or does evil overwhelm good? 
alignment = data.Alignment.value_counts()
plt.pie(alignment) 
plt.title("Character Alignment")

# Find out if combat skills relate to person's strength or it's intelligence?
sc_df = data[['Strength', 'Combat']]
sc_covariance = data.Strength.cov(data.Combat) 
sc_strength = data.Strength.std()
sc_combat = data.Combat.std() 

sc_pearson = sc_covariance / (sc_combat * sc_strength) 

ic_df = data[['Intelligence', 'Combat']]
ic_covariance = data.Intelligence.cov(data.Combat) 
ic_intelligence = data.Intelligence.std()
ic_combat = data.Combat.std() 

ic_pearson = ic_covariance / (ic_combat * ic_intelligence) 

# Who are the best of the best in this superhero universe?
total_high = data.Total.quantile(0.99) 

super_best = data[data['Total'] > total_high] 
print(super_best)

super_best_names = super_best.Name.tolist()  
print(super_best_names) 


# Of the top 1% members of 'ASB', measure certain attributes in case they go rogue and become threatening to the human kind.

x = np.linspace(0,100)
y = np.linspace(0,100) 

f, (ax_1, ax_2, ax_3) = plt.subplots(3, sharex=True, sharey=True)
ax_1.boxplot(data[['Intelligence']]) 
ax_1.set_title('Intelligence')
ax_2.boxplot(data[['Speed']]) 
ax_2.set_title('Speed')
ax_3.boxplot(data[['Power']]) 
ax_3.set_title('Power')
