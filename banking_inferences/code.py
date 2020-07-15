# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here

#Confidence Interval
data_sample = data.sample(n=sample_size,random_state=0)

confidence_interval = [data_sample['installment'].mean() - (z_critical*data_sample['installment'].std()/math.sqrt(sample_size)), data_sample['installment'].mean() + (z_critical*data_sample['installment'].std()/math.sqrt(sample_size))]
print("confidence interval: ",confidence_interval)

true_mean = data['installment'].mean()
print("true mean: ",true_mean)

#CLT
sample_size = np.array([20,50,100])

fig, axes = plt.subplots(3,1, figsize=(10,20))

for i in range(len(sample_size)):
    m = []
    
    for j in range(1000):
        
        mean = data['installment'].sample(sample_size[i]).mean()
        
        m.append(mean)
        
    mean_series = pd.Series(m)
    
    axes[i].hist(mean_series)
    
plt.show()


#Small Business Interests
data['int.rate.new'] = data['int.rate'].map(lambda x: str(x)[:-1])

data['int.rate.new'] = data['int.rate.new'].astype(float)/100

z_statistic_1, p_value_1 = ztest(x1 = data[data['purpose'] == 'small_business']['int.rate.new'], value = data['int.rate.new'].mean(), alternative='larger')

print("z-statistic : ",z_statistic_1)
print("p-value : ",p_value_1)

#Installment vs Loan Defaulting
z_statistic_2, p_value_2 = ztest(x1 = data[data['paid.back.loan'] == 'No']['installment'], x2 = data[data['paid.back.loan'] == 'Yes']['installment'])

print("z-statistic 2 : ",z_statistic_2)
print("p-value 2 : ",p_value_2)

#Purpose vs Loan Defaulting
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()

no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()

observed = pd.concat([yes.transpose(), no.transpose()], 1, keys=['Yes','No'])

chi2, p , dof, ex = chi2_contingency(observed)

print("chi statistic is : ", chi2)
print("critical value : ", critical_value)




