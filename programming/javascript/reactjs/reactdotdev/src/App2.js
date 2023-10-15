import { useState } from 'react';

function MyButton() {
    const [count, setCount] = useState(0);

    function handleClick() {
        console.log('You clicked me!');
        setCount(count + 1);
      }

    return(
        <button onClick={handleClick}>
            Clicked {count} times
        </button>
    );
}
export default function App2() {

    return(
        <div>
            <h1>Welcome to my app</h1>
            <MyButton />
            <MyButton />
        </div>
    );

}