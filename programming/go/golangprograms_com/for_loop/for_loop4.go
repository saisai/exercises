package main

import "fmt"

func main() {
	i := 5
	for {
		fmt.Println("Hello")
		if i == 10 {
			break
		}
		i++
	}
}

