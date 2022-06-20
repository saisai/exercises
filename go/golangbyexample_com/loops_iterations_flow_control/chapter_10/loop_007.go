

package main

import "fmt"

func main() {

	i := 1
	// function call in the init part in for loop
	for test(); i < 3; i++ {
		fmt.Println(i)
	}

	// assignment in the init part in for loop
	for i = 2; i < 3; i++ {
		fmt.Println(i)
	}
}

func test() {
	fmt.Println("In test function")
}
