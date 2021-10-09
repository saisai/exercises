// using chained methods
function reverseStr1(s) {
  return s.split('').reverse().join('');
}

// fast method using for loop
function reverseStr2(s) {
  for(var i = s.length - 1, o=''; i >=0; o += s[i--]){}
  return o;
}

// fast method using while loop (faster with long strings in some browsers
// when compared with for loop)

function reverseStr3(s){
  var i = s.length, o = '';
  while(i--) o += s[i];
  return o;
}

console.log(reverseStr1("Some string to be reversed"));
console.log(reverseStr2("Some string to be reversed"));
console.log(reverseStr3("Some string to be reversed"));

