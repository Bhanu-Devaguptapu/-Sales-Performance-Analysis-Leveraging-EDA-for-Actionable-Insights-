#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1STEP.First know the problem statements.
#2STEP.Collect the data from the respective sources.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns
#First load the csv file into the kernal
csv_file_path = 'westTeam.csv'
dataset = pd.read_csv(csv_file_path)
print(dataset)
#Find the type of the data in dataset
type(dataset)
dataset.info()
#Shape of data
dataset.shape
###Find the top columns and rows in dataset
dataset.head(10)
#Find the bottom columns and rows in dataset
dataset.tail(10)
#3STEP.Clean and Prepare the data
###To find null values in the dataset
f=dataset.isna().sum(axis=0)
f
#OBSERVATION:There are no null values in the given dataset
#To find the duplicate values from the dataset.
dataset.duplicated().sum()
#OBSERVATION: There are no null values as well as duplicated rows and columns in the given dataset.

#4STEP.Analyzing of the given dataset.
#######################
#We can find the count of unique values of dataset 
dataset.nunique()
#We can also find what are the data values in the each column of dataset separately and the range of values
np.unique(dataset.Product)
np.unique(dataset.Category)
np.unique(dataset.Cost)
np.unique(dataset.Discount)
np.unique(dataset.Quantity)
np.unique(dataset.SalesDate)
np.unique(dataset.CustomerID)
np.unique(dataset.CustomerReview)
np.unique(dataset.SalesPrice)
#By this we found the different values and limits between the datavalues in the dataset
#########################
#FIND the maximum and minimum values of the Cost
#Cost is the amount that a business spent for manufacturing the product
print(max(dataset.Cost))
print(min(dataset.Cost))
#FIND the minimum and Maximum values of SalesPrice
#Sales price is the amount that a business fix along with the profit to the customer
print(max(dataset.SalesPrice))
print(min(dataset.SalesPrice))
#OBSERVATION: As the cost price is more than sales price we can say that this year business has a loss.
###################
#To know basic statistical observations in dataset
print(dataset.describe())
#To count the products, no.of times they are sold
count_1=dataset['Product'].value_counts()
count_1
#Find the maximum values
dataset['Product'].value_counts().max()
#Data visualization for the products
#Barplot
#colorss = ['black','bisque','forestgreen','slategrey','limegreen','royalblue','lightcoral','yellow','red','darkturquoise','magenta','chocolate','crimson','purple','blue','orange','olive','darkslategrey','indigo','lightgreen']
#dataset['Product'].value_counts().plot.bar(color=colorss)
#Observation:By this barplot we can say that Fitness Tracker and Gaming Console has more sales in the year 2023.
####################
#We can find the count of category means in which method more sales are done
count_2=dataset['Category'].value_counts()
count_2
#Barplot
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
dataset['Category'].value_counts().plot.bar(color=colors)
#OBSERVATION: By using this graph we can say that most of the sales are done through online and promotions method.
####To know how diffrent products are sold in different method.
pd.crosstab(dataset.Product,dataset.Category)
###
#count_3=dataset['SalesDate'].value_counts()
#count_3'''


# In[5]:


#First load the csv file into the kernal
csv_file_path = 'westTeam.csv'
dataset = pd.read_csv(csv_file_path)
print(dataset)
#1st problem statement
dataset['SalesDate'] = pd.DatetimeIndex(dataset['SalesDate']).month
dataset['SalesDate'].value_counts()
df=pd.crosstab(dataset.SalesDate,dataset.Product) 
# look for the max values in each row
mxs = df.eq(df.max(axis=1), axis=0)
# join the column names of the max values of each row into a single string
df['Max'] = mxs.dot(mxs.columns + ', ').str.rstrip(', ')
df
colorss = ['black','bisque','forestgreen','slategrey','limegreen','royalblue','lightcoral','yellow','red','darkturquoise','magenta','chocolate','crimson','purple','blue','orange','olive','darkslategrey','indigo','lightgreen']
df.plot.bar(color=colorss)
plt.legend(loc='center left',fontsize=10,bbox_to_anchor=(1.25, 0.5))
#OBSERVATION: AS there are 3 sesons given when compared to all the sesons 10th month have more sales and in 9th month Fitness Tracker is in first place, in 10th month Laptop is in first place and in 11th month Novel is in first place.So, by this we can say that customers are much intrested in Fitness tracker,Laptops and Novels.


# In[9]:


