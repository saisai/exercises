
let scores = [80, 90, 70];

for(let score of scores) {
    score = score + 5;
    console.log(score);

}

for (const score of scores) {
    console.log(score);
}

let colors = ['Red', 'Green', 'Blue'];

for (const [index, color] of colors.entries()) {
    console.log(`${color} is at index ${index}`);
}

const ratings = [
    {user: 'John',score: 3},
    {user: 'Jane',score: 4},
    {user: 'David',score: 5},
    {user: 'Peter',score: 2},
];

let sum = 0;
for (const {score} of ratings) {
    sum += score;
}

console.log(`Total scores: ${sum}`); // 14

let str = "abc";
for(let c of str) {
    console.log(c);
}

let colorss = new Map();

colorss.set('red', '#ff0000');
colorss.set('green', '#00ff00');
colorss.set('blue', '#0000ff');

for (let color of colorss) {
    console.log(color);
}

let nums = new Set([1, 2, 3]);

for (let num of nums) {
    console.log(num);
}