package main

import "fmt"

func main() {
	fmt.Println(calculation("Rectangle", 20, 30))
	fmt.Println(calculation("Square", 20))
}

func calculation(str string, y ...int) int {
	area := 1

	for _, val := range y {
		if str == "Ractangle" {
			area *= val
		} else if str == "Square" {
			area = val * val
		}
	}
	return area
}

