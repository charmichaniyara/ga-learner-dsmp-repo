# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

#Step1
bank = pd.DataFrame(bank_data)
print(bank.head())

categorical_var = bank.select_dtypes(include = 'object') 
# print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
# print(numerical_var)

#Step2
banks = bank.drop(['Loan_ID'],axis=1)

# print(banks.isnull().sum())

bank_mode = banks.mode(numeric_only=True)
# print(bank_mode)

banks.fillna(bank_mode, inplace=True)
print(banks.head())
print(banks.isnull().sum().values.sum())

#Step3
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)

#Step4
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]['Loan_Status'].value_counts()
print("Loan approved for Self-Employed People: ",loan_approved_se[0]) 

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]['Loan_Status'].value_counts()
print("Loan approved for NON Self-Employed People: ",loan_approved_nse[0])

percentage_se = loan_approved_se *100 /614
print("Percentage for Self-Employed People:", percentage_se)

percentage_nse = loan_approved_nse *100 /614
print("Percentage for NON Self-Employed People:", percentage_nse)

#Step5
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
#print(loan_term)

big_loan_term = (loan_term > 25).count()
print("big loan term: ", big_loan_term)

#Step6
columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])
print(mean_values)

#Code starts here




