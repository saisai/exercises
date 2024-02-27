package main

import (
  "cmp"
  "fmt"
)

func main() {
  userInput1 := ""
  userInput2 := "some text"

  fmt.Println(cmp.Or(userInput1, "default"))
  fmt.Println(cmp.Or(userInput2, "default"))
  fmt.Println(cmp.Or(userInput1, userInput2, "default"))
}
