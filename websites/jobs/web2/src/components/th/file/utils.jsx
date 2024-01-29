import * as React from 'react';
import Container from '@mui/material/Container';

import Modal from '@mui/material/Modal';
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Stack } from '@mui/material';

import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import { styled } from '@mui/material/styles';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

import { useLoaderData,
    Form,
} from "react-router-dom";


import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import positionService from '../../../services/position.service';
import fileService from '../../../services/file.service';

import "./style.css"
import { EditPositionModal } from './edit';

const VisuallyHiddenInput = styled('input')({
    clip: 'rect(0 0 0 0)',
    clipPath: 'inset(50%)',
    height: 1,
    overflow: 'hidden',
    position: 'absolute',
    bottom: 0,
    left: 0,
    whiteSpace: 'nowrap',
    width: 1,
  });


export function ShowFile({data}) {

    const onDeleteClick = (e, row) => {
      e.stopPropagation();
      fileService.delete(row.id)
        .then(response => {
          console.log(response.data);
          window.location.reload();

        })
        .catch(e => {
          console.log(e);
        });
    };          
  
    const columns = [
      { field: 'id', headerName: 'ID' },
      { field: 'tutorial_id', headerName: 'ID' },
      { field: 'title',
         headerName: 'Title', 
         width: 650,
         renderCell: getUrl,
      },    

       {
        field: "editButton",
        headerName: "",
        description: "Actions column.",
        sortable: false,
        width: 100,      
        renderCell: OpenModalButton
       },
      {
        field: "applyButton",
        headerName: "Actions",
        description: "Actions column.",
        sortable: false,
        width: 200,      
        renderCell: (params) => {        
          return (
            <>
            <Stack direction="row" spacing={2}>             
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
            disableSelectIconOnClick     
            initialState={{
            ...data.initialState,
            pagination: { paginationModel: { pageSize: 25 } },
            }}
            pageSizeOptions={[25, 50, 75, 100]}
            />     
      </>
    );
  }


  export function AddPositionModal({ onOpen, onClose, open }) {
    const [desc, setDesc] = React.useState();   
    const [alert, setAlert] = React.useState(false);
    const [dataAlert, setDataAlert] = React.useState();
    const [position, setPosition] = React.useState();
    const [positionID, setPositionID] = React.useState('');
    const [fileUploaded, setFileUploaded] = React.useState();

    React.useEffect(() => {
        const fetchData = async () =>{
            try {
                const {data: response} = await positionService.getAll();
                setPosition(response);
            } catch (error) {
                console.error(error.message);
            }
        }
        fetchData();
    }, []);

    const handleFileChange = (e) => {
      if (e.target.files) {
        console.log("file");
        setFileUploaded(e.target.files[0]);
      }
    };

    const handleChange = (event) => {
        setPositionID(event.target.value);
    };

    const handleClose = () => {
      setAlert(false);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);

        console.log({
            title: data.get('title'),
            id : positionID         
        });
        console.log(fileUploaded);
        data.append("id", positionID);
        data.append("file", fileUploaded);
        fileService.create(data )
        .then(response => {
          console.log(response.data);
          if(response.data.message) {
            setAlert(true);
            setDataAlert({title: data.get('title')});
          }
          else {
            window.location.reload();
          }          

        })
        .catch(e => {
          console.log(e);
        });  
      };

    return (
      <div>
        <Modal
          open={open}     
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >        
          <Box sx={style}  noValidate>   
            <Typography component="h5" variant="h6">
              {"Add File for position" }
            </Typography>
            <Box  sx={{ mt: 1 }}>
            <Form method="post" onSubmit={handleSubmit}>  
            <TextField
                margin="normal"
                required
                fullWidth
                id="title"
                label="Title"
                name="title"
                autoComplete="title"
                autoFocus                
              />                 
              <Box sx={{ minWidth: 120 }}>
                <FormControl fullWidth>
                    <InputLabel id="demo-simple-select-label">Position</InputLabel>
                    <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={positionID}
                    label="Position"
                    onChange={handleChange}
                    >
                    <MenuItem value="">-----------------</MenuItem>
                    {position && 
                        position.map((item) => (
                            <MenuItem key={item.id} value={item.id}>{item.title}</MenuItem>
                        ))
                    }
                    </Select>
                </FormControl>
                </Box>
                <Button component="label" variant="contained" startIcon={<CloudUploadIcon />} onChange={handleFileChange} >
                  Upload file
                  <VisuallyHiddenInput type="file" />
              </Button>
              <CKEditor
                    name="desc"
                    editor={ ClassicEditor } 
                    onReady={ editor => {
                        // You can store the "editor" and use when it is needed.
                        console.log( 'Editor is ready to use!', editor );
                        setDesc(editor.getData());
                    } }
                    onChange={ ( event, editor ) => {
                        console.log( event );
                        console.log(editor.getData());
                        setDesc(editor.getData());                 
                    } }
                    onBlur={ ( event, editor ) => {
                        console.log( 'Blur.', editor );
                    } }
                    onFocus={ ( event, editor ) => {
                        console.log( 'Focus.', editor );
                    } }
                />
                
              <Grid container spacing={2}>
                <Grid item xs>                
                  <Button                      
                    onClick={(e) => onClose(false)}                  
                    variant="contained"
                    fullWidth
                    sx={{ mt: 3, mb: 2 }}
                  >
                    Cancel
                  </Button>
                  
                </Grid>              
                <Grid item xs>
                  <Button
                    type="submit"                  
                    variant="contained"
                    fullWidth
                    sx={{ mt: 3, mb: 2 }}
                  >
                    Save
                  </Button>
                </Grid>
              </Grid>
              </Form>
            </Box>
          </Box>
          
        </Modal>
        {alert ? <AlertDialogPosition open={alert} handleClose={handleClose} data={dataAlert}></AlertDialogPosition> : <></> }
      </div>
    );
  }


  export const style = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 800,
    height: 600,
    bgcolor: "background.paper",
    border: "1px solid #000",
    boxShadow: 24,
    p: 4
  };

  export function getUrl(params) {
    return (
        <a target='_blank'  rel="noreferrer"  href={params.row.link}>{params.row.title}</a>
    );    
  };


  const OpenModalButton = ({ row }) => {
    const [open, setOpen] = React.useState(false);
  
    const handleOpen = () => {
      setOpen(true);
    };
  
    const handleClose = () => {
      setOpen(false);
    };
    return (
      <>
        <Button 
          variant="contained"
          color="warning" 
          onClick={handleOpen}
        >Edit</Button>
        <EditPositionModal
          open={open}
          onOpen={handleOpen}
          onClose={handleClose}
          row={row}
        />
      </>
    );
  };