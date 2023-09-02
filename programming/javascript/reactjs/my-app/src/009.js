import React from 'react';
import ReactDOM from 'react-dom';

function shoot() {
  alert('Great Shot');
}

const element = (
  <button onClick={shoot}>Take the short!</button>
);

ReactDOM.render(element, document.getElementById('root'));

