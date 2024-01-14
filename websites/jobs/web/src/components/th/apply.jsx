import * as React from 'react';
import Container from '@mui/material/Container';

import axios from 'axios';
import { useLoaderData } from "react-router-dom";
import { URL, ShowDataGrid, ShowApply } from './utils';
  
export default function Apply() {

    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])

    React.useEffect(() => {
        const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await axios.get(`${URL}apply`);
            setData(response);
        } catch (error) {
            console.error(error.message);
        }
        setLoading(false);
        }

        fetchData();
    }, []);


    // get data from searching query
    const { contacts } = useLoaderData() || {};   
    
    return (
        
        <>
        <Container component="main">
            <div> 
                        
                { contacts && contacts.data ? (
                    <ShowApply data={contacts.data} />
                    ) : (            
                        <ShowApply data={data}  />
                    )
                }
            </div>
        </Container>
        </>    
    );
}