#First load the csv file into the kernal
csv_file_path = 'westTeam.csv'
dataset = pd.read_csv(csv_file_path)
print(dataset)
###2nd Question
con=dataset['CustomerID'].value_counts()
con
#Observation: By this we can say that There are only 3 customers who are repeteadly purchasing the products from this company and only Customer_2 has high purchasing rate i.e 3334and customer_1.customer_2 has equal purchasing rate i.e 3333
##########
labels=['Customer_1','Customer_2','Customer_3']
con=dataset['CustomerID'].value_counts()
sizes=con
d=dataset['CustomerID'].value_counts()
c=('lightskyblue','yellowgreen','lightcoral')
explode=(0,0.1,0)
tickets=[3333,3334,3333]
total=np.sum(tickets)
def val_per(x): 
    return '{:.2f}%\n({:.0f})'.format(x, total*x/100)
plt.pie(tickets,explode=explode,labels=labels,colors=c,autopct=val_per,shadow=True,startangle=40, wedgeprops = {"edgecolor" : "black"})
plt.axis('equal')
plt.tight_layout()
plt.show()
#################
customer=pd.crosstab(dataset.Product,dataset.CustomerID)
mxs = customer.eq(customer.max(axis=1), axis=0)
customer['Max'] = mxs.dot(mxs.columns + ', ').str.rstrip(', ')
customer
#Observation: In This we can observe which customer purchased more products and what are they.
customer.plot.bar()
plt.legend(loc='center left',fontsize=10,bbox_to_anchor=(1.25, 0.5))
#In this bar graph we can see how the 3 customers brought the products and the maximum products they purchased.
###############
dataset['SalesDate'] = pd.DatetimeIndex(dataset['SalesDate']).month
dataset['SalesDate'].value_counts()
b=pd.crosstab(dataset.CustomerID,dataset.SalesDate)
b


# In[12]:


#First load the csv file into the kernal
csv_file_path = 'westTeam.csv'
dataset = pd.read_csv(csv_file_path)
print(dataset)
#############################
###3rd question:
#FIND the maximum and minimum values of the Cost
#Cost is the amount that a business spent for manufacturing the product
print(max(dataset.Cost))
print(min(dataset.Cost))
#FIND the minimum and Maximum values of SalesPrice
#Sales price is the amount that a business fix along with the profit to the customer
print(max(dataset.SalesPrice))
print(min(dataset.SalesPrice))
#OBSERVATION: As the cost price is more than sales price we can say that this year business has a loss.
#pd.crosstab(dataset.Cost,dataset.Product)
g=dataset[['Cost','SalesPrice']]
g
s=dataset['Profit/Loss']=np.where(dataset['Cost']<dataset['SalesPrice'],'Profit','Loss')
dataset['Difference']=dataset['Cost']-dataset['SalesPrice']
c=print(dataset[['Cost','SalesPrice','Profit/Loss','Difference']])
print(c)
pd.set_option('display.max_rows', 10000) #To print all the rows in the result dataset.
pl=print(dataset['Profit/Loss'])
pl
dataset['Difference']=dataset['Cost']-dataset['SalesPrice']
t=dataset[['Product','Profit/Loss','Difference']]
t
#OBSERVATION:By this we can say that all the product that are sold in loss.
dataset['Profit/Loss'].value_counts()
total_1 =dataset['Cost'].sum()
total_2=dataset['SalesPrice'].sum()
print(total_1,total_2)
#Observation:By the above observations we can understand that Salesprice is less than cost so the company shouls reduce the discounts and increase the sales price inorder to get profits.
#Difference column shows the difference between the Cost and SalesPrice.
i=dataset[['Product','Profit/Loss']].value_counts()
colorss = ['black','bisque','forestgreen','slategrey','limegreen','royalblue','lightcoral','yellow','red','darkturquoise','magenta','chocolate','crimson','purple','blue','orange','olive','darkslategrey','indigo','lightgreen']
i.plot.bar(color=colorss)
#Observation:In this graph we can see that all the products are in loss in all the three seasons.


# In[17]:


#First load the csv file into the kernal
csv_file_path = 'westTeam.csv'
dataset = pd.read_csv(csv_file_path)
print(dataset)
####################
#7th question:
dataset['CustomerRating'] = dataset.CustomerReview.astype(str).str[:1]
dataset['CustomerRating'] = dataset['CustomerRating'].astype(int)
dataset['CustomerRating'] = dataset['CustomerRating'].apply(lambda x: 5 if x > 5 else x)
dataset['CustomerRating'].value_counts()
##############
#By this we can find the no.of ratings for each product
pd.crosstab(dataset.Product,dataset.CustomerRating)
###############
#colors = sns.color_palette("deep") 
#sns.countplot(x='Product', data=dataset[dataset['CustomerRating'] == 5], order=dataset['Product'].value_counts().iloc[1:20].index,palette=colors)
#plt.xticks(rotation=90, fontsize=10, c="black")
#Observation: By the above graph we can find that "Gaming Console" has high 5 points rating. So, in order to get profits the company must increase the production of Gaming Console.
colors = sns.color_palette("deep") 
sns.countplot(x='Product', data=dataset[dataset['CustomerRating'] == 1], order=dataset['Product'].value_counts().iloc[1:20].index,palette=colors)
plt.xticks(rotation=90, fontsize=10, c="black")
#Observation:By the above graph we can tell that Headphones have least rating, so company must focus on the quality of the headphones product.


