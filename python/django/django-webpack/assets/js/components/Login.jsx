import React from 'react';

import { 
        Button, CssBaseline, TextField, FormControlLabel, Checkbox, Link ,
        Grid,
        Box,
        Typography,
        Container,
        InputAdornment,
        } from "@mui/material";

import { Lock, Mail } from '@mui/icons-material'
import { ThemeProvider } from '@mui/material/styles';
import { createTheme } from '@mui/material/styles';
import { makeStyles } from '@mui/styles';
//import Logo from './Assets/logo-sample.svg'

const theme = createTheme({
  palette:{
    primary:{main: '#F5B62A'},
    secondary:{main:'#383938'},
  }
});

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(4),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: '30px',
    backgroundColor: 'white',
    borderradius: '4px',
    boxShadow: '0px 1px 5px 0px rgba(0,0,0,0.2), 0px 2px 2px 0px rgba(0,0,0,0.14), 0px 3px 1px -2px rgba(0,0,0,0.12)',
  },
  inputF:{

  },
  avatar: {
    // margin: theme.spacing(2),
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    // marginTop: theme.spacing(1),
  },
  submit: {
    // margin: theme.spacing(3, 0, 2),
  },
  signup: {
    // margin: theme.spacing(-2, 0, 2),
  },
}));

export default function SignIn() {
  const classes = useStyles();

  return (
    <ThemeProvider theme={theme}>
    <Container component="main" maxWidth="sm">
      <CssBaseline />
      <div className={classes.paper}>
      <Grid 
            container
            direction="row"
            justify="center"
            alignItems="center"
      >   
        <Grid item xs={9}>
            <img maxWidth="300" alt="Logo" className={classes.avatar} />
        </Grid>
      </Grid>
        
        <Typography component="div">
          <Box fontSize={30} fontWeight={600} m={-2}>
              SIGN IN
          </Box>
        </Typography>
        <Typography component="div">
          <Box fontSize={16} m={1} paddingT>
            Sign into your account
          </Box>
        </Typography>
        <form className={classes.form} noValidate>
          <Grid 
              container
              direction="row"
              justify="center"
              alignItems="center"
          >
            <Grid item xs={9}>
              <TextField
                className={classes.inputF}
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                autoFocus
                InputProps={{
                  startAdornment: <InputAdornment position="start"><Mail color="disabled"/></InputAdornment>,
                }}
              />
            </Grid>

            <Grid item xs={9}>
              <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              InputProps={{
                startAdornment: <InputAdornment position="start"><Lock color="disabled" /></InputAdornment>,
              }}
              />
            </Grid>

            <Grid item xs={9}>
              <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
              />
            </Grid>
              
            <Grid item xs={9} >
              <Button
              type="submit"
              fullWidth
              variant="contained"
              color="secondary"
              className={classes.submit}
              m={0}
              >
                Sign In
              </Button>
            </Grid>

            <Grid item>
              <Link href="#" variant="body2" color="secondary" >
                Forgot your password?
              </Link>
            </Grid>

            <Grid item xs={9}>  
              <Typography component="div">
                <Box fontSize={20} m={3} paddingT>
                  <Link href="#" color="secondary" >
                        YOU DO NOT HAVE AN ACCOUNT?
                  </Link>
                </Box>
              </Typography>
            </Grid>

            <Grid item xs={9}>
              <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.signup}
              m={-1}
              >
              SIGN UP
              </Button>
            </Grid>

          </Grid>

          
        </form>
      </div>
    </Container>
    </ThemeProvider>
  );
}