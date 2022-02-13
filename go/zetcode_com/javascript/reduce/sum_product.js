let vals = [1, 2, 3, 4, 5];

let sum = vals.reduce((total, next) => {return total + next});
let product = vals.reduce((total, next) => {return total * next});

console.log(`The sum is: ${sum}`);
console.log(`The product is: ${product}`);

