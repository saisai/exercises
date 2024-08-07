import * as React from 'react';
import {  createTheme, ThemeProvider } from '@mui/material/styles';
import { blue } from '@mui/material/colors';
import { Box, Stack } from '@mui/system';
import { Typography } from '@mui/material';

const theme = createTheme({
  palette: {
    primary: {
      light: blue[300],
      main: blue[500],
      dark: blue[700],
      darker: blue[900],
    },
  },
});

export default function AddingColorTokens() {
  return (
    <ThemeProvider theme={theme}>
      <Stack direction="row" gap={1}>
        <Stack alignItems="center">
          <Typography variant="body2">light</Typography>
          <Box sx={{ bgcolor: `primary.light`, width: 40, height: 20 }} />
        </Stack>
        <Stack alignItems="center">
          <Typography variant="body2">main</Typography>
          <Box sx={{ bgcolor: `primary.main`, width: 40, height: 20 }} />
        </Stack>
        <Stack alignItems="center">
          <Typography variant="body2">dark</Typography>
          <Box sx={{ bgcolor: `primary.dark`, width: 40, height: 20 }} />
        </Stack>
        <Stack alignItems="center">
          <Typography variant="body2">darker</Typography>
          <Box sx={{ bgcolor: `primary.darker`, width: 40, height: 20 }} />
        </Stack>
      </Stack>
    </ThemeProvider>
  );
}
