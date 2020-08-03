# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder




#Loading the data
data=pd.read_csv(path)
#data.head(10)

#Code starts here

#plotting histogram
data['Rating'].plot(kind='hist')
plt.show()

#subset dataframe where rating <= 5
data = data[data['Rating'] <= 5]

#plotting histogram again
data['Rating'].plot(kind='hist')
plt.show()

#sum of null values of each column
total_null = data.isnull().sum()
#Percentage of null values of each column
percent_null = total_null / data.isnull().count()
#Concatenating total and percentage
missing_data = pd.concat([total_null,percent_null], axis=1, keys=['Total','Percentage'])
print(missing_data)

#dropping null values
data.dropna(inplace=True)

#sum of null values of each column
total_null1 = data.isnull().sum()
#Percentage of null values of each column
percent_null1 = total_null1 / data.isnull().count()
#Concatenating total and percentage
missing_data1 = pd.concat([total_null1,percent_null1], axis=1, keys=['Total','Percentage'])
print(missing_data1)

#Category vs Rating
plt.figure(figsize=(10,10))
cat = sns.catplot(x='Category', y='Rating', data=data, kind='box', height=10)
cat.set_xticklabels(rotation=90)
plt.title('Rating vs Category Boxplot')
plt.show()

#Removing ',' from Installs column
data['Installs'] = data['Installs'].str.replace(',','')
#Removing '+' from Installs column
data['Installs'] = data['Installs'].str.replace('+','')
#Converting Install column datatype to int
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le = LabelEncoder()
#Label encoding the column to reduce the effect of a large range of values
data['Installs'] = le.fit_transform(data['Installs'])

#Rating vs Installs
plt.figure(figsize=(10,10))
sns.regplot(x='Installs', y='Rating', data=data)
plt.title('Rating vs Installs RegPlot')
plt.show()

#Removing '$' from Installs column
data['Price'] = data['Price'].str.replace('$','')
#Converting Price column datatype to float
data['Price'] = data['Price'].astype(float)

#Rating vs Price
plt.figure(figsize=(10,10))
sns.regplot(x='Price', y='Rating', data=data)
plt.title('Rating vs Price RegPlot')
plt.show()

#Find number of unique Genres
print(len(data['Genres'].unique()),' Genres')
#Splitting the column to include only the first genre of each app
data['Genres'] = data['Genres'].str.split(';').str[0]
#Grouping by Genres and finding mean
gr_mean = data[['Genres','Rating']].groupby(['Genres']).mean()
print(gr_mean.describe())

#Sorting by Rating
gr_mean = gr_mean.sort_values('Rating')

print("minimum : ", gr_mean.head(1))
print("maximum : ", gr_mean.tail(1))


