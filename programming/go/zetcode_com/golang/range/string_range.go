package main

import "fmt"

func main() {

	s := "合気道"

	for idx, e := range s {
		fmt.Printf("%d %c\n", idx, e)
	}

	fmt.Println()
}

