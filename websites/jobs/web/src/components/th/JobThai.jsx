import * as React from 'react';
import Container from '@mui/material/Container';
import { DataGrid } from '@mui/x-data-grid';

import axios from 'axios';
import { columns, URL } from './utils';
  
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

    return (
        <>
        <Container component="main">
            <div>
                {loading && <div>Loading</div>}
                <DataGrid
                rows={data}
                columns={columns}                
                initialState={{
                ...data.initialState,
                pagination: { paginationModel: { pageSize: 25 } },
                }}
                pageSizeOptions={[25, 50, 75, 100]}
                />      
            </div>
        </Container>
        </>    
    );
}
