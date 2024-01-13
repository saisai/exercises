import * as React from 'react';
import Container from '@mui/material/Container';

export default function Search() {
    return (

        <Container component="main">
        <form  id="search-form" role="search">
            <input
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
            ></div>
        </form>
        </Container>
    );

}         
    