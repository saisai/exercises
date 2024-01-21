import * as React from 'react';
import Container from '@mui/material/Container';
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";

export default function Search() {
    return (
        
        <Container component="main" >
            <Box
            display="flex"
            justifyContent="center"
            alignItems="center" 
            >
            <form  id="search-form" role="search">
                <TextField
                        id="search-bar"
                        className="text"                
                        label="Enter the position to be searched..."
                        variant="outlined"
                        placeholder="Search..."
                        size="small"
                        name="q"     
                        style = {{ width: "500px"}}           
                    />
                    <IconButton type="submit" aria-label="search">
                        <SearchIcon style={{ fill: "blue" }} />
                    </IconButton>
                
                
                {/* <input
                id="q"
                aria-label="Search contacts"
                placeholder="Search"
                type="search"
                name="q"
                />
                <div
                id="search-spinner"
                aria-hidden
                hidden={true}
                />
                <div
                className="sr-only"
                aria-live="polite"
                ></div> */}
            </form>
            </Box>
            </Container>
          
    );

}         
    