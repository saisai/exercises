import React from "react";
import ReactDOM from "react-dom/client";
//import App from "./App";

import { Box } from '@mui/material';

import Sidebar from "./components/Sidebar";
import Feed from "./components/Feed";
import Navbar from './components/Navbar';


function App() {

    return(
        <div>
        <Box>
            <Navbar />
            <Sidebar />
            <Feed />
        </Box>
        </div>
    );

}

const root = ReactDOM.createRoot(document.getElementById("react-app"));
root.render(
  <React.StrictMode>
      <App />
  </React.StrictMode>
);