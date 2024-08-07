import * as React from 'react';
import Container from '@mui/material/Container';

import axios from 'axios';
import { useLoaderData } from "react-router-dom";
import { URL, ShowDataGrid } from './utils';
  
export default function JobThai() {

    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])

    React.useEffect(() => {
        const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await axios.get(`${URL}jobthai`);
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
