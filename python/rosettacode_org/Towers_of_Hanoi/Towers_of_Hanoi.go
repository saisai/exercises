package main

import "fmt"

func main() {
	move(3, "A", "B", "C")
}

func move(n uint64, a, b, c string) {
	if n > 0 {
		move(n-1, a, c, b)
		fmt.Println("a")
		fmt.Println("Move disk from " + a + " to " + c)
		fmt.Println("b")
		move(n -1, b, a, c)
		fmt.Println("c")
	}
}