# In[14]:


#First load the csv file into the kernal
csv_file_path = 'westTeam.csv'
dataset = pd.read_csv(csv_file_path)
print(dataset)
###############
#4th question:
#f=pd.crosstab(dataset.Product,dataset.Quantity)
sns.countplot(x='Product', data=dataset[dataset['Quantity'] == 1], order=dataset['Product'].value_counts().iloc[1:20].index)
plt.xticks(rotation=90, fontsize=10, c="black")
#######################
sns.countplot(x='Product', data=dataset[dataset['Quantity'] == 10], order=dataset['Product'].value_counts().iloc[1:20].index)
plt.xticks(rotation=90, fontsize=10, c="black")
#######################
sns.countplot(x='Product', data=dataset[dataset['Quantity'] == 5], order=dataset['Product'].value_counts().iloc[1:20].index)
plt.xticks(rotation=90, fontsize=10, c="black")
##Observation:By the above graphs and ratings(from 7th question) we can say that "Air purifier" is sold in high quantity whereas "Digital Camera" sold in medium quantity and "Gaming Console" which is a set so it is sold at low quantity.
#In order to maintain customer loyality company ca increase the quality of "Digital Camera" to increase it sales/Profits.


# In[10]:


#First load the csv file into the kernal
csv_file_path = 'westTeam.csv'
dataset = pd.read_csv(csv_file_path)
print(dataset)
############################
#As we already found that the company is in loss by providing high discounts to the customers. Inorder to get profits the company should gradually decrease the discounts.
dataset['Difference']=dataset['Cost']-dataset['SalesPrice']
#############################
dataset['discount_in_rupees'] = (dataset['Discount'] / 100) * dataset['Cost']
dataset[['discount_in_rupees','Cost','SalesPrice','Difference','Discount']]
p=dataset['Difference'].sum()
q=dataset['discount_in_rupees'].sum()
print(p,q)
#Observation:We can see that difference between cost and sales is equal to the discount rupees provided by the company.So, inorder to gain profits the company must remove the discounts and increase the quality of the products as well as decrease the cost price.


# In[16]:


#First load the csv file into the kernal
csv_file_path = 'westTeam.csv'
dataset = pd.read_csv(csv_file_path)
print(dataset)
###########################
#6th Question:
#Observation:As we know that when we remove the discount percentage from sales then the company may get profits.
#So, now we will add the dicount to the salesPrice as well as additional amount so that the company may get profit in the future.
dataset['discount_in_rupees'] = (dataset['Discount'] / 100) * dataset['Cost']
r=dataset['discount_in_rupees']+dataset['SalesPrice']
r
#r is equal to the Cost price of the company, even if the company sell the product in the same amount there is neither loss nor profit.
#So,they must add an extra amount to the SalesPrice
dataset['Difference']=dataset['Cost']-dataset['SalesPrice']
dataset['Sales']=r+dataset['Difference']
dataset['Sales']
#Now the comapny has profits in its sales, if we show it in graph for future analysis it will be as follows:
s=dataset['Sales'].sum()
t=dataset['Cost'].sum()
column_names = ['Cost', 'Sales']
values = [t, s]  # Values for the two columns
plt.figure(figsize=(3,5))
plt.bar(column_names, values, color=['blue', 'orange'])
plt.xlabel('Columns')
plt.ylabel('Values')
plt.title('Comparison of Cost and Sales in Future')
plt.show()
#This barplot shows the difference between Cost and SalesPrice and increase in SalesPrice in future.
x=dataset['SalesPrice'].head(20)
y=dataset['Sales'].head(20)
plt.scatter(x,y)
plt.xlabel('Sales in future')
plt.ylabel('Count')
plt.show()
###########################
#We can find the count of category means in which method more sales are done
count_2=dataset['Category'].value_counts()
count_2
#Barplot
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
dataset['Category'].value_counts().plot.bar(color=colors)
#OBSERVATION: By using this graph we can say that most of the sales are done through online and promotions method.So, if company  increase focus on store and gifts category there may be increase in sales in future.
####################
dataset['SalesDate'] = pd.DatetimeIndex(dataset['SalesDate']).month
dataset['SalesDate'].value_counts()
df=pd.crosstab(dataset.SalesDate,dataset.Product) 
# look for the min values in each row
mx = df.eq(df.min(axis=1), axis=0)
# join the column names of the min values of each row into a single string
df['Min'] = mx.dot(mx.columns + ', ').str.rstrip(', ')
df
################


# In[2]:


total_1 =dataset['Cost'].sum()
total_2=dataset['SalesPrice'].sum()
print(total_1,total_2)


# In[4]:


np.unique(dataset.Product)

