

import * as React from 'react';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';

export default function BoxSx() {
  return (

    <React.Fragment>
    <CssBaseline />
    <Container maxWidth="sm">
    <Box
      sx={{
        width: 800,
        height: 300,
        backgroundColor: 'primary.dark',
        '&:hover': {
          backgroundColor: 'primary.main',
          opacity: [0.9, 0.8, 0.7],
        },
      }}
    />
    </Container>
  </React.Fragment>

    
  );
}