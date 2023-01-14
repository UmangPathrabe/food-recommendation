# Flask API Template

This project is backend API built with Python and Flask for recipe recommendation.

## Built With

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Docker](https://www.docker.com/)

## Prerequisites

You will need the following things properly installed on your computer:
* [Python v3.10.9](https://www.python.org/)
* [Flask v2.2.2](http://flask.pocoo.org/)

### For running directly on Windows

* Install [python](https://www.python.org/downloads/)

* run to install flask:
```
  $ pip install Flask
```

### Running
run app.py from /frontend for JSON5
```
  $ python app.py
```

## Database

The database is stored in a .csv file in **`database/`**
Trying to run directly on Windows can cause issues with detecting this file from recommend.py
If you face issues, please manually change to the direct path for windows in recommend.py

### Database Preprocessing

The script for preprocessing the dataset is available in **`database/`** as dataset_preprocessing.py

## Flask API

You can use the test endpoint to test connection

* `http://localhost:5000/api/test`
(returns a test json response)

### PyDoc

The PyDoc files can be read from app.html and recommend.html in **`/pydoc`** folder

### References
https://flask.palletsprojects.com/en/2.2.x/api/
https://github.com/pemagrg1/flask-for-beginners
https://docs.docker.com/compose/gettingstarted/

