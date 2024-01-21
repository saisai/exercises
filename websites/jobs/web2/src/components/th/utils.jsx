import * as React from "react";
import { DataGrid } from '@mui/x-data-grid';
import { Button, Stack } from "@mui/material";


import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';

import axios from "axios";
import { useLocation, 
  useNavigate, useParams, Link,
  redirect,
  NavLink,
 } from "react-router-dom";
import AlertDialog from "./alert";


export function getUrl(params) {
    return (
        <a target='_blank'  rel="noreferrer"  href={params.row.link}>{params.row.title}</a>
    );    
  };

export const URL = "http://127.0.0.1:8888/";

export const footers = [
    {
      title: 'Company',
      description: ['Team', 'History', 'Contact us', 'Locations'],
    },
    {
      title: 'Features',
      description: [
        'Cool stuff',
        'Random feature',
        'Team feature',
        'Developer stuff',
        'Another one',
      ],
    },
    {
      title: 'Resources',
      description: ['Resource', 'Resource name', 'Another resource', 'Final resource'],
    },
    {
      title: 'Legal',
      description: ['Privacy policy', 'Terms of use'],
    },
  ];

export function ShowDataGrid({data}) {
  const [clickedRow, setClickedRow] = React.useState();
  const [open, setOpen] = React.useState(false);


  const handleClose = () => {
    setOpen(false);
  };

  const onButtonClick = (e, row) => {
    e.stopPropagation();
    setClickedRow(row);
    console.log(JSON.stringify(row));  
    
    axios({
      method: 'post',
      url: `${URL}apply`,
      data: {
        title: row.title,
        link: row.link,
        time: row.time,
      }
    })
    .then((response) => {
      // console.log(response);
      // console.log(response.status);
      // alert(JSON.stringify(response));
      if(response.data.message) {
        setOpen(true);
      }
    }, (error) => {
      console.log(error);
    });    
  };  

  const columns = [
    { field: 'id', headerName: 'ID' },
    { field: 'title',
       headerName: 'Title', 
       width: 650,
       renderCell: getUrl,
    },
    { field: 'time',
     headerName: 'Time',
     width: 150 },    
    {
      field: "deleteButton",
      headerName: "Actions",
      description: "Actions column.",
      sortable: false,
      width: 160,
      renderCell: (params) => {
        return (
          <Button
            onClick={(e) => onButtonClick(e, params.row)}
            variant="contained"
          >
            Add
          </Button>
        );
      }
    },
  ];

  // clickedRow: {clickedRow ? `${clickedRow.firstName}` : null}

  return (
      <>
        <DataGrid
            rows={data}
            columns={columns}                
            initialState={{
            ...data.initialState,
            pagination: { paginationModel: { pageSize: 25 } },
            }}
            pageSizeOptions={[25, 50, 75, 100]}
            />     

        {/* added alert */}
        {open ? <AlertDialog open={open} handleClose={handleClose} data={clickedRow}></AlertDialog>
        : <></> }
        {/* added alert end */}
      </>
  );
}

