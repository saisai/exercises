import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import SignIn from './components/sign-in/SignIn';
import SignUp from './components/sign-up/SignUp';
import reportWebVitals from './reportWebVitals';
import SignInSide from './components/sign-in-side/SignInSide';
import StickyFooter from './components/sticky-footer/StickyFooter';


const root = ReactDOM.createRoot(document.getElementById('root'));
{/* <SignIn /> 
  <SignUp />
  <SignInSide />
*/}
root.render(
  <StickyFooter />
  
  
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
