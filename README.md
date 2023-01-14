# Recipe Recommendation System
This recipe recommendation system is built using Python, ReactJS and Flask API. It allows users to search for recipes based on their dietary preferences and needs. It also provides nutritional information for each recipe, allowing users to make informed decisions about their meals. The system is easy to use and provides a great way for users to discover new recipes and explore different cuisines.

### Built With

* [Python 3](https://www.python.org/)
* [React](https://reactjs.org/)
* [Flask](http://flask.pocoo.org/)
* [Docker](https://www.docker.com/)

### Dataset used from
- [Food.com Recipes and Interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions)

## Prerequisites
- [Install Docker and Docker Compose](https://docs.docker.com/compose/install/)

## Run
*   From the **`/food-recommendation`** directory run
```
$ docker compose up
```
*   Go to 
http://localhost:3000/

### Backend

Flask for the backend API (default port: 5000)  
For more information see the `README.md` file in the backend directory.

### Frontend

React for the frontend App (default port: 3000)  
For more information see the `README.md` file in the frontend directory.
If the chow command takes too long when building the container, it can be removed, but it may cause problems.




## License
This project is licensed under the GNU General Public License - see the `LICENSE` file for details
