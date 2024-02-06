import * as React from 'react';
import Container from '@mui/material/Container';


import axios from 'axios';
import { useLoaderData } from "react-router-dom";

import { URL, ShowDataGrid } from './utils';
import Search from './Search';


export default function ThJobsDb({ contacts }) {
    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])

    React.useEffect(() => {
        const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await axios.get(`${URL}jobsdb`);
            setData(response);
        } catch (error) {
            console.error(error.message);
        }
        setLoading(false);
        }

        fetchData();
        
    }, []);


    // get data from searching query 
    const { contactssearch } = useLoaderData() || {};  

    return (
        <>
        <Search />
        <Container component="main">
            <div>                         
                { contacts && contacts.data.length ? (
                    <ShowDataGrid data={contacts.data} />
                    ) : (            
                        <ShowDataGrid data={data}  />
                    )
                }
            </div>
        </Container>
        </>     
    );
}
