package main

import (
  "fmt"
)

func isSubsequence(s string, t string) bool {
  i, j := 0, 0
  for i < len(s) && j < len(t) {
    if s[i] == t[j] {
      i++
    }
    j++
  }
  return i == len(s)
}

func main() {
  s, t := "abc","ahbgdc"
  fmt.Println(isSubsequence(s, t))
}
