function recurse(depth)
{
 try
 {
  return recurse(depth + 1);
 }
 catch(ex)
 {
  return depth;
 }
}
 
var maxRecursion = recurse(1);
console.log("Recursion depth on this system is " + maxRecursion);
//document.write("Recursion depth on this system is " + maxRecursion);
