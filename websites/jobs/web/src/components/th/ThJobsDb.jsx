import * as React from 'react';
import Container from '@mui/material/Container';


import axios from 'axios';
import { useLoaderData } from "react-router-dom";

import { URL, ShowDataGrid } from './utils';


export default function ThJobsDb({ contacts }) {
    const [loading, setLoading] = React.useState(true);
    const [data, setData] = React.useState([])

    React.useEffect(() => {
        const fetchData = async () =>{
        setLoading(true);
        try {
            const {data: response} = await axios.get(`${URL}jobsdb`);
            setData(response);
        } catch (error) {
            console.error(error.message);
        }
        setLoading(false);
        }

        fetchData();
        
    }, []);

    

    // get data from searching query 
    const { contactssearch } = useLoaderData() || {};   
    console.log("THJOB");
    console.log(JSON.stringify(contacts));    

    return (
        <>
        { contacts && contacts.data.length ? (
            <Container component="main">
                <ShowDataGrid data={contacts.data}  />
            </Container>
        ) : 
            (

                <Container component="main">
                    <div>         

                        { contactssearch && contactssearch.data.length ? (
                            <ShowDataGrid data={contactssearch.data} />
                            ) : (            
                                <ShowDataGrid data={data} />
                            )
                        }
                    </div>
                </Container>

            )
        }
        </>

        // <>
        // <Container component="main">
        //     <div>         

        //         { contacts && contacts.data.length ? (
        //             <ShowDataGrid data={contacts.data} columns={columns} />
        //             ) : (            
        //                 <ShowDataGrid data={data} columns={columns} />
        //             )
        //         }
        //     </div>
        // </Container>
        // </>        
    );
}


