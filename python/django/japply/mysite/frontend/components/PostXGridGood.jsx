import React, { useEffect, useState} from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import { DataGrid } from '@mui/x-data-grid';

import axios from 'axios';

const columns = [
  
  { 
    field: 'title', 
    headerName: 'Title',
    flex: 1,
    renderCell: (params) =>    
      <Link href={params.row.link} target="_blank" rel="noreferrer">{params.row.title}</Link>
  },
 
];


const PostXGrid = () => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([])

  var config = {
    headers: {'Access-Control-Allow-Origin': '*',
              "Content-type": "application/json"
    }
  };

  useEffect(() => {
    const fetchData = async () =>{
      setLoading(true);
      try {
        const {data: response} = await axios.get('/api/thjobsdb/', config);        
        setData(response);
        
      } catch (error) {
        console.error(error.message);
      }
      setLoading(false);
    }
    

    fetchData();
    
    
  }, []);

  const rows = data.jobsdb;

  return (
    <div>
    {loading && <div>Loading</div>}
    {!loading && (
      <div style={{ height: 500, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={50}
        rowsPerPageOptions={[5]}
        checkboxSelection
      />
      </div>
    )}
    </div>
  )
}

export default PostXGrid;