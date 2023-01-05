import pandas as pd



df = pd.read_csv('../food-recommendation/test.csv')



# print(df.dtypes)

print("Data read success")




# Time to make
# print(df['minutes'].value_counts())

m15 = df['minutes'].isin(range(0, 15))
# d15 = df[m15]
# print(d15['minutes'].value_counts())
# print(m15.value_counts())
m30 = df['minutes'].isin(range(15, 30))
m60 = df['minutes'].isin(range(30, 60))
m120 = df['minutes'].isin(range(60, 120))
m180 = df['minutes'].isin(range(120, 180))
mx = df['minutes'].isin(range(180, ))


# tags (cusiene - mexican, chinese etc)



# Steps (Complexity, easy/hard)
# print(df['n_steps'].value_counts())
s3 = df['n_steps'].isin(range(0, 3))
print(s3.value_counts())
s6 = df['n_steps'].isin(range(3, 6))
s14 = df['n_steps'].isin(range(6, 14))
sx = df['n_steps'].isin(range(14, ))



# ingidients



# n of ingredients
# print(df['n_ingredients'].value_counts())
i3 = df['n_steps'].isin(range(0, 3))
i6 = df['n_steps'].isin(range(3, 6))
i10 = df['n_steps'].isin(range(6, 10))
ix = df['n_steps'].isin(range(10, ))


# food type (Healthy, Veg, Non-veg, Veg dessert, Non-veg dessert)
# print(df['food types'].value_counts())

th = df['food types'].isin(['Healthy'])
# print(df[th])
tv = df['food types'].isin(['Veg'])
tnv = df['food types'].isin(['Non-veg'])
tdv = df['food types'].isin(['Veg dessert'])
tdnv = df['food types'].isin(['Non-Veg dessert'])
