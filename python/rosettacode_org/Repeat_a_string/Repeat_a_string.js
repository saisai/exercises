String.prototype.repeatt = function(n) {
  return new Array(1 + (n || 0)).join(this);
}

console.log("ha".repeatt(5));


console.log("HHa".repeat(5));

