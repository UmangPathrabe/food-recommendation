import pandas as pd

metadata=pd.read_csv('../food-recommendation/test1.csv')







C = metadata['average_rating'].mean()
print(C)

m = metadata['votes'].quantile(0.75)
print(m)

q_movies = metadata.copy().loc[metadata['votes'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['votes']
    R = x['average_rating']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

metadata['score'] = metadata.apply(weighted_rating, axis=1)
# metadata.to_csv('testfull.csv')

df = metadata
print(df.shape[0])
df = df[df.votes != 0]
print(df.shape[0])
df = df[df.votes != 1]
print(df.shape[0])
df.to_csv('testfinal1.csv')
df = df[df.votes != 2]
print(df.shape[0])
df.to_csv('testfinal2.csv')
df = df[df.votes != 3]
print(df.shape[0])
df.to_csv('testfinal3.csv')

# q_movies.to_csv('testx.csv')
# q_movies.to_csv('test2.csv')