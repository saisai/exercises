package main

import (

  "fmt"
  "maps"
)

func main() {
  m1 := map[string]int{
    "key": 1,
  }

  m2 := maps.Clone(m1)
  m2["key"] = 100
  fmt.Println(m1["key"])
  fmt.Println(m2["key"])

  m3 := map[string][]int{
    "key": {1, 2, 3},
  }

  m4 := maps.Clone(m3)
  fmt.Println(m4["key"][0])
  m4["key"][0] = 100
  fmt.Println(m3["key"][0])
  fmt.Println(m4["key"][0])
}
