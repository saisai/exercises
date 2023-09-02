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


import axios from 'axios';


axios.create({
  baseURL: "http://localhost:9999/api/",
  headers: {
    "Content-type": "application/json"
  }
});


const Post2 = () => {
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
  
  return (
    <div>
    {loading && <div>Loading</div>}
    {!loading && (
    <Box sx={{ width: '100%' }}>
      
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Title</TableCell>
            
            
            
            
          </TableRow>
        </TableHead>
        <TableBody>
          {data.jobsdb.map((row) => (
            <TableRow
              key={row.pk}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                <Link href={row.link} target="_blank" rel="noreferrer">{row.title}</Link>
                
                
              </TableCell>
                            
          
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>


    </Box>
    )}
    </div>
  )
}

export default Post2;