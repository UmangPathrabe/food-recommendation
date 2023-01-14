import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';


/**
 * Renders the main app page
 * on button press, gets user input and sends POST request with input data in JSON
 * recieves POST response with JSON data and renders it 
 * 
 * 
 * @module JSON5      used for parsing steps data
 *  
 * @return  {HTML}    Renders main page
 */
function App() {

    /**
     * calling async function at submit event
     * 
     * @async   Used so that we can use await in fetch to wait for response
     */
    const handleSubmit = async(event) => {
        event.preventDefault();           // prevents reset of entered data
        const formData = event.target;    //storing data from form elements

        // making JSON of form data
        const jsonData = {
          type: formData['type'].value, 
          mins: formData['mins'].value, 
          step: formData['steps'].value, 
          ingr: formData['ingredients'].value};
          
        const sendData = jsonData;          //  JSON object for sending data


        /**
         * using fetch to send JSON to api by POST method and wait for reponse
         * then rendering the recieved JSON reponse
         * 
         * @constant {JSON} showData  stores data to be diplayed
         */
        await fetch("/api/rec", {method: "POST", headers: {'Content-Type' : 'application/json'}, body: JSON.stringify(sendData)})
          .then((response) => response.json()     // storing entire api response
            .then((responseData) => {             // storing JSON object from api respone

              const showData = responseData;

              // for (no recipe found) error response
              if (showData.error === 1) {
                const Display = <p>No results found, please change filters</p>
                ReactDOM.render(Display,document.querySelector('#root'));
              } 


              var temp;     // used as temp storage

              /**
              * getting string of ingredients and making a JSON array
              * replacing single quotes with double for parse()
              * normal parse() is used since ingredients data has no random single quotes
              * @constant {array} ingr     stores ingredients
              */
              temp = showData.ingredients[0].replace(/'/g, '"');
              const ingr = JSON.parse(temp);


              /**
              * using JSON5 to make JSON array from string without having issues with single quotes
              * @module JSON5       better parse()
              * @constant {array} step     stores steps
              */
              const JSON5 = require('json5');
              const step = JSON5.parse(showData.steps[0]);
              // old parse() without JSON5 (causes a lot more issues with single quotes)
              // temp = showData.steps[0].replace(/'/g, '"');
              // const step = JSON.parse(temp);


              /**
              * getting string of nutrition data and making a JSON array of numbers
              * removing '[' and ']' for easy split into array
              * @constant {array} nutrition    stores nutrition data
              */
              temp = showData.nutrition[0].replace('[', ' ');
              temp = temp.replace(']', '');
              temp = temp.split(',');
              const nutrition = temp;

              // Displaying recommendation output
              const Display = <React.Fragment>

                                <h1>{showData.name[0].toUpperCase()}</h1>

                                <p>{showData.description[0].charAt(0).toUpperCase() + showData.description[0].slice(1)}</p>

                                <p><b>Time to make - </b>{showData.minutes[0]} minutes</p>

                                <div class="grid-container">
                                <div>
                                <h4>Ingredients -</h4>
                                <ul className='ingr_list'>
                                  {ingr.map(item => {return <li>{item}</li>;})}
                                </ul>
                                </div>

                                <div>
                                <h4>Steps -</h4>
                                <ol>
                                  {step.map(item => {return <li>{item}</li>;})}
                                </ol>
                                </div>
                                </div>

                                <br></br>
                                <h4>Nutritional Information -</h4>
                                <p>This recipe has {nutrition[0]} Calories</p>
                                <ul className='nutri'>
                                  <li>Total Fat = {parseInt(nutrition[1])} % DV</li>
                                  <li>Sugar = {parseInt(nutrition[2])} % DV</li>
                                  <li>Sodium = {parseInt(nutrition[3])} % DV</li>
                                  <li>Protein = {parseInt(nutrition[4])} % DV</li>
                                  <li>Saturated Fat = {parseInt(nutrition[5])} % DV</li>
                                  <li>Carbohydrates = {parseInt(nutrition[6])} % DV</li>
                                  <span><i>* % DV stands for Percent Daily Value</i></span>
                                </ul>

                              </React.Fragment>;

              ReactDOM.render(Display,document.querySelector('#root'));     // renders recipe data

            })
          )
      }


    // default return of App() which renders main page
    return (
        <React.Fragment>

          <h2>Recipe Recommendation System</h2>
          
          <form onSubmit={e => handleSubmit(e)}>
            <b>

          <p>Select the Type of Food you want to have:</p> 
            <select name="type">
              <option value="Healthy">Healthy</option>
              <option value="Veg">Veg</option>
              <option value="Non-Veg">Non-Veg</option>
              <option value="Veg_Dessert">Veg Dessert</option>
              <option value="Non-Veg_Dessert">Non-Veg Dessert</option>
            </select>

            <p>How much time do you have for preparation ?</p>
            <input name='mins' type="number" placeholder='Number in Minutes' />

            <p>How many steps in the process do you prefer ?</p>
            <input name='steps' type="number" placeholder='Number' />

            <p>How many ingredients are available with you ?</p>
            <input name='ingredients' type="number" placeholder='Number' />

            <br></br><br></br>
            <button><b>Recommend</b></button>
            <br></br><br></br>

            </b>
          </form>

        </React.Fragment>
      )
    }

export default App;
