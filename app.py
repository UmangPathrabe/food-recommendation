from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

def recommend(text1,text2):
   combine = text1 + text2
   return combine

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    rec = recommend(text1,text2)
    result = {
        "output": rec
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

