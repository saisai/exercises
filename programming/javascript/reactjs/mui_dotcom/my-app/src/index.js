import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
//import App from './App';
import SignUp from './data/material/getting-started/templates/checkout/Checkout';
//import SignUp from './data/material/getting-started/templates/sign-up/SignUp';
//import SignIn from './data/material/getting-started/templates/sign-in/SignIn';
//import Dashboard from './data/material/getting-started/templates/dashboard/Dashboard';
//import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
  <SignUp />
  {/* <App /> */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();
