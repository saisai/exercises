import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Game from './Game';
import Game2 from './Game2';
import reportWebVitals from './reportWebVitals';
import Game3 from './Game3';
import Game4 from './Game4';
import Game5 from './Game5';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    {/* <App /> 
    <Game />
    
    <Game2 />
    
    <Game3 />
    
    <Game4 />
    */}
    <Game5 />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
