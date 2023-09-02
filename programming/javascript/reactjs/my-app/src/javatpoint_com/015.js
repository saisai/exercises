import React from 'react';   
import ReactDOM from 'react-dom';   
function MenuBlog(props) {  
  const titlebar = (  
    <ol>  
      {props.data.map((show) =>  
        <li key={show.id}>  
          {show.title}  
        </li>  
      )}  
    </ol>  
  );  
  const content = props.data.map((show) =>  
    <div key={show.id}>  
      <h3>{show.title}: {show.content}</h3>      
    </div>  
  );  
  return (  
    <div>  
      {titlebar}  
      <hr />  
      {content}  
    </div>  
  );  
}  
const data = [  
  {id: 1, title: 'First', content: 'Welcome to JavaTpoint!!'},  
  {id: 2, title: 'Second', content: 'It is the best ReactJS Tutorial!!'},  
  {id: 3, title: 'Third', content: 'Here, you can learn all the ReactJS topics!!'}  
];  
ReactDOM.render(  
  <MenuBlog data={data} />,  
  document.getElementById('root')  
);  