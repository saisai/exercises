import * as React from 'react';
import Container from '@mui/material/Container';

import { DataGrid } from '@mui/x-data-grid';
import { Button, Stack } from "@mui/material";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Modal from '@mui/material/Modal';

import { getUrl } from './utils';


import axios from "axios";
import { useLocation, 
  useNavigate, useParams, Link,
  redirect,
  NavLink,
 } from "react-router-dom";


import { useLoaderData } from "react-router-dom";
import { URL, ShowDataGrid, ShowApply } from './utils';

const style = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 400,
    bgcolor: "background.paper",
    border: "2px solid #000",
    boxShadow: 24,
    p: 4
  };
  
  function BasicModal({ onOpen, onClose, open, row }) {
    return (
      <div>
        <Modal
          open={open}
          onClose={onClose}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >
          <Box sx={style}>
            <Typography id="modal-modal-title" variant="h6" component="h2">
              {row.col1}
            </Typography>
            <Typography id="modal-modal-description" sx={{ mt: 2 }}>
              {row.col2}
            </Typography>
          </Box>
        </Modal>
      </div>
    );
  }
  
  const OpenModalButton = ({ row }) => {
    console.log(JSON.stringify(row));
    const [open, setOpen] = React.useState(false);
  
    const handleOpen = () => {
      setOpen(true);
    };
  
    const handleClose = () => {
      setOpen(false);
    };
    return (
      <>
        <Button onClick={handleOpen}>Test</Button>
        <BasicModal
          open={open}
          onOpen={handleOpen}
          onClose={handleClose}
          row={row}
        />
      </>
    );
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
    renderCell: OpenModalButton        
},    
];

const data = [
    {
        "id": 308,
        "title": "Full Stack Developer – Django, React.js",
        "link": "https://th.jobsdb.com/th/en/job/full-stack-developer-django-react.js-300003002989172?token=0~dca8a0a0-62c5-4329-bd92-b1e18a541534&sectionRank=2&jobId=jobsdb-th-job-300003002989172",
        "time": "2d ago",
        "email": null,
        "description": null,
        "createdAt": "2024-01-14T14:36:11.298+00:00",
        "updatedAt": null
    },
    {
        "id": 309,
        "title": "Technical Lead Python Developer – Huge Project 2024 – Near BTS line",
        "link": "https://th.jobsdb.com/th/en/job/technical-lead-python-developer-huge-project-2024-near-bts-line-300003002990549?token=0~dca8a0a0-62c5-4329-bd92-b1e18a541534&sectionRank=3&jobId=jobsdb-th-job-300003002990549",
        "time": "1d ago",
        "email": null,
        "description": null,
        "createdAt": "2024-01-14T14:36:12.045+00:00",
        "updatedAt": null
    },
]
export default function ApplyTest() {

    //const [loading, setLoading] = React.useState(true);
    // const [data, setData] = React.useState([])

    // React.useEffect(() => {
    //     const fetchData = async () =>{
    //     //setLoading(true);
    //     try {
    //         const {data: response} = await axios.get(`${URL}apply`);
    //         setData(response);
    //         console.log(response)
    //     } catch (error) {
    //         console.error(error.message);
    //     }
    //     //setLoading(false);
    //     }

    //     fetchData();
    // }, []);


    // get data from searching query
    //const { contacts } = useLoaderData() || {};   
    
    return (        
        <Container component="main" sx={{ zIndex: 1300}}>
            <DataGrid
              rows={data}
              columns={columns}           
              sx={{ zIndex: 1300}}                   
              initialState={{
              ...data.initialState,
              pagination: { paginationModel: { pageSize: 25 } },
              }}
              pageSizeOptions={[25, 50, 75, 100]}
              />     
        </Container>        
    );
}

