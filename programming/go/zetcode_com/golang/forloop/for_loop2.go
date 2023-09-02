package main

import "fmt"

func main() {

	sum := 0
	i := 9

	for i > 0 {
		sum += i
		i--
	}

	fmt.Println(sum)
}

