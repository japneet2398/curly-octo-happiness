#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_excel("Covid_19_dataset.xlsx")


# In[2]:


for val in df:
    print(val)


# # Visualization 1: Age

# In[10]:


deceased=df[df["Current Status"]=="Deceased"]["Age Bracket"].dropna().values

recovered=df[df["Current Status"]=="Recovered"]["Age Bracket"].dropna().values

import matplotlib.pyplot as plt
plt.hist(deceased,bins=10)
plt.title("Deceased Persons")
plt.xlabel("Age")
plt.ylabel("No. of persons")
plt.yticks(range(12))
plt.show()

import matplotlib.pyplot as plt1
plt1.hist(recovered,bins=10)
plt.title("Recovered Persons")
plt.xlabel("Age")
plt.ylabel("No. of persons")
plt.figure(figsize=(50,50))
plt1.show()


# # Observations:
# From the above visualization it is observed that people of the age from 60-80 are more prone to death due to Covid 19 and in contrast to this people of the 20-50 have greater ability to overcome the disease to high immunity
#     

# In[ ]:





# # Visualization 2: States

# In[9]:


ds=df["Detected State"].dropna().unique()

dict={}
for i in ds:
    a=df[df["Detected State"]==i]["Patient Number"].values
    n=len(a)
    dict[i]=n

import matplotlib.pyplot as plt
plt.barh(ds,dict.values())
plt.rcParams["figure.figsize"] = (10,6)   #width=10 inches,height=6 inches
plt.title("States Affected")
plt.xlabel("No. of persons")
plt.ylabel("States")
plt.show()
#to view this graph appropriately use scroll view for the output cell


# # Observation:
# From the above visualization we can see that Maharashtra has the highest number of patients and is ahead with a great margin, Kerala is second and Tamil Nadu is third with respect to number of patients.

# In[ ]:





# # Visualization 3: Gender

# In[5]:


recovered=df[df["Current Status"]=="Recovered"]["Gender"].dropna().values      #total recovered(men and women)
recovered=list(recovered)
m_recovered=recovered.count("M")
f_recovered=recovered.count("F")

#print(m_recovered)
#print(f_recovered)

affected=df["Gender"].dropna()    #total affected (men and women)
affected=list(affected)
m_affected=affected.count("M")
f_affected=affected.count("F")

#print(m_affected)
#print(f_affected)

m_perc=(m_recovered/m_affected)*100    #calculating percentage
f_perc=(f_recovered/f_affected)*100

#print(m_perc)
#print(f_perc)

import matplotlib.pyplot as plt
y=[m_perc,f_perc]
plt.rcParams["figure.figsize"]=(5,5)
plt.bar(["Males","Females"],y)
plt.ylabel("Percentage Recovered")
plt.xlabel("Gender")
plt.title("Males and Females recovered with respect males and females affected resp")
plt.show()


# # Observation:
# It is observed that females are recovering at a faster pace as compared to males although the margin is very less

# In[ ]:




