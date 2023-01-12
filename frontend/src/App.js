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





import React, { useState } from 'react';

// main app function
function App() {
    const [displayData, SetdisplayData] = useState()

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
              SetdisplayData (responseData)       // displaying receieved JSON data
            })
          )
        


        // for testing only
        // SetdisplayData (sendData) 
      }



    return (
        <React.Fragment>
          <form style={{paddingLeft: '20px'}} onSubmit={e => handleSubmit(e)}>

          <p>Select Food Type</p> 
            <select name="type">
              <option value="Healthy">Healthy</option>
              <option value="Veg">Veg</option>
              <option value="Non-Veg">Non-Veg</option>
              <option value="Veg_Dessert">Veg Dessert</option>
              <option value="Non-Veg_Dessert">Non-Veg Dessert</option>
            </select>

            <p>How much time do you have ?</p>
            <input name='mins' type="number" placeholder='Number in Minutes' />

            <p>How many steps ?</p>
            <input name='steps' type="number" placeholder='Number' />

            <p>How many ingredients ?</p>
            <input name='ingredients' type="number" placeholder='Number' />

            <br></br><br></br>
            <button>Submit</button>
            <br></br><br></br>

            <pre>{JSON.stringify(displayData, null, 2)}</pre>

          </form>
          
        </React.Fragment>
      )
    }

export default App;
