
Array.prototype.timeoutSort = function(f) {
  this.forEach(function(n){
    setTimeout(function() { f(n)}, 5 * n)
  });
}

[1, 9, 8, 7, 6, 5, 3, 4, 5, 2, 0].timeoutSort(function(n) {
  console.log(n + '\n');
})