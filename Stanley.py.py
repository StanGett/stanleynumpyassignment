#!/usr/bin/env python
# coding: utf-8

# # 1. Use various functions under numerical Python to execute the following instructions.
# a) Generate a 2 by 3 matrix containing element from 1 to 6 and multiply it by a scale factor of two.

# In[1]:


import numpy as np


# In[2]:


x=np.array([[1,2,3],[4,5,6]])


# In[3]:


print(x*2)


# b) Create a 3 by 3 identity matrix

# In[4]:


matrix=np.identity(3)


# In[5]:


print(matrix)


#  c) Create a 1-D arry1 which contains element ranging from 0 to twenty-seven.
#    Convert arry1 to a 3-D arry2

# In[6]:


arry1=np.arange(27)


# In[7]:


print(arry1)


# # converting the 1-D arry to a3-D arry

# In[8]:


arry1=np.arange(27)


# In[9]:


arry2=arry1.reshape(3,3,3)


# In[10]:


print(arry2)


# # d) create a 2-D arry  containing 1 to 6 and 7 to 12 and sticking the two arrys vertically and horizontally.

# In[11]:


arry_A=np.array([[1,2,3], [4,5,6]])


# In[12]:


print(arry_A)


# In[13]:


arry_B= np.array([[7,8,9],[10,11,12]])


# In[14]:


print(arry_B)


# In[15]:


V_stack=np.vstack((arry_A,arry_B))


# In[16]:


print(V_stack)


# In[17]:


h_stack=np.hstack((arry_A,arry_B))


# In[18]:


print(h_stack)


# # e) from 0 to 100 sequence with equally spacing 0f 5.

# In[19]:


sequence=np.arange(0,101,5)


# In[20]:


print(sequence)


# In[ ]:





# # Use the various Functions associated with Pandas to answer the following Questions
# a) students names

# In[6]:


import pandas as pd


# In[7]:


student_names= ['Stanley Gettor','Lordina Obour','Daniel Wilson','Michael Obour','John Avedzi','Olivia Teye']


# In[8]:


students=pd.DataFrame(student_names,columns=['Names'])


# In[9]:


print(students)


# b)  Write a program to create a DataFrame teams using a list of names of Ghana Premier League Teams and the goals they scored in their previous five matches.

# In[25]:


teams_names=['Accra Heart of OAK','Asante Kotoko','Ashanti Gold SC','Berekum Chelsea','Kumasi Asante Kotoko','WAFA','Bachem united']


# In[26]:


goals_dict= {'Accra Heart of OAK':[1,2,0,3,1],
         'Asante Kotoko':[1,0,1,2,0],
         'Ashanti Gold SC':[2,3,2,0,1],
         'Berekum Chelsea':[1,0,0,3,2] ,
         'Kumasi Asante Kotoko':[1,3,2,1,4],
         'WAFA':[2,9.3,0,1],
         'Bachem united':[1,0,0,5,3]}


# In[27]:


teams = pd.DataFrame.from_dict(goals_dict,orient='index', columns=['Match 1','Match 2','Match 3','Match 4','Match 5'])


# In[28]:


teams['teams_names']=teams_names


# In[29]:


teams.set_index('teams_names', inplace = True)


# In[30]:


print(teams)


# # c) Write a program to create a DataFrame countries using a dictionary which stored country name ,capitals, and population s of the country. Do this for west African Countries.

# In[31]:


data= {'Country':['Benin','Ghana','BUrkina Faso','Cape Verde','Cote d/vore','Gambia','Guinea','Togo','Nigeria','Mali','senegal','Sierra Leon','The Gambia','Niger','Guinea-Bissau','Mauritania'],
       'Capital':['Porto-Novo','Accra','Ouagadogou','praia','Yamoussoukro','Banjul','Abijan','Conakry','Lome','Lagos','Dakar','Free Town','Bamako','Banjul','Niamey','Bissau' ],
       'Population':[24245532,12340112,54463434,67254433,18443360,11121904,20353354,21212239,59677346,90966683,12124442,32114787,43261287,12432332,8675748,12322347] }


# In[33]:


countries=pd.DataFrame(data)


# In[34]:


print(countries)


# # 2d) A programme capturing the prtovided dataset in python.

# In[36]:


#creating the given table
#names of the teams and the goals
import pandas as pd
Sno =[1,2,3,4,5,6,7]
team=['Accra Heart of Oak','Asante Kotoko','Ebusua Duafs', 'Secondi Hassacas','Okwahu United','Tano Bofoakwa','BA United']
gf= [120,90,90,80,78,70,71]
ga=[35,55,60,43,39,50,55]
pts=[80,60,60,55,53,49,44]


# In[39]:


# assigning the headings to the table
teams_standing={'SNO':Sno,'Team':team,'GF':gf,'GA':ga,'PTS':pts}


# In[40]:


#creating the headings to dataframe
league_table= pd.DataFrame(teams_standing)
league_table


# In[41]:


#ii.b. teams that conceeded less than 80 goals
league_table[league_table['GF']<80]


# In[42]:


#ii.c. teams that had less than 60points 
league_table[league_table['PTS']<60]


# In[ ]:




