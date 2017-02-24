# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:27:23 2017

@author: wilso
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:15:48 2017

@author: wilso
"""
import scipy 
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
import datetime as dt
import math as mt
def date_parse(string):
    return dt.datetime.strptime(string,'%Y-%m-%d %H:%M:%S.%f')
packages=[]
f=open('C:/Users/wilso/OneDrive/Grad/Datamining/Big Data datafile/signal1.txt')

rows = f.readlines(100000)
logret_list=[]
prprice=1
prtime=date_parse('2000-01-01 01:01:01.000000')

for row in rows:
        package ={}
        cols=row.split(",")
        try:
            package["date"]=date_parse(cols[0])
        except:
            continue
        
        package['price']=float(cols[1])
       # package['volume']=int(cols[2].strip('\n'))
         
        timediff=1000000*(package['date']-prtime).total_seconds()
        try:
            
            logret=mt.log10(package['price']/prprice)/timediff
        except: 
            continue
        logret_list.append(logret)
        prprice= package['price']
        prtime=package["date"]
        
        
    
logret_list=logret_list[1:]
#print(logret_list)

plt.hist(logret_list, bins=20,range=[-.0008,.0008])
print(scipy.stats.describe(logret_list))
        
    
            

       
            

         
    
    
  


