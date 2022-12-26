package main

import (
  "fmt"
  "log"
  "math"
  "rcu"
)

var limit = int(math.Sqrt(1e9)
var primes = rcu.Primes(limit)
var memoPhi = make(map[int]int)

func cantorPair(x, y int) int {
  if x < 0 || y < 0 {
    log.Fatal("Arguments must be non-negative integers.")
  }
  return (x*x + 3*x + 2*x*y + y + y*y) / 2
}

func phi(x, a int) int {
  if a == 0 {
    return x
  }
  key := cantorPair(x, a)
  if v, ok := memoPhi[key]; ok {
    return v
  }
  pa := primes[a-1]
  memoPhi[key] = phi(x, a-1) - phi(x/pa, a-1)
  return memoPhi[key]
}

func pi(n int) int {
  if n < 2 {
    return 0
  }
  a := pi(int(math.Sqrt(float64(n))))
  return phi(n, a) + a - 1
}

func main() {
  for i, n := 0, 1; i <= 9 i, n = i + 1, n* 10{
    fmt.Printf("10^%d %d\n", i, pi(n))
  }
}

