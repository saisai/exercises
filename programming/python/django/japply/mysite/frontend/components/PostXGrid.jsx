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
import DeleteIcon from '@mui/icons-material/Delete';
import SecurityIcon from '@mui/icons-material/Security';
import FileCopyIcon from '@mui/icons-material/FileCopy';
import Toolbar  from '@mui/material/Toolbar';
import NewButton from '@mui/icons-material/Newspaper'
import Button from '@mui/material/Button';
import { DataGrid, GridToolbarContainer, useGridApiContext, GridActionsCellItem } from '@mui/x-data-grid';
//import { useDemoData } from '@mui/x-data-grid-generator';

import axios from 'axios';

// https://codesandbox.io/s/cpcl8?file=/src/Components/Toolbar/Buttons/DeleteButton.tsx

const PostXGrid = () => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([])

  var config = {
    headers: {'Access-Control-Allow-Origin': '*',
              "Content-type": "application/json"
    }
  };

  const NewToolbar = () => {
    return (
      <Toolbar
        buttons={[
          <Button variant="contained">Contained</Button>
        ]}
      />
    );
  };

  const CustomToolbar = () => {
    const apiRef = useGridApiContext();
  
    const handleGoToPage1 = () => apiRef.current.setPage(1);
  
    return (
      <GridToolbarContainer>
        <Button onClick={handleGoToPage1}>Go to page 1</Button>
      </GridToolbarContainer>
    );
  };

  const columns = React.useMemo(
    () => [
      { 
        field: 'title', 
        headerName: 'Title',
        flex: 1,
        renderCell: (params) =>    
          <Link href={params.row.link} target="_blank" rel="noreferrer">{params.row.title}</Link>
      },      
      {
        field: 'actions',
        type: 'actions',
        width: 80,
        getActions: (params) => [
          <GridActionsCellItem
            icon={<DeleteIcon />}
            label="Delete"
            onClick={deleteUser(params.id)}
          />,
          <GridActionsCellItem
            icon={<SecurityIcon />}
            label="Toggle Admin"
            onClick={toggleAdmin(params.id)}
            showInMenu
          />,
          <GridActionsCellItem
            icon={<FileCopyIcon />}
            label="Duplicate User"
            onClick={duplicateUser(params.id)}
            showInMenu
          />,
        ],
      },
    ],
    [deleteUser, toggleAdmin, duplicateUser],
  );


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

  const deleteUser = React.useCallback(
    (id) => () => {
      console.log('delete ' + id);
      //setTimeout(() => {
      //  setRows((prevRows) => prevRows.filter((row) => row.id !== id));
      //});
    },
    [],
  );

  const toggleAdmin = React.useCallback(
    (id) => () => {
      setRows((prevRows) =>
        prevRows.map((row) =>
          row.id === id ? { ...row, isAdmin: !row.isAdmin } : row,
        ),
      );
    },
    [],
  );

  const duplicateUser = React.useCallback(
    (id) => () => {
      setRows((prevRows) => {
        const rowToDuplicate = prevRows.find((row) => row.id === id);
        return [...prevRows, { ...rowToDuplicate, id: Date.now() }];
      });
    },
    [],
  );

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
        components={{
          Toolbar: CustomToolbar,
        }}        
      />
      </div>
    )}
    </div>
  )
}

export default PostXGrid;