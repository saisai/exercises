
function fizz(d, e) {
  return function b(a) {
    return a ? b(a -1).concat(a) : [];
  }(e).reduce(function(b, a){
    return b + (d.reduce(function(b, c){
      return b + (a % c[0] ? "" : c[1]);
    }, "") || a.toString()) + "\n";
  }, "");
}

console.log(fizz([[3, 'Fizz'], [5, 'Buzz'], [7, 'Baxx']], 20));

