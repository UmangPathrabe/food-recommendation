import pandas as pd

df = pd.read_csv('../food-recommendation/testfinal3.csv')
print("*****Total data - ", df.shape[0])
dff = pd.DataFrame()


from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
usrd = []


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

i3 = df['n_ingredients'].isin(range(0, 3))
i6 = df['n_ingredients'].isin(range(3, 6))
i10 = df['n_ingredients'].isin(range(6, 10))
ix = df['n_ingredients'].isin(range(10, ))

th = df['food types'].isin(['Healthy'])
tv = df['food types'].isin(['Veg'])
tnv = df['food types'].isin(['Non-veg'])
tdv = df['food types'].isin(['Veg dessert'])
tdnv = df['food types'].isin(['Non-Veg dessert'])

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()



def get_val():
    global mins
    global step
    global ingd
    global type
    mins = int(usrd[0])
    step = int(usrd[1])
    ingd = int(usrd[2])
    type = int(usrd[3])
    print("*****Selection from web - ", usrd)


def filter_req(mins, step, ingd, type):
    print("*****Selection in py - ", mins, step, ingd, type)
    global df1
    global df2
    global df3
    global df4

    match mins:
        case 0:
            df1 = df
        case 1:
            df1 = df[m15]
        case 2:
            df1 = df[m30]
        case 3:
            df1 = df[m60]
            print("*****df1 data - ", df1.shape[0])
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
            print("*****df2 data - ", df2.shape[0])
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
            print("*****df3 data - ", df3.shape[0])
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
            print("*****df4 data - ", df4.shape[0])
        case 4:
            df4 = df3[tdv]
        case 5:
            df4 = df3[tdnv]

    # print(df4.shape[0])
    return(df4)


def get_rec():
    global dff
    print("*****Filtered data - ", dff.shape[0])
    reco = dff.sample(3)
    return reco


def run_all():
    global dff
    get_val()
    dff = filter_req(mins, step, ingd, type)
    # print(dff.shape[0])
    # print(dff.head(10))
    rec = get_rec()
    # dff.to_csv('delete.csv')
    print("*****Final data rec - \n", rec)
    return rec





# def main():
#     global usrd 
#     usrd = [3, 3, 3, 3]
#     run_all()

# if __name__=='__main__':
#     main()





@app.route('/', methods =["GET", "POST"])
def test():
    if request.method == "POST":
        usrd.clear()
        typ = request.form.get("type")
        min = request.form.get("mins")
        ste = request.form.get("step")
        ing = request.form.get("ingd")
        usrd.append(min)
        usrd.append(ste)
        usrd.append(ing)
        usrd.append(typ)
        return redirect(url_for('output'))
    else:
        return render_template("test2.html")

@app.route('/output')
def output():
    rec = run_all()
    # return render_template("testout.html", out=usrd, display=rec)
    return rec.to_html(header="true", table_id="table")
    # display=[rec.to_html]
    # display=[rec.to_html(classes='data', header="true")]

if __name__=='__main__':
    app.run(debug=True)