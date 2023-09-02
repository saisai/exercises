import React from 'react';
import ReactDOM from 'react-dom';
import './mysass.scss';

class MyHeader extends React.Component {
  render() {
    return (
      <div>
      <h1>Hello Style test!</h1>
      <p>Add a little style!.</p>
      </div>
    );
   
}
}

ReactDOM.render(<MyHeader />, document.getElementById('root'));