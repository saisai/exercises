import * as React from 'react';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

import {
    DataGrid,
    GridToolbarContainer,
    GridToolbarFilterButton,
  } from '@mui/x-data-grid';
import axios from 'axios';
import { Link, useLocation, useParams } from "react-router-dom";

import Search from './Search';
import { URL as MyURL,
    ShowDataGrid,
} from './utils';


function NoRowsOverlay() {
    return (
      <Stack height="100%" alignItems="center" justifyContent="center">
        No rows in DataGrid
        <pre>(rows=&#123;[]&#125;)</pre>
      </Stack>
    );
  }

  const columns = [
    { field: 'id', headerName: 'ID' },
    { field: 'title',
       headerName: 'Title', 
       width: 650,      
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


export default function JobThai({ contacts }) {
    // const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])
    const [search, setSearch] = React.useState(false);

    const location = useLocation();
    const query = new URLSearchParams(location.search).get("q");
    console.log("location.search.length " + location.search.length);
    if(location.search.length > 2) {
      
        React.useEffect(() => {
            const fetchData = async () =>{
            // setLoading(true);
            console.log("set searach " + search);
            setSearch(search);
            try {
                let uu = `${MyURL}jobthaisearach/?keyword=${query}`;
                console.log("uur " + uu);
                const {data: response} = await axios.get(uu);
                setData(response);
                console.log('search result ' + response.length);
            } catch (error) {
                console.error(error.message);
            }
            // setLoading(false);
            }    
            // fetchData();    
            setTimeout(() => {
                fetchData();            
            }, 1000);            
        }, [!search]);
        
    } 
    else{
        console.log("no search");        
        React.useEffect(() => {
            const fetchData2 = async () =>{
            // setLoading(true);
            console.log("set searach 2" + search);
            setSearch(search);               
            try {
                let uu = `${MyURL}jobthai`;
                console.log("no search uu " + uu);
                const {data: response} = await axios.get(uu);

                setData(response);
                console.log(response);
            } catch (error) {
                console.error(error.message);
            }
            // setLoading(false);
            }
            setTimeout(() => {
                fetchData2();            
            }, 1000);
        }, [search]);      
    }


    return (
        <>
        <Search />
        <Container component="main">
            <div>                
            search {'' + search }
            {
                    
                data.length ?  (
                    <ShowDataGrid data={data}  />        
                ) : (
                    <div style={{ height: 400, width: '100%' }}>
                        <DataGrid               
                            columns={columns}                  
                            rows={data}           
                            components={{ NoRowsOverlay }}                           
                        />
                    </div>
                )
            }                    
            </div>
        </Container>
        </>     
    );
}
