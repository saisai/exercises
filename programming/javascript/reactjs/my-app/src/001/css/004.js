import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';

class MyHeader extends React.Component {
  render() {
    return (
      <div>
      <h1>Hello Style!</h1>
      <p>Add a little style!.</p>
      </div>
    );
  }
}

ReactDOM.render(<MyHeader />, document.getElementById('root'));

/*
Notice that you now have three files in your project:
'index.js', 'index.html', and 'App.css'.
*/
