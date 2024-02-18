
package main

import "fmt"

func myfunc(p, q int) (int, int, int) {
  return p -q, p * q, p + q
}

func main() {
  var myvar1, myvar2, myvar3 = myfunc(4, 2)

  fmt.Printf("Result is: %d", myvar1)
  fmt.Printf("\nResult is: %d", myvar2)
  fmt.Printf("\n Result is: %d", myvar3)
}
