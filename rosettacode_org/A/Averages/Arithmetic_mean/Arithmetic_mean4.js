
Array.prototype.mean = function() {
  return !this.length ? 0
    : this.reduce(function(pre, cur, i) {
        return (pre * i + cur) / (i + 1);
    });
}
console.log([1,2,3,4, 5].mean());
console.log([].mean());
