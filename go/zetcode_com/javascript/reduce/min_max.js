let vals = [1, 2, 3, 4, 5];

const [initial] = vals;

console.log(initial);

const min = vals.reduce((total, next) => Math.min(total, next), initial);
const max = vals.reduce((total, next) => Math.max(total, next), initial);

console.log(`The minimum is: ${min}`);
console.log(`The maximum is: ${max}`);

