#!/usr/bin/env python
# coding: utf-8

# In[39]:


#fibonacci series

#taking input for the desired terms c and defining c as a integer for integer values

#providing the first and second number of the series a and b

#condition for terms terms can't be negative so using the if else statement 

#printing b 

#for loop is used for continues of the series

# + operator is used for the first term of the series c= a+ b

#now printing the c for next term of the series  by print(c)

#now a has to take the value of next term of the series so giving the value a=b

#and b has to take the value of next term of the series which was print earlier by adding previous term and it is c , so b=c

#it will be continues till satisfying the range

c = int(input()) 
a=0
b=1
if c<=0:
    print('enter number greater than 0 ')
else:
    print(b)
for i in range(0,c):
    c=a+b
    print(c)
    a=b
    b=c
   


# 

# In[ ]:




