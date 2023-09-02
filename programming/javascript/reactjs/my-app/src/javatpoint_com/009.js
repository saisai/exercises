import React, { Component } from 'react';  
import ReactDOM from 'react-dom';  
class App extends React.Component {  
    constructor(props) {  
        super(props);  
        this.state = {  
            personGoing: true,  
            numberOfPersons: 5  
        };  
        this.handleInputChange = this.handleInputChange.bind(this);  
   }  
   handleInputChange(event) {  
       const target = event.target;  
       const value = target.type === 'checkbox' ? target.checked : target.value;  
       const name = target.name;  
       this.setState({  
           [name]: value  
       });  
  }  
  render() {  
      return (  
          <form>  
              <h1>Multiple Input Controlled Form Example</h1>  
              <label>  
                  Is Person going:  
                  <input  
                    name="personGoing"  
                    type="checkbox"  
                    checked={this.state.personGoing}  
                    onChange={this.handleInputChange} />  
             </label>  
             <br />  
             <label>  
                 Number of persons:  
                 <input  
                 name="numberOfPersons"  
                 type="number"  
                 value={this.state.numberOfPersons}  
                 onChange={this.handleInputChange} />  
             </label>  
         </form>  
     );  
  }  
}  
ReactDOM.render(<App/>, document.getElementById('root'));  