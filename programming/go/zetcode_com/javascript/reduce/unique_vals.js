let vals = [1, 1, 2, 2, 3, 4, 5, 5];

let unique_vals = vals.reduce((total, next) => {
  if(total.includes(next)){
    return total;
  } else {
    return [...total, next];
  }

}, []);

console.log(unique_vals);

