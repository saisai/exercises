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

import { getUrl, style } from '../utils';
import Search from '../Search';
import { AddPositionModal, ShowFile } from './utils';
import fileService from '../../../services/file.service';



export default function File() {
    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])
    React.useEffect(() => {
        const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await fileService.getAll();
            setData(response);
        } catch (error) {
            console.error(error.message);
        }
        setLoading(false);
        }

        fetchData();
    }, []);
    console.log("file " + JSON.stringify(data));
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
                <ShowFile data={contacts.data} />
                ) : (            
                    <ShowFile data={data}  />
                )
            }
          </div>
        </Container>
        </>    
    );
}