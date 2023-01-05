import numpy as np
import pandas as pd
# import seaborn as sns
# import sys
# import matplotlib.pyplot as plt
# import seaborn as sns

df = pd.read_csv('../food-recommendation/database/RAW_recipes.csv')

# print(df.head())
# print(df.dtypes)



df[['calories','total fat (PDV)','sugar (PDV)','sodium (PDV)','protein (PDV)','saturated fat (PDV)','carbohydrates (PDV)']] = df.nutrition.str.split(",",expand=True) 
df['calories'] =  df['calories'].apply(lambda x: x.replace('[','')) 
df['carbohydrates (PDV)'] =  df['carbohydrates (PDV)'].apply(lambda x: x.replace(']','')) 
df[['calories','total fat (PDV)','sugar (PDV)','sodium (PDV)','protein (PDV)','saturated fat (PDV)','carbohydrates (PDV)']] = df[['calories','total fat (PDV)','sugar (PDV)','sodium (PDV)','protein (PDV)','saturated fat (PDV)','carbohydrates (PDV)']].astype('float')

# print(df.dtypes)
# print(df.head())



df['food types'] = np.nan
df['food types'] = df['food types'].astype('str')



for i in df['ingredients'].index:
    if('eggs' not in df['ingredients'][i]):
         if('ice-cream' in df['ingredients'][i] or 'chocolate' in df['ingredients'][i] or 'cookies' in df['ingredients'][i]):
                df['food types'][i]='Veg dessert'
    elif('eggs' in df['ingredients'][i]):
        if('ice-cream' in df['ingredients'][i] or 'chocolate' in df['ingredients'][i] or 'cookies' in df['ingredients'][i]):
                df['food types'][i]='Non-Veg dessert'



for i in df.index:
    if(df['food types'][i]!='Veg dessert' and df['food types'][i]!='Non-Veg dessert' and 20<df['calories'][i]<300):
        df['food types'][i]='Healthy'



for i in df.index:
    if(df['food types'][i]!='Veg dessert' and df['food types'][i]!='Non-Veg dessert' and df['food types'][i]!='Healthy'):
        if('chicken' in df['ingredients'][i] or 'eggs' in df['ingredients'][i] or'ham' in df['ingredients'][i] or 'pepperoni' in df['ingredients'][i] ):
            df['food types'][i]='Non-veg'



for i in df.index:
    if(df['food types'][i]!='Veg dessert' and df['food types'][i]!='Non-Veg dessert' and df['food types'][i]!='Healthy' and df['food types'][i]!='Non-veg'):
        df['food types'][i]='Veg'


print(df['food types'].value_counts())
# df.to_csv('test.csv')





# types = pd.get_dummies(df['food types'])
# df1 = pd.concat([df,types],axis = 1)
# df1.head()
# print(df1.dtypes)

# df1.to_csv('test1.csv')





# Time to make
# m_30 = df['minutes'].isin([4, 2, 6])
# m_60 = df['minutes'].isin([4, 2, 6])

# tags (cusiene - mexican, chinese etc)

# Steps (Complexity, easy/hard)

# ingidients

# n of ingridients

# food type (Healthy, Veg, Non-veg, Veg dessert, Non-veg dessert)