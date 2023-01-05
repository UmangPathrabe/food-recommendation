import pandas as pd

df=pd.read_csv('../food-recommendation/test.csv')
df2=pd.read_csv('../food-recommendation/database/RAW_interactions.csv')

df2=df2.drop(['user_id','date','review'],axis=1)



C=df2['rating'].mean()

df3=df2.groupby(['recipe_id'])['rating'].agg(['mean','count'])
df3.reset_index(inplace=True)

df3.rename(columns={'mean':'average_rating','count':'votes'},inplace=True)

food_df = pd.merge(df, df3, left_on='id',right_on='recipe_id')

food_df.to_csv('test1.csv')


# After this I deleted coloums manually (change later)