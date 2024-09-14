import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import MyApp, { Profile,
  ShoppingList,
  MyApp2,
 } from './components/learn/mybutton.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* <App /> */}
    <MyApp />
    <Profile />
    <ShoppingList />
    <MyApp2 />
  </React.StrictMode>,
)
