import React from 'react';
import ReactDOM from 'react-dom';

class MyForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      description: 'The content of a textarea goes in the value attribute'
    };
  }
  render() {
    return (
      <form>
      <textarea value={this.state.description} />
      </form>
    );
  }
}

ReactDOM.render(<MyForm />, document.getElementById('root'));