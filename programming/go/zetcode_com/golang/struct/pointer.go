package main

import "fmt"

type Point struct {
	x int
	y int
}

func main() {

	p := Point{3, 4}

	p_p := &p

	(*p_p).x = 1
	p_p.y = 2
	fmt.Println(p)
}

