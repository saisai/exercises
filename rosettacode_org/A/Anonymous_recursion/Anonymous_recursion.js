function fibo(n) {
    if(n < 0) {throw "Argument cannot be negative"}

    return (function(n) {
        return (n < 2) ? 1 : arguments.callee(n-1) + arguments.callee(n-2);
    })(n);
}

console.log(fibo(10));


function fiboo(n) {
  if (n < 0) { throw "Argument cannot be negative"; }

  return (function fib(n) {
    return (n < 2) ? 1 : fib(n-1) + fib(n-2);
  })(n);
}

console.log(fiboo(10))
