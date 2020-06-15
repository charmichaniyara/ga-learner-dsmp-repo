# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
#Task 1
p_a = df[df.fico > 700].shape[0]/df.shape[0]
p_b = df[df.purpose == 'debt_consolidation'].shape[0]/df.shape[0]

df1 = df[df.purpose == 'debt_consolidation']
p_a_b = df1[df1.fico >700].shape[0]/df1.shape[0]

result = (p_a_b == p_a)
print("Result: ",result)

#Task 2
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]

new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]

bayes = (prob_pd_cs * prob_lp)/prob_cs
print("Bayes: ",bayes)

#Task 3
df.purpose.value_counts().plot(kind='bar')
plt.show()

df1 = df[df['paid.back.loan'] == 'No']
df1.purpose.value_counts().plot(kind='bar')
plt.show()
#Task 4


