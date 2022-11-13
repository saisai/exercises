import React from 'react';
import ReactDOM from "react-dom/client";
import Sidebar from "./components/Sidebar";
import Feed from "./components/Feed";
//import Rightbar from "./components/Rightbar";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Box, Stack } from "@mui/material";
import Navbar from "./components/Navbar";
//import Add from "./components/Add";
import { useState } from "react";

function App() {
  const [mode, setMode] = useState("light");

  const darkTheme = createTheme({
    palette: {
      mode: mode,
    },
  });
  return (
    <ThemeProvider theme={darkTheme}>
      <Box bgcolor={"background.default"} color={"text.primary"}>
        <Navbar />
        <Stack direction="row" spacing={2} justifyContent="space-between">
        <Sidebar setMode={setMode} mode={mode}/>
          <Feed />          
        </Stack>
        
      </Box>
    </ThemeProvider>
  );
}
const root = ReactDOM.createRoot(document.getElementById("react-app"));
root.render(
  <React.StrictMode>
      <App />
  </React.StrictMode>
);