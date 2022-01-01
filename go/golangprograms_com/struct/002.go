package main

import "fmt"

type rectangle struct {
	length int
	breadth int
	color string

	geometry struct {
		area int
		perimeter int
	}
}

func main() {
	var rect rectangle // dot notation
	rect.length = 10
	rect.breadth = 20
	rect.color = "Green"

	rect.geometry.area = rect.length * rect.breadth
	rect.geometry.perimeter = 2 * (rect.length + rect.breadth)

	fmt.Println(rect)
	fmt.Println("Area:\t", rect.geometry.area)
	fmt.Println("Perimeter:", rect.geometry.perimeter)
}

