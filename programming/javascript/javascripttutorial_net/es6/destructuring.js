function getScores() {
    return [70, 80, 90, 100];
 }
 let [x, y ,...args] = getScores();
console.log(x); // 70
console.log(y); // 80
console.log(args); // [90, 100] 
console.log(args[0]); // [90, 100] 