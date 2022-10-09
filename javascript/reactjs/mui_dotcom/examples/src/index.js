import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import SignIn from './components/sign-in/SignIn';
import SignUp from './components/sign-up/SignUp';
import reportWebVitals from './reportWebVitals';
import SignInSide from './components/sign-in-side/SignInSide';
import StickyFooter from './components/sticky-footer/StickyFooter';
import Album from './components/album/Album';
import Main from './components/material-components/main';


const root = ReactDOM.createRoot(document.getElementById('root'));
{/* <SignIn /> 
  <SignUp />
  <SignInSide />
  <StickyFooter />
    <Album />
*/}
root.render(
  
  <Main />
  
  
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
