# Frontend

This project is a frontend web app built with ReactJS for recipe recommendation.
Main code is in App.js in **`/src`** folder


## Built With

* [React](https://reactjs.org/)
* [Docker](https://www.docker.com/)

## Prerequisites

You will need the following things properly installed on your computer:
* [node.js v18.13.0] (https://nodejs.org/en/)
* [JSON5](https://json5.org/) (required for better parse() function)


### For running directly on Windows

* Install node.js

* run in /frontend to get dependencies:
```
  $ npm install
```

* run in /frontend for JSON5
```
  $ npm install json5
```

### Running
From the /frontend directory run:
```
  $ npm start
```

## Proxy

Proxy needs to be defined in package.json for forwarding API calls to API's port (default 5000 for flask)

for windows development:
`"proxy": "http://127.0.0.1:5000",`

for docker:
`"proxy": "http://host.docker.internal:5000",`

### JSDoc

The JSDoc files can be read from App.js.html in **`/jsdoc`** folder

### References
https://reactjs.org/docs/create-a-new-react-app.html  
https://stackoverflow.com/questions/41402834/convert-string-array-to-array-in-javascript  
https://stackoverflow.com/questions/36038454/parsing-string-as-json-with-single-quotes  




## Extra information

This project was created with [Create React App](https://github.com/facebook/create-react-app).

### Create React App - Available Scripts:

In the project directory, you can run:

#### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

#### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

#### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.
