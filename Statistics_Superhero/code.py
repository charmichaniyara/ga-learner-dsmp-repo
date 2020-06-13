# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
#1
data['Gender'] = data['Gender'].replace('-','Agender')

data['Gender'].value_counts().plot(kind="bar")
plt.title('Gender Distribution of Superheros')
plt.xlabel("Gender")
plt.ylabel("Frequency")
plt.show()

#2
data.Alignment.value_counts().plot(kind="pie")
plt.title('Alignment Distribution of Superheros')
#plt.xlabel("Alignment")
#plt.ylabel("Frequency")
plt.show()

#3
pearson_strength = data[["Combat","Strength"]].corr(method='pearson')
print("Pearson coefficient between Combat and Strength: ",pearson_strength.iloc[1,0])

pearson_Intel = data[["Combat","Intelligence"]].corr(method='pearson')
print("Pearson coefficient between Combat and Intelligence: ",pearson_Intel.iloc[1,0])


#4
q =data['Total'].quantile([0.99])
#print(q.get(key=0.99))

d = data[['Name','Total']][(data.Total > q.get(key=0.99))]
print(d)

super_best_names = d.Name.tolist()
print(super_best_names)


