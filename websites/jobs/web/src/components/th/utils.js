import * as React from "react";
import { DataGrid } from '@mui/x-data-grid';
import { Button, Stack } from "@mui/material";

import axios from "axios";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import ApplyService from "../../services/apply.service";

export function getUrl(params) {
    return (
        <a target='_blank'  rel="noreferrer"  href={params.row.link}>{params.row.title}</a>
    );    
  }

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
      console.log(response);
      console.log(response.status);
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
      </>
  );
}


export function ShowApply({data}) {
  const navigate = useNavigate();

  const [clickedRow, setClickedRow] = React.useState();
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
      console.log(response);
      console.log(response.status);
    }, (error) => {
      console.log(error);
    });    
  };  

  const onDeleteClick = (e, row) => {
    e.stopPropagation();
    console.log(JSON.stringify(row));
    ApplyService.delete(row.id)
      .then(response => {
        console.log(response.data);
        window.location.reload();
        //navigate("/apply");
        

        //this.props.router.navigate('/tutorials');
      })
      .catch(e => {
        console.log(e);
      });
  };  
  

  const onEditClick = (e, row) => {
    e.stopPropagation();
    alert(JSON.stringify(row));
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
     width: 100 },    
    {
      field: "applyButton",
      headerName: "Actions",
      description: "Actions column.",
      sortable: false,
      width: 300,      
      renderCell: (params) => {
        return (
          <>
          <Stack direction="row" spacing={2}>
          <Button
            onClick={(e) => onButtonClick(e, params.row)}
            variant="contained"
          >
            Apply
          </Button>
          <Button
            onClick={(e) => onEditClick(e, params.row)}
            variant="contained"
            color="warning"
          >
            Edit
          </Button>
          
          <Button
            onClick={(e) => onDeleteClick(e, params.row)}
            variant="contained"
            color="error"
          >
            Delete
          </Button>
          </Stack>
          </>
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
      </>
  );
}
