import * as React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardHeader from '@mui/material/CardHeader';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import StarIcon from '@mui/icons-material/StarBorder';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import GlobalStyles from '@mui/material/GlobalStyles';
import Container from '@mui/material/Container';
import { DataGrid } from '@mui/x-data-grid';

import axios from 'axios';
import Copyright from './Copyright';

function getUrl(params) {
    console.log(params.row.title);
    return (
        <a target='_blank' href={params.row.link}>{params.row.title}</a>
    );
    
  }
  
const columns = [
    { field: 'id', headerName: 'ID' },
    { field: 'title', headerName: 'Title', width: 300,
        renderCell: getUrl,
    },
    { field: 'time', headerName: 'Time', width: 600 }
  ]

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

export default function ThJobsDb() {

    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])

    React.useEffect(() => {
        const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await axios.get('http://127.0.0.1:8888/jobsdb');
            setData(response);
        } catch (error) {
            console.error(error.message);
        }
        setLoading(false);
        }

        fetchData();
    }, []);

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
                            JobsDb
                        </Link>
                    </nav>
                    <Button href="#" variant="outlined" sx={{ my: 1, mx: 1.5 }}>
                        Login
                    </Button>
                </Toolbar>
            </AppBar>

            {/* Hero unit */}
            <Container disableGutters maxWidth="sm" component="main">
                <div>
                    {loading && <div>Loading</div>}
                    <DataGrid
                        rows={data}
                        columns={columns}
                        pageSize={12}
                    />

                </div>
            </Container>
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