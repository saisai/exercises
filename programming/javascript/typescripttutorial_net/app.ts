let message: string = 'Hello, World';
console.log(message);

let heading = document.createElement('h1')
heading.textContent = message

// add the heading the document
document.body.appendChild(heading)
