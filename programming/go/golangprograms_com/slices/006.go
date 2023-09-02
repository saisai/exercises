package main

import "fmt"

func main() {
	var intSlice = []int{10, 20, 30, 40}

	fmt.Println(intSlice[0])
	fmt.Println(intSlice[1])
	fmt.Println(intSlice[0:4])
	fmt.Println(intSlice[:])
	fmt.Println(intSlice[:3])
}
