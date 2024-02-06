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

import axios from 'axios';
import { useLoaderData,
    Form,
} from "react-router-dom";

import { URL, getUrl, style } from './utils';
import ApplyService from "../../services/apply.service";

import "./style.css";
import Search from './Search';
  
export default function Apply() {
    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])

    React.useEffect(() => {
        const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await axios.get(`${URL}apply`);
            setData(response);
        } catch (error) {
            console.error(error.message);
        }
        // console.log(data);
        setLoading(false);
        }

        fetchData();
    }, []);

    // get data from searching query
    const { contacts } = useLoaderData() || {};       
    return (        
        <>
        <Search />
        <Container component="main">
            <div>                         
                { contacts && contacts.data ? (
                    <ShowApply data={contacts.data} />
                    ) : (            
                        <ShowApply data={data}  />
                    )
                }
            </div>
        </Container>
        </>    
    );
}

function BasicModal({ onOpen, onClose, open, row }) {

    const [desc, setDesc] = React.useState();   

    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);

        console.log({
          email: data.get('email')          
        });

        data.append('description', desc );
        ApplyService.update(row.id, data )
        .then(response => {
          console.log(response.data);
          window.location.reload();

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
              { row.title }
            </Typography>
            <Box  sx={{ mt: 1 }}>
            <Form method="post" onSubmit={handleSubmit}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                autoFocus
                value={row.email}
              />        
              <CKEditor
                    name="desc"
                    editor={ ClassicEditor }                    
                    data={row.description}
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
        <BasicModal
          open={open}
          onOpen={handleOpen}
          onClose={handleClose}
          row={row}
        />
      </>
    );
  };
  
  export function ShowApply({data}) {
    const [clickedRow, setClickedRow] = React.useState();
    const [layout, setLayout] = React.useState(undefined);
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

        })
        .catch(e => {
          console.log(e);
        });
    };  
    
  
    const columns = [
      { field: 'id', headerName: 'ID' },
      { field: 'title',
         headerName: 'Title', 
         width: 500,
         renderCell: getUrl,
      },
      { field: 'applyTimes',
       headerName: 'Apply Times',
       width: 100 },
      { field: 'time',
       headerName: 'Time',
       width: 100 },    
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
              onClick={(e) => onButtonClick(e, params.row)}
              variant="contained"
            >
              Apply
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
 