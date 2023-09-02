import React from 'react';   
import ReactDOM from 'react-dom';   
  
const myList = ['Peter', 'Sachin', 'Kevin', 'Dhoni', 'Alisa'];   
const listItems = myList.map((myList)=>{   
    return <li>{myList}</li>;   
});   
ReactDOM.render(   
    <ul> {listItems} </ul>,   
    document.getElementById('root')   
);   
