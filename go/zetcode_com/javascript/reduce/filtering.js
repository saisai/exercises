let vals = [-1, -2, 3, 4, -5, -6];

let filtered =vals.reduce((total, next) => {
  if (next > 0) {
    total.push(next * 2);
  }

  return total;

}, []);

console.log(filtered);

