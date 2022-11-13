import React, { useEffect, useState} from 'react';
import axios from 'axios';


axios.create({
  baseURL: "http://localhost:9999/api/",
  headers: {
    "Content-type": "application/json"
  }
});

const Post2 = () => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([])

  var config = {
    headers: {'Access-Control-Allow-Origin': '*',
              "Content-type": "application/json"
    }
  };

  useEffect(() => {
    const fetchData = async () =>{
      setLoading(true);
      try {
        const {data: response} = await axios.get('/api/thjobsdb/', config);        
        setData(response);
        
      } catch (error) {
        console.error(error.message);
      }
      setLoading(false);
    }
    

    fetchData();
    
    
  }, []);
  console.log(JSON.stringify(data.jobsdb))
  return (
    <div>
    {loading && <div>Loading</div>}
    {!loading && (
      <div>
      
        <h2>Doing stuff with data</h2>
        {data.jobsdb.map( (row, index) => {
          
          return(
          row.title
          )

        } )}
        
      </div>
    )}
    </div>
  )
}

export default Post2;