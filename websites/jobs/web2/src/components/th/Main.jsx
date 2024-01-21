import * as React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';

import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import GlobalStyles from '@mui/material/GlobalStyles';


import axios from 'axios';
import { Link as RLink, Outlet  } from "react-router-dom";
import { useLoaderData } from "react-router-dom";


import { URL as MyURL,
 } from './utils';

 import Footer from './Footer';
import Search from './Search';
import ThJobsDb from './ThJobsDb';


export async function loader({ request }) {
    const url = new URL(request.url);
    const q = url.searchParams.get("q");
    let contacts = {};
    if(request.url.indexOf("jobthai") > -1)
    {
        let uu = `${MyURL}jobthaisearach/?keyword=${q}`;
        contacts = await axios.get(uu);        
    } else if(request.url.indexOf("jobsdb") > -1) {
        let uu = `${MyURL}jobsdbsearch/?keyword=${q}`;
        contacts = await axios.get(uu);        
    } else if(request.url.indexOf("?q") > -1) {
        let uu = `${MyURL}jobsdbsearch/?keyword=${q}`;
        contacts = await axios.get(uu);       
        console.log(JSON.stringify(contacts)) ;
    }       

    return { contacts };
}

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default function Main() {

    // get data from searching query
    const { contacts } = useLoaderData() || {};   
    //console.log("asdf");
    //console.log(JSON.stringify(contacts));
    
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
                            component={RLink}
                            to="/applytest"
                        >
                            Apply Test
                        </Link>  
                        <Link
                            variant='button'
                            color="text.primary"
                            href="#"
                            sx={{ my: 1, mx: 1.5 }}
                            component={RLink}
                            to="/apply"
                        >
                            Apply
                        </Link>  
                    
                        <Link
                            variant='button'
                            color="text.primary"
                            href="#"
                            sx={{ my: 1, mx: 1.5 }}
                            component={RLink}
                            to="/jobthai"
                        >
                            JobThai
                        </Link>                
                        <Link
                            variant='button'
                            color="text.primary"
                            href="#"
                            sx={{ my: 1, mx: 1.5 }}
                            component={RLink}
                            to="/jobsdb"
                        >
                            JobsDb
                        </Link>

                    </nav>
                    <Button href="/login" variant="outlined" sx={{ my: 1, mx: 1.5 }}>
                        Login
                    </Button>
                </Toolbar>
            </AppBar>

            <Search />
            
            {/* Hero unit */}
            <div sx={{ zIndex: 1300}}>
                {contacts && contacts.data ? (
                    <ThJobsDb contacts={ contacts } />
                ) :
                 (
                    <Outlet />
                 )}              
                
            </div>
            {/* End hero unit */}


            {/* Footer */}
            <Footer />            
            {/* End footer */}

        </ThemeProvider>
    );
}