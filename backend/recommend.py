import pandas as pd
from pathlib import Path

# database_file = "backend/database/recipeData.csv"                   # direct path for windows
database_file = Path.cwd() / "database" / "recipeData.csv"        # For getting path in docker
# print("*****PATH is -", database_file)

df = pd.read_csv(database_file)     # Main data frame



def filter_database(userData):
    # print("*****Total data - ", df.shape[0])

    # Filter data by type of food
    match userData[0]:
        case 'Healthy':
            th = df['food types'].isin(['Healthy'])
            dff = df[th]
        case 'Veg':
            tv = df['food types'].isin(['Veg'])
            dff = df[tv]
        case 'Non-Veg':
            tnv = df['food types'].isin(['Non-veg'])
            dff = df[tnv]
        case 'Veg_Dessert':
            tdv = df['food types'].isin(['Veg dessert'])
            dff = df[tdv]
        case 'Non-Veg_Dessert':
            tdnv = df['food types'].isin(['Non-Veg dessert'])
            dff = df[tdnv]

    # Filtering data by time (in minutes) required to prepare
    m = dff['minutes'].isin(range(0, int(userData[1])))
    dff = dff[m]

    # Filtering data by number of steps required to prepare
    s = dff['n_steps'].isin(range(0, int(userData[2])))
    dff = dff[s]

    # Filtering data by number of ingredients required to prepare
    i = dff['n_ingredients'].isin(range(0, int(userData[3])))
    dff = dff[i]

    # print("*****Filtered data - ", dff.shape[0])



    # Sorting data by score which is based on average rating and number of votes
    df_sorted = dff.sort_values('score',ascending = False).head(30)         # Taking top 3 best recipes
    # print("*****sorted top 30 recipes - ", df_sorted.shape[0])
    
    # Taking 3 random recipes from top 30
    df_final = df_sorted.sample(3)
    # print("*****final recommended 3 recipes - ", df_final)


    return df_final.to_dict()



# for testing only
# userData = ['Non-Veg', '120', '10', '8']
# filter_database(userData)


