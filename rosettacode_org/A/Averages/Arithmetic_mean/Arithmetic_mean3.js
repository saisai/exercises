function mean(array) {
  return !array.length ? 0
  : array.reduce(function(pre, cur, i) {
      return (pre * i + cur) / ( i + 1);
  });
}
console.log(mean([1, 2, 3, 4, 5]));

