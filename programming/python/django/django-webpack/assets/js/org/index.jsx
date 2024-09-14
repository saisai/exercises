/*
import React from 'react';
import ReactDOM from 'react-dom';

import App from './app';

ReactDOM.render(<App/>, document.getElementById('react-app'));

*/
/*
import React from 'react';
import ReactDOM from 'react-dom/client';

function Hello(props) {
  return <h1>Hello World!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById("react-app"));
root.render(<Hello />);
*/

import React from 'react';
import ReactDOM from 'react-dom/client';

import App from './app';

const root = ReactDOM.createRoot(document.getElementById("react-app"));
root.render(<App />);