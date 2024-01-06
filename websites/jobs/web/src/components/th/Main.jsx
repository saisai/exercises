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

import { Routes, Route, Link as RLink } from "react-router-dom";

import JobThai from './JobThai';
import ThJobsDb from './ThJobsDb'; 
import Copyright from './Copyright';

const footers = [
    {
      title: 'Company',
      description: ['Team', 'History', 'Contact us', 'Locations'],
    },
    {
      title: 'Features',
      description: [
        'Cool stuff',
        'Random feature',
        'Team feature',
        'Developer stuff',
        'Another one',
      ],
    },
    {
      title: 'Resources',
      description: ['Resource', 'Resource name', 'Another resource', 'Final resource'],
    },
    {
      title: 'Legal',
      description: ['Privacy policy', 'Terms of use'],
    },
  ];

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
                    </nav>
                    <Button href="#" variant="outlined" sx={{ my: 1, mx: 1.5 }}>
                        Login
                    </Button>
                </Toolbar>
            </AppBar>

            {/* Hero unit */}
            <Routes>
                <Route path="/" >
                    <Route index  element={<ThJobsDb />} />
                    <Route path="/jobthai" element={<JobThai />} />
                    <Route path="/jobsdb" element={<ThJobsDb />} />
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