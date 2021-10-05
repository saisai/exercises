import React, { Component } from 'react';  
import { render } from 'react-dom';  
import ReactDOM from 'react-dom';     
function CustomInput(props) {  
  let callRefInput = React.createRef();  
   
  function handleClick() {  
    callRefInput.current.focus();  
  }  
   
  return (  
    <div>  
      <h2>Adding Ref to Class Component</h2>  
      <input  
        type="text"  
        ref={callRefInput} />  
      <input  
        type="button"  
        value="Focus input"  
        onClick={handleClick}  
      />  
    </div>  
  );  
}  
class App extends React.Component {  
  constructor(props) {  
    super(props);  
    this.callRefInput = React.createRef();  
  }  
   
  focusRefInput() {  
    this.callRefInput.current.focus();  
  }  
   
  render() {  
    return (  
      <CustomInput ref={this.callRefInput} />  
    );  
  }  
}  
ReactDOM.render(<App/>, document.getElementById('root'));  