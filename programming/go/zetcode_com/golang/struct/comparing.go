package main

import "fmt"

type Point struct {
    x int
    y int
}

func main() {

    p1 := Point{3, 4}
    p2 := Point{3, 4}

    if p1 == p2 {

        fmt.Println("The structs are equal")
    } else {

        fmt.Println("The structs are not equal")
    }
}
