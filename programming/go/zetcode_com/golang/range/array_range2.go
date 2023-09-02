package main

import "fmt"

func main() {

	vals := [...]int{5, 4, 3, 2, 1}

	for _, e := range vals {
		fmt.Printf("%d ", e)
	}

	fmt.Println("\n*************")

	for idx, _ := range vals {
		fmt.Printf("%d", idx)
	}

	fmt.Println("\n**********")

	for idx := range vals {
		fmt.Printf("%d -> %d\n", idx, vals[idx])
	}
}

