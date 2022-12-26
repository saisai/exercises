package main

import (
    "fmt"
    "math"
)

func main() {
    for i := 1; i <= 100; i++ {
        f := math.Sqrt(float64(i))
        if math.Mod(f, 1) == 0 {
            fmt.Print("0")
        } else {
            fmt.Print("-")
        }
    }
    fmt.Println()
}
