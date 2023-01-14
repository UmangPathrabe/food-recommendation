from flask import Flask, request, jsonify
from recommend import *     # imports functions from recommend.py

"""

    Description:
        This file runs the backend for API responses.

    Routes:
        route('/'): main API page.
        route('/api/test'): for testing if API GET and POST calls are working.
        route('/api/rec'): for receiving JSON data and passing array data to recommend.py

"""

# declare constants for connection
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)


# sample page
@app.route('/')
def api():
    """
    Description:
        Main api endpoint (unused)
    """
    return "<h1>API</h1>"


# api endpoint for test
@app.route('/api/test', methods=['GET', 'POST'])
def test():
    """
    Description:
        Test api endpoint used only for testing connection, ports and request methods
    """
    if request.method == 'POST':
        return jsonify({'test': 'POST success'})
    else:
        return jsonify({'test': 'GET success'})


userData = []
# api endpoint for recommendation
@app.route('/api/rec', methods=['POST'])
def rec():
    """
    Description:
        Test api endpoint used only for testing connection, ports and request methods.

    Parameters:
        userData (array): The user input data recived from JSON request.
    
    Returns:
        recommendation (JSON): Gives recipe JSON data to respone.

    Used by:
        Responds to POST api request from frontend.

    Requires:
        recommend.py for recommendation function.

    """
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
    # else:
    #     return jsonify({'description': 'POST not used'})


if __name__ == '__main__':
    app.run(host=HOST, debug=True, port=PORT)