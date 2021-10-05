import React, { Component } from 'react';  
import ReactDOM from 'react-dom';  
class App extends React.Component {  
   constructor() {  
      super();  
      this.findDomNodeHandler1 = this.findDomNodeHandler1.bind(this);  
      this.findDomNodeHandler2 = this.findDomNodeHandler2.bind(this);  
   };  
   findDomNodeHandler1() {  
       var myDivOne = document.getElementById('myDivOne');  
       ReactDOM.findDOMNode(myDivOne).style.color = 'red';  
   }  
   findDomNodeHandler2() {  
       var myDivTwo = document.getElementById('myDivTwo');  
       ReactDOM.findDOMNode(myDivTwo).style.color = 'blue';  
   }  
   render() {  
      return (  
         <div>  
             <h1>ReactJS Find DOM Node Example</h1>  
             <button onClick = {this.findDomNodeHandler1}>FIND_DOM_NODE1</button>  
             <button onClick = {this.findDomNodeHandler2}>FIND_DOM_NODE2</button>  
             <h3 id = "myDivOne">JTP-NODE1</h3>  
             <h3 id = "myDivTwo">JTP-NODE2</h3>  
         </div>  
      );  
   }  
}  
//export default App;  

ReactDOM.render(<App/>, document.getElementById('root'));  