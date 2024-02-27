package main

import (
  "fmt"
  "strings"
)

func main() {
  fmt.Println(strings.Contains("seafood", "foo"))
  fmt.Println(strings.Contains("seafoo", "bar"))
  fmt.Println(strings.Contains("seafood", ""))
  fmt.Println(strings.Contains("", ""))
}
