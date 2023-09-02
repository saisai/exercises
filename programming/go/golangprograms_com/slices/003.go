package main

import "fmt"

func main() {

	var intSlice = []int{10,20, 30,40}
	var strSlice = []string{"India", "Canada", "Japan"}

	fmt.Println("inSlice \tLen: %v \t Cap: %v\n", len(intSlice), cap(intSlice))
	fmt.Printf("strSlice \tLen: %v \tCap: %v\n", len(strSlice), cap(strSlice))
}

