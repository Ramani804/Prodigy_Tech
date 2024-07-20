import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn 

d=pd.read_csv('C:\\Users\\Dell\\Desktop\\prodigy_intern\\task1.csv')

data1 = pd.DataFrame(d)




del data1['2023']

#print(len(data1['Country Name']))
x=data1.columns[4:]

y = data1.iloc[0,4:]
print(y)


plt.xticks(rotation=90)


for i in range(0,265):
    for k in range(1,12):
       plt.subplot(24,11,k)
       plt.bar(x,data1.iloc[i,4:]) 
       plt.xticks(rotation=90)   
       plt.tight_layout()   
       
plt.show()
        