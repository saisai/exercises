import * as React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import GlobalStyles from '@mui/material/GlobalStyles';
import Container from '@mui/material/Container';

import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import TextField from "@mui/material/TextField";

import { Routes, Route, Link as RLink, Outlet } from "react-router-dom";
import { useNavigate, useSearchParams } from "react-router-dom";
import axios from 'axios';
import JobThai from './JobThai';
import ThJobsDb from './ThJobsDb'; 
import Copyright from './Copyright';

import { footers, URL } from './utils';


function SearchForm() {
    const [searchParams, setSearchParams] = useSearchParams();
    const navigate = useNavigate();
    const [searchQuery, setSearchQuery] = React.useState(searchParams.get("keyword") || "");

    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])
  
    const handleSubmit = (event) => {
      event.preventDefault();
      setSearchParams({ q: searchQuery });
      //navigate(`${URL}/jobthai?keyword=${encodeURIComponent(searchQuery)}`);
      // axios.get(`${URL}/jobthai?keyword=${encodeURIComponent(searchQuery)}`)

      const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await axios.get(`${URL}jobthai?keyword=${encodeURIComponent(searchQuery)}`);
            setData(response);
            console.log(data);
        } catch (error) {
            console.error(error.message);
        }
        setLoading(false);
        }

        fetchData();


    };
  
    return (
        <div>
            <div style={{ display: "flex" }}>
                <form onSubmit={handleSubmit}>
                    <input
                    type="text"
                    placeholder="Search..."
                    value={searchQuery}
                    onChange={(event) => setSearchQuery(event.target.value)}
                    />
                    <button type="submit">Search</button>
                </form>      
            </div>
        

        {data && (
            <div
            style={{
                padding: "24px",
                margin: "24px 0",
                borderTop: "1px solid #eaeaea",
                display: "flex",
                alignItems: "center",
                gap: "16px",
            }}
            >
            <div>
                <h2>{data.lengthme}</h2>
                <p>{data.length}</p>
            </div>
            </div>
        )}
        </div>

    );
  }

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default function Main() {
    
    return (
        <ThemeProvider theme={defaultTheme}>
            <GlobalStyles styles={{ ul : { margin: 0, padding: 0, listStyle: 'none'} }} />
            <CssBaseline />
            <AppBar
                position='static'
                color="default"
                elevation={0}
                sx={{ borderBottom: (theme) => `1px solid ${theme.palette.divider}`}}
                >
                <Toolbar sx={{ flexWrap: 'wrap'}}>
                    <Typography variant="h6" color="inherit" noWrap sx={{ flexGrow: 1 }}>
                        Company name
                    </Typography>                    
                    <nav>
                   
                            <Link
                                variant='button'
                                color="text.primary"
                                href="#"
                                sx={{ my: 1, mx: 1.5 }}
                            >
                                <RLink to="/jobthai">JobThai</RLink>
                            </Link>
             
                        <Link
                            variant='button'
                            color="text.primary"
                            href="#"
                            sx={{ my: 1, mx: 1.5 }}
                        >
                            <RLink to="/jobsdb">JobsDb</RLink>                            
                        </Link>

                        <Outlet />
                    </nav>
                    <Button href="#" variant="outlined" sx={{ my: 1, mx: 1.5 }}>
                        Login
                    </Button>
                </Toolbar>
            </AppBar>
            <Container>
            <div
            style={{
                display: "flex",
                alignSelf: "center",
                justifyContent: "center",
                flexDirection: "column",
                padding: 20
            }}
            >
                <SearchForm />
            </div>
            </Container>
            
            

            {/* Hero unit */}
            <Routes>
                <Route path="/" >
                    <Route index  element={<ThJobsDb />} />
                    <Route path="/jobthai" element={<JobThai />} />
                    <Route path="/jobsdb" element={<ThJobsDb />} />
                    <Route path="/jobthai/?q" element={<SearchForm />} />
                </Route>
            </Routes>

            {/* End hero unit */}


            {/* Footer */}
            <Container
                maxWidth="md"
                component="footer"
                sx={{
                borderTop: (theme) => `1px solid ${theme.palette.divider}`,
                mt: 8,
                py: [3, 6],
                }}
            >
                <Grid container spacing={4} justifyContent="space-evenly">
                {footers.map((footer) => (
                    <Grid item xs={6} sm={3} key={footer.title}>
                    <Typography variant="h6" color="text.primary" gutterBottom>
                        {footer.title}
                    </Typography>
                    <ul>
                        {footer.description.map((item) => (
                        <li key={item}>
                            <Link href="#" variant="subtitle1" color="text.secondary">
                            {item}
                            </Link>
                        </li>
                        ))}
                    </ul>
                    </Grid>
                ))}
                </Grid>
                <Copyright sx={{ mt: 5 }} />
            </Container>
            {/* End footer */}

        </ThemeProvider>
    );
}