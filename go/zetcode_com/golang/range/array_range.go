package main

import "fmt"

func main() {

	vals := [...]int{5,4,3,2,1}

	for idx, e := range vals {
		fmt.Println("element ", e, " at index ", idx)
	}
}

