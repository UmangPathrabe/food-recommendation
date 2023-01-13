// import React, { Component } from 'react';
// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//         <header className="App-header">
//           <img src={logo} className="App-logo" alt="logo" />
//           <p>
//             Edit <code>src/App.js</code> and save to reload.
//           </p>
//           <a
//             className="App-link"
//             href="https://github.com/caseyr003/flask-react-template"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             View on Github
//           </a>
//         </header>
//       </div>
//   );
// }





import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';

// main app function
function App() {

    // calling async function at submit event
    const handleSubmit = async(event) => {
        event.preventDefault();           // prevents reset of entered data
        const formData = event.target;    //storing data from form elements
        
        // making JSON of form data
        const jsonData = {
          type: formData['type'].value, 
          mins: formData['mins'].value, 
          step: formData['steps'].value, 
          ingr: formData['ingredients'].value}
        // console.log('*****JSON is', jsonData);
          
        const sendData = jsonData
        // console.log('*****Send JSON is', jsonData);

        // useing fetch to send JSON data to api by POST method
        await fetch("/api/rec", {method: "POST", headers: {'Content-Type' : 'application/json'}, body: JSON.stringify(sendData)})
          .then((response) => response.json()     // storing entire api response
            .then((responseData) => {             // storing JSON data from api respone
              // console.log('*****API response is', response);
              // console.log('*****API response JSON data is', responseData);

              const showData = responseData
              var temp

              // getting string of ingredients and making a JSON array
              temp = showData.ingredients[0].replace(/'/g, '"');
              const ingr = JSON.parse(temp);

              // getting string of steps and making a JSON array
              temp = showData.steps[0].replace(/'/g, '"');
              const step = JSON.parse(temp);

              // getting string of nutrition data and making a JSON array
              temp = showData.nutrition[0].replace('[', ' ');
              temp = temp.replace(']', '');
              temp = temp.split(',');
              const nutrition = temp;

              // Displaying recommendation
              const Display = <React.Fragment>
                                <h1>{showData.name[0].toUpperCase()}</h1>

                                <p>{showData.description[0].charAt(0).toUpperCase() + showData.description[0].slice(1)}</p>

                                <p><b>Time to make - </b>{showData.minutes[0]} minutes</p>

                                <h4>Ingredients -</h4>
                                <ul className='ingr_list'>
                                  {ingr.map(item => {return <li>{item}</li>;})}
                                </ul>

                                <h4>Steps -</h4>
                                <ol>
                                  {step.map(item => {return <li>{item}</li>;})}
                                </ol>

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

              ReactDOM.render(Display,document.querySelector('#root'));

            })
          )
      }



    return (
        <React.Fragment>
          {/* <h2>Recipe Recommendation System</h2> */}
          <h2>RECIPE RECOMMENDATION SYSTEM</h2>
          <p>This system will recommend recipes to you according to you requirements</p> 
          <br></br>
          <form onSubmit={e => handleSubmit(e)}>

          <p>Select the Type of Food you want to have</p> 
            <select name="type">
              <option value="Healthy">Healthy</option>
              <option value="Veg">Veg</option>
              <option value="Non-Veg">Non-Veg</option>
              <option value="Veg_Dessert">Veg Dessert</option>
              <option value="Non-Veg_Dessert">Non-Veg Dessert</option>
            </select>

            <p>How much time do you have for preparation ?</p>
            <input name='mins' type="number" placeholder='Number in Minutes' />

            <p>How many step in the process do you prefer ?</p>
            <input name='steps' type="number" placeholder='Number' />

            <p>How many ingredients are available with you ?</p>
            <input name='ingredients' type="number" placeholder='Number' />

            <br></br><br></br>
            <button>Recommend</button>
            <br></br><br></br>

          </form>
          
        </React.Fragment>
      )
    }

export default App;
