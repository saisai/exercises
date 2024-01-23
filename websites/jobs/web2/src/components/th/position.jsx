import * as React from 'react';
import Container from '@mui/material/Container';

import Modal from '@mui/material/Modal';
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Stack } from '@mui/material';


import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

import { useLoaderData,
    Form,
} from "react-router-dom";

import { getUrl, style } from './utils';
import Search from './Search';
import PositionService from '../../services/position.service';
import AlertDialogPosition from './alert-position';

import "./style.css";
  
export default function Position() {
    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])
    React.useEffect(() => {
        const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await PositionService.getAll();
            setData(response);
        } catch (error) {
            console.error(error.message);
        }
        setLoading(false);
        }

        fetchData();
    }, []);

    const [open, setOpen] = React.useState(false);    
  
    const handleOpen = () => {
      setOpen(true);
    };
  
    const handleClose = () => {
      setOpen(false);
    };

    // get data from searching query
    const { contacts } = useLoaderData() || {};       
    return (        
        <>
        <Button variant="contained" onClick={handleOpen}>Add</Button>
        <AddPositionModal
          open={open}
          onOpen={handleOpen}
          onClose={handleClose}         
        />
        <Search />
        <Container component="main">
          <div>                         
            { contacts && contacts.data ? (
                <ShowPosition data={contacts.data} />
                ) : (            
                    <ShowPosition data={data}  />
                )
            }
          </div>
        </Container>
        </>    
    );
}


  
function AddPositionModal({ onOpen, onClose, open }) {

    const [desc, setDesc] = React.useState();   
    const [alert, setAlert] = React.useState(false);
    const [dataAlert, setDataAlert] = React.useState();

    const handleClose = () => {
      setAlert(false);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);

        console.log({
          email: data.get('email')          
        });

        data.append('description', desc );
        PositionService.create(data )
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
              {"Add Position" }
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
  
  export function ShowPosition({data}) {

    const onDeleteClick = (e, row) => {
      e.stopPropagation();
      PositionService.delete(row.id)
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
 
function EditPositionModal({ onOpen, onClose, open, row }) {
    const [title, setTitle] = React.useState(row.title);
    const [desc, setDesc] = React.useState();   
    const [alert, setAlert] = React.useState(false);
    const [dataAlert, setDataAlert] = React.useState();

    const handleClose = () => {
      setAlert(false);
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
              {"Edit Position" }
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
