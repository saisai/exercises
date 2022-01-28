package main

import "fmt"

func main() {

	sum := func(a, b, c int) int {
		return a + b + c
	}(3, 5, 7)

	fmt.Println("5+3+7 =", sum)
}

