import { useRouteError, Outlet } from "react-router-dom";
import * as React from 'react';
import Container from '@mui/material/Container';

export default function ErrorPage() {
  const error = useRouteError();
  // console.error(error);

  return (
    <div>
    <Container component="main">
      <h1>Oops!</h1>
      <p>Sorry, an unexpected error has occurred.</p>
      {/* <p>
        <i>{error.statusText || error.message}</i>
      </p> */}
    </Container>
    <Outlet />
    </div>
  );
}