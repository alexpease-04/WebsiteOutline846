#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[2]:


#Reading csv
df=pd.read_csv('CSV_Folder/policeKillings.csv')
df.head(5)


# In[3]:


#Count number of people killed of each race
dfRace=df.groupby(df['race'])
dfRace.count()


# In[4]:


#Pie Chart of all deaths
sb.set_palette(sb.color_palette('Reds_r'))
labels='Asian','Black','Hispanic','Native','Other','White'
explode=0,0.1,0,0,0,0
plt.pie(dfRace['id'].count(),labels=labels,explode=explode,autopct='%1.1f%%',shadow=True,radius=3)


# In[5]:


#Separating by Gender
dfM=df.loc[df['gender']=='M']
dfW=df.loc[df['gender']=='F']
dfM=dfM.groupby(dfM['race'])
dfW=dfW.groupby(dfW['race'])
dfW.count()


# In[6]:


sb.set_palette(sb.color_palette('coolwarm_r'))
N=6
men = (dfM['race'].count())
women = (dfW['race'].count())
ind = np.arange(N)
width = 0.5 
p1 = plt.bar(ind, men, width)
p2 = plt.bar(ind, women, width,bottom=men)
plt.ylabel('Deaths')
plt.xticks(ind, ('Asian', 'Black', 'Hispanic', 'Native', 'Other','White'))
plt.yticks(np.arange(0, 3000, 500))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()


# In[7]:


#Pie chart of women's deaths
labels='Asian','Black','Hispanic','Native','Other','White'
sb.set_palette(sb.color_palette('Reds_r'))
explode=0,0.1,0,0,0,0
plt.pie(dfW['race'].count(),labels=labels,explode=explode,autopct='%1.1f%%',shadow=True,radius=3)


# In[8]:


#adding race percentages of the US population
population=328000000
raceData={'Population%':[5.9,11.1,18.5,1.3,3.3,60.1]}
raceDf=pd.DataFrame(data=raceData,index=['A','B','H','N','O','W'])
raceDf['Population(Millions)']=raceDf['Population%']*3.28000
raceDf


# In[9]:


#adding percentages of police killings
raceDf['Killing%']=dfRace['id'].count()/4898*100
raceDf['Killing']=dfRace['id'].count()
raceDf


# In[10]:


#Find Killings/Million
raceDf['Killings/Million']=raceDf['Killing']/raceDf['Population(Millions)']
raceDf


# In[11]:


#Graphing Police Killings/Million
plt.title('Police Killings per Million of People of a Given Race')
plt.ylabel('Police Killings per Million people')
plt.xticks(ind, ('Asian', 'Black', 'Hispanic', 'Native', 'Other','White'))
plt.bar(ind,raceDf['Killings/Million'],width)


# In[12]:


#Using data from https://www.bjs.gov/index.cfm?ty=pbdetail&iid=6406
policeInteraction={'Number of Police-Initiated Interactions':[435694,182687,188492,107234],'Percent of Population':[.22,.4,.35,.52],'Deaths':[2477,1298,903,220]}
policeIntDf=pd.DataFrame(data=policeInteraction,index=['White','Black','Hispanic','Other'])
policeIntDf.head()


# In[14]:


#Find the percent of police interactions that end in death
policeIntDf['Percent of Interactions that End with Death']=policeIntDf['Deaths']/policeIntDf['Number of Police-Initiated Interactions']*100
policeIntDf


# In[16]:


#Graphing policeIntDf
plt.title('Percent of Police-Initiated Interactions that end in Death by Race')
plt.ylabel('Percent of Interactions That end in Death')
plt.xticks(np.arange(4), ('White','Black','Hispanic','Other'))
plt.bar(np.arange(4),policeIntDf['Percent of Interactions that End with Death'],width)

