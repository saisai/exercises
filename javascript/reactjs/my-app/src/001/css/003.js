import React from 'react';
import ReactDOM from 'react-dom';


const mystyle2 = {
      color: "white",
      backgroundColor: "DodgerBlue",
      padding: "100px",
      fontFamily: "Arial"
    };

class MyHeader extends React.Component {
  render() {
    const mystyle = {
      color: "white",
      backgroundColor: "DodgerBlue",
      padding: "10px",
      fontFamily: "Arial"
    };
    return (
      <div>
      <h1 style={mystyle2}>Hello Style!</h1>
      <p>Add a little style!</p>
      </div>
    );
  }
}

ReactDOM.render(<MyHeader />, document.getElementById('root'));