package main

import "fmt"

func main() {
	var count int =4
	fmt.Println(count)

	var pv = &count
	*pv = 3
	fmt.Println(pv)
	fmt.Println(*pv)

	var pv2 *int = &count
	*pv =2
	fmt.Println(pv2)
	fmt.Println(*pv2)

	pv3 := &count
	*pv = 1
	fmt.Println(pv3)
	fmt.Println(*pv3)
}

