import React from "react";
import Box from '@mui/material';

import Sidebar from "./components/Sidebar";
import Feed from "./components/Feed";
import Navbar from './components/Navbar';


function App() {

    return(
        <Box>
            <Navbar />
            <Sidebar />
            <Feed />
        </Box>
    );

}

export default App;