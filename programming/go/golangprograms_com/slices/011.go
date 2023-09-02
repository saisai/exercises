package main

import "fmt"

func main() {
	var strSlice = []string{"India", "Canada", "Japan", "Germany", "Italy"}

	fmt.Println("\n---------------Example 1 --------------------\n")

	for index, element := range strSlice {
		fmt.Println(index, "--", element)
	}

	fmt.Println("\n-----------------------Example 2---------------\n")
	for _, value := range strSlice {
		fmt.Println(value)
	}

	j := 0
	fmt.Println("\n---------- Example 3 --------------\n")
	for range strSlice {
		fmt.Println(strSlice[j])
		j++
	}


}

