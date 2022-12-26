function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}
var value = "123.45e7"; // Assign string literal to value
if (isNumeric(value)) {
    console.log(value);
  // value is a number
}
//Or, in web browser in address field:
//  javascript:function isNumeric(n) {return !isNaN(parseFloat(n)) && isFinite(n);}; value="123.45e4"; if(isNumeric(value)) {alert('numeric')} else {alert('non-numeric')}


// https://stackoverflow.com/questions/18082/validate-decimal-numbers-in-javascript-isnumeric
function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}
