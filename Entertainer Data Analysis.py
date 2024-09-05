#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[11]:


#Load the excel file into a psndas Dataframe
df = pd.read_excel('Entertainer - Basic Info.xlsx')


# In[14]:


#Save the Dataframe to a CSV file
df.to_csv('Basic Info.csv', index=False)
print('Conversion complete')


# In[18]:


filepath = 'Basic Info.csv'


# In[20]:


data =pd.read_csv(filepath)


# In[22]:


data.head()


# In[25]:


data.shape


# In[28]:


data.dtypes


# In[30]:


data.isnull()


# In[31]:


data.info()


# In[33]:


data['Entertainer'].describe()


# In[36]:


count_Adele =len(data['Entertainer'][data['Entertainer']=='Adele'])
count_Bob=len(data['Entertainer'][data['Entertainer']=='Bob'])


# In[37]:


print("As per dataset, we have %d records Entertainer as 'Adele' and %d as 'Bob'" %(count_Adele,count_Bob))


# In[40]:


data.describe()


# In[41]:


data = data[data['Entertainer'] != 'Adele']


# In[42]:


data[data['Entertainer'] == 'Adele'].mean()


# In[47]:


#Load the Excel file into a pandas DataFrame
excel_file = pd.read_excel('Entertainer - Breakthrough Info.xlsx')

#Save the DataFrame to a CSV file
excel_file.to_csv('Breakthrough Info.csv' , index=False)

print('Conversion complete')


# In[49]:


import plotly.express as px
df = pd.read_csv("Breakthrough Info.csv")


# In[51]:


df.shape


# In[52]:


df.columns


# In[53]:


x = df.groupby(['Breakthrough Name']).size().reset_index(name = 'counts')
print(x)


# In[54]:


pieChart = px.pie(x, values='counts' , names='Breakthrough Name' , title='Several Songs')
pieChart.show


# In[57]:


import plotly.graph_objects as go

#Create a simple scatter plot
fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 1, 3]))

#Display the figure
fig.show()


# In[59]:


df['Year of First Oscar/Grammy/Emmy'] = df['Year of First Oscar/Grammy/Emmy'].fillna('Year of First Oscar/Grammy/Emmy').fillna('Year of First Oscar/Grammy/Emmy not specified')
df.head()


# In[60]:


Entertainer_list = pd.DataFrame()
print(Entertainer_list)


# In[61]:


Entertainer_list = df.Entertainer.str.split(',', expand=True).stack()
print(Entertainer_list)


# In[62]:


Entertainer_list = Entertainer_list.to_frame()
print(Entertainer_list)


# In[72]:


import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[65]:


plt.figure(figsize= (10,6))
df.groupby('Year of Breakthrough/#1 Hit/Award Nomination')


# In[66]:


df['Year of First Oscar/Grammy/Emmy'].dtype
df['Year of Breakthrough/#1 Hit/Award Nomination'].dtype


# In[67]:


df['Year of First Oscar/Grammy/Emmy'] = pd.to_numeric(df['Year of First Oscar/Grammy/Emmy'], errors='coerce')
df['Year of Breakthrough/#1 Hit/Award Nomination'] = pd.to_numeric(df['Year of Breakthrough/#1 Hit/Award Nomination'], errors='coerce')


# In[69]:


df.insert(3, 'Best year' , df['Year of First Oscar/Grammy/Emmy'] - df['Year of Breakthrough/#1 Hit/Award Nomination'])


# In[70]:


df['Best year'].dtype


# In[75]:


df['Best year'].plot(kind= 'hist', bins=10)
plt.xlabel('Years')
plt.ylabel('Frequency')
plt.title('Distribution of Best Year')
plt.show


# In[76]:


df1= df[['Entertainer','Year of Breakthrough/#1 Hit/Award Nomination','Breakthrough Name','Year of First Oscar/Grammy/Emmy']]


# In[77]:


df1.hist(bins = 20, figsize =(14,12))


# In[78]:


df.Entertainer.value_counts()


# In[79]:


df2= df.groupby('Year of Breakthrough/#1 Hit/Award Nomination')['Year of First Oscar/Grammy/Emmy'].sum().plot(kind='line')

