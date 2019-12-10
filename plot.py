import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Per capita consumption of electricity.csv')

print(df.head())

desc=df.describe()
print(desc)

print(df.columns)


df=df.drop(40,axis=0)#to remove all india data that is total

for each in desc.columns:
    print('details of--',each)
    print('mean = ', desc.iloc[1][each])
    print('Standard Deviation = ', desc.iloc[2][each])
    print('Max = ', desc.iloc[7][each])
    print('Min = ', desc.iloc[3][each])
    print()
    plt.bar(df['Region/State/U.T.'],df[each],color='blue')
    plt.xticks(rotation=90)
    plt.ylabel('consumption of electricity(kwh)')
    plt.xlabel(each)
    plt.title('States vs Consumption of energy for '+ each)
    plt.show()  #this will show 6 different bar graphs for 6 different time period 

