#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight= weight
        
    def introduce_self(self):  
        print("My name is "+ self.name)


# In[7]:



r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)


# In[10]:


r1.introduce_self()
r2.introduce_self()


# In[ ]:





# In[9]:





# In[ ]:




