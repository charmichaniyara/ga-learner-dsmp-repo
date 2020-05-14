# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
#Step1
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census = np.concatenate((data,np.array(new_record)),axis=0)

#Step2
age = census[:,0]
#print(age)

max_age = age.max()
print("Maximum Age: ",max_age)

min_age = age.min()
print("Minimum Age: ",min_age)

age_mean = age.mean()
print("Mean Age: ",age_mean)

age_std = np.std(age)
print("Standard Deviation of Age: ",age_std)

#Step3
r = census[:,2]
b0 = (r==0)
race_0 = r[b0]

b1 = (r==1)
race_1 = r[b1]

b2 = (r==2)
race_2 = r[b2]

b3 = (r==3)
race_3 = r[b3]

b4 = (r==4)
race_4 = r[b4]

len_0 = len(race_0)

len_1 = len(race_1)

len_2 = len(race_2)

len_3 = len(race_3)

len_4 = len(race_4)

m = [len_0,len_1,len_2,len_3,len_4]
marray= np.array(m)
minor = marray.min()

if len_0 == minor:
    minority_race = 0
elif len_1 == minor:
    minority_race = 1
elif len_2 == minor:
    minority_race = 2
elif len_3 == minor:
    minority_race = 3
elif len_4 == minor:
    minority_race = 4
    
print("Minority Race: ",minority_race)

#Step4

a = census[:,0]
ag = (a > 60)
senior_citizens = a[ag]

wh = census[:,6]
a = census[:,0]
swh = (a > 60)
senior_wh = wh[swh]

working_hours_sum = senior_wh.sum()
print("Working hours sum: ", working_hours_sum)

senior_citizens_len = len(senior_citizens)

working_hours_sum = senior_wh.sum()

avg_working_hours = working_hours_sum / senior_citizens_len
print("Average Working Hours: ",avg_working_hours)

#Step5
h = census[:,1]
h1 = (h > 10)
high = h[h1]
#high

l = census[:,1]
l1 = (l <= 10)
low = l[l1]
#low

mh = census[:,7]
h = census[:,1]
h1 = (h > 10)
high_pay = mh[h1]
#high_pay
avg_pay_high = high_pay.mean()
print("Avg High Pay: ",avg_pay_high)

ml = census[:,7]
l = census[:,1]
l1 = (l <= 10)
low_pay = ml[l1]
#low_pay
avg_pay_low = low_pay.mean()
print("Avg Low Pay: ",avg_pay_low)





