package main

import "fmt"

func modify(pv *int) {
	*pv = 11
}

func main() {
	var count int = 10
	fmt.Println(count)

	modify(&count)
	fmt.Println(count)
}

