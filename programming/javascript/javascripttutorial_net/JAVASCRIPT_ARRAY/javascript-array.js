let mountains = ['Everest', 'Fuji', 'Nanga Parbat'];
console.log(mountains[0]); // 'Everest'
console.log(mountains[1]); // 'Fuji'
console.log(mountains[2]); // 'Nanga Parbat'

let mountainss = ['Everest', 'Fuji', 'Nanga Parbat'];
mountainss[2] = 'K2';

console.log(mountainss);

let seas = ['Black Sea', 'Caribbean Sea', 'North Sea', 'Baltic Sea'];
seas.push('Red Sea');

console.log(seas);

seas.unshift('Red Sea');

console.log(seas);

const lastElement = seas.pop();
console.log(lastElement);

const firstElement = seas.shift();

console.log(firstElement);


let index = seas.indexOf('North Sea')
console.log(index)

console.log(Array.isArray(seas));

