import React from 'react';   
import ReactDOM from 'react-dom';   
  
function NameList(props) {  
  const myLists = props.myLists;  
  const listItems = myLists.map((myList) =>  
    <li>{myList}</li>  
  );  
  return (  
    <div>  
        <h2>Rendering Lists inside component</h2>  
              <ul>{listItems}</ul>  
    </div>  
  );  
}  
const myLists = ['Peter', 'Sachin', 'Kevin', 'Dhoni', 'Alisa'];   
ReactDOM.render(  
  <NameList myLists={myLists} />,  
  document.getElementById('root')  
);  
