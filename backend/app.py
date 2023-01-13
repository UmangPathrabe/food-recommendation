from flask import Flask, request, jsonify
from recommend import *     # imports functions from recommendation file


# declare constants for connection
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)

# sample page
@app.route('/')
def hello():
    return "<h1>API</h1>"

# sample api endpoint
@app.route('/api/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        return jsonify({'test': 'POST success'})
    else:
        return jsonify({'test': 'GET success'})

userData = []
# api endpoint for recommendation
@app.route('/api/rec', methods=['GET', 'POST'])
def rec():
    if request.method == 'POST':
        # get formData from post request
        jsonData = request.get_json('Finput')
        # print("*****JSON data from frontend", jsonData, type(jsonData))

        # storing user data from json in array
        userData.clear()
        userData.append(jsonData.get('type'))
        userData.append(jsonData.get('mins'))
        userData.append(jsonData.get('step'))
        userData.append(jsonData.get('ingr'))
        # print("*****user data array from frontend", userData)

        # passing user data for filtering
        recommendation = filter_database(userData)     # calls function from recommend.py

        return jsonify(recommendation)
    else:
        return jsonify({'error': 'POST not used'})


if __name__ == '__main__':
    app.run(host=HOST, debug=True, port=PORT)