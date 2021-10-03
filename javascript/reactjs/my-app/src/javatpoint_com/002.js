import React, { Component } from 'react';  
import ReactDOM from 'react-dom';
class App extends React.Component {  
 constructor() {  
      super();        
      this.state = { displayBio: false };  
      console.log('Component this', this);  
      this.toggleDisplayBio = this.toggleDisplayBio.bind(this);  
      }  
      toggleDisplayBio(){  
          this.setState({displayBio: !this.state.displayBio});  
          }  
      render() {  
          return (  
              <div>  
                  <h1>Welcome to JavaTpoint!!</h1>  
                  {  
                      this.state.displayBio ? (   
                          <div>  
                              <p><h4>Javatpoint is one of the best Java training institute in Noida, Delhi, Gurugram, Ghaziabad and Faridabad. We have a team of experienced Java developers and trainers from multinational companies to teach our campus students.</h4></p>  
                              <button onClick={this.toggleDisplayBio}> Show Less </button>  
                        </div>  
                          ) : (  
                              <div>  
                                  <button onClick={this.toggleDisplayBio}> Read More </button>  
                              </div>  
                          )  
                  }  
             </div>  
        )  
    }  
}  
ReactDOM.render(<App />, document.getElementById('root'));
//export default App;  