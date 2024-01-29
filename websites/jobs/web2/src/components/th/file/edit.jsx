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


import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

import { useLoaderData,
    Form,
} from "react-router-dom";


import "./style.css";
import { style } from './utils';

export function EditPositionModal({ onOpen, onClose, open, row }) {
    console.log(JSON.stringify(row));
    const [title, setTitle] = React.useState(row.title);
    const [desc, setDesc] = React.useState();   
    const [alert, setAlert] = React.useState(false);
    const [dataAlert, setDataAlert] = React.useState();


    const [position, setPosition] = React.useState();
    const [positionID, setPositionID] = React.useState('');
    const [fileUploaded, setFileUploaded] = React.useState();

    const handleClose = () => {
      setAlert(false);
    };

    const handleFileChange = (e) => {
        if (e.target.files) {
          console.log("file");
          setFileUploaded(e.target.files[0]);
        }
      };
  
      const handleChange = (event) => {
          setPositionID(event.target.value);
      };

    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);

        console.log({
          title: data.get('title') ,
          row_id: row.id         
        });

        data.append('description', desc );
        PositionService.update(row.id,data )
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
              {"Edit Position File uploading..." }
            </Typography>
            <Box  sx={{ mt: 1 }}>
            <Form method="post" onSubmit={handleSubmit}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="edit-title"
                label="Title"
                name="title"
                autoComplete="title"
                autoFocus            
                value={title} 
                onChange={(event) => {
                  setTitle(event.target.value);
                }}   
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
              <CKEditor
                    name="desc"
                    data={row.description}
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
                    onClick={(e) => {setTitle(row.title); onClose(false)}}
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