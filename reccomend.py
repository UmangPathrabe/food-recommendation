import pandas as pd



df = pd.read_csv('../food-recommendation/testfinal3.csv')
print(df.shape[0])



mins = 0
step = 0
ingd = 0
type = 0



m15 = df['minutes'].isin(range(0, 15))
m30 = df['minutes'].isin(range(15, 30))
m60 = df['minutes'].isin(range(30, 60))
m120 = df['minutes'].isin(range(60, 120))
m180 = df['minutes'].isin(range(120, 180))
mx = df['minutes'].isin(range(180, ))

s3 = df['n_steps'].isin(range(0, 3))
s6 = df['n_steps'].isin(range(3, 6))
s14 = df['n_steps'].isin(range(6, 14))
sx = df['n_steps'].isin(range(14, ))

i3 = df['n_steps'].isin(range(0, 3))
i6 = df['n_steps'].isin(range(3, 6))
i10 = df['n_steps'].isin(range(6, 10))
ix = df['n_steps'].isin(range(10, ))

th = df['food types'].isin(['Healthy'])
tv = df['food types'].isin(['Veg'])
tnv = df['food types'].isin(['Non-veg'])
tdv = df['food types'].isin(['Veg dessert'])
tdnv = df['food types'].isin(['Non-Veg dessert'])



def filter_req(mins, step, ingd, type):

    match mins:
        case 0:
            df1 = df
        case 1:
            df1 = df[m15]
        case 2:
            df1 = df[m30]
        case 3:
            df1 = df[m60]
        case 4:
            df1 = df[m120]
        case 5:
            df1 = df[m180]
        case 6:
            df1 = df[mx]
    
    match step:
        case 0:
            df2 = df1
        case 1:
            df2 = df1[s3]
        case 2:
            df2 = df1[s6]
        case 3:
            df2 = df1[s14]
        case 4:
            df2 = df1[sx]
    
    match ingd:
        case 0:
            df3 = df2
        case 1:
            df3 = df2[i3]
        case 2:
            df3 = df2[i6]
        case 3:
            df3 = df2[i10]
        case 4:
            df3 = df2[ix]

    match type:
        case 0:
            df4 = df3
        case 1:
            df4 = df3[th]
        case 2:
            df4 = df3[tv]
        case 3:
            df4 = df3[tnv]
        case 4:
            df4 = df3[tdv]
        case 5:
            df4 = df3[tdnv]

    # print(df4.shape[0])
    return(df4)



# Only for testing
import random
def set_temp_val():
    global mins
    global step
    global ingd
    global type
    # mins = random.randint(0, 6)
    # step = random.randint(0, 4)
    # ingd = random.randint(0, 4)
    # type = random.randint(0, 5)
    mins = 3
    step = 3
    ingd = 3
    type = 2
    print(mins, step, ingd, type)



def main():
    set_temp_val()
    dff = filter_req(mins, step, ingd, type)
    print(dff.shape[0])
    print(dff.head(10))
    dff.to_csv('delete.csv')



if __name__=="__main__":
    main()