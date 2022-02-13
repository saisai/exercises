const axios = require('axios');

axios.get('http://google.com').then(resp => {
  console.log(resp.data);
});
