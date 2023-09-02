package main

import "fmt"

func main() {
	var slice1 = []string{"india", "japan", "canada"}
	var slice2 = []string{"australia", "russia"}

	slice2 = append(slice2, slice1...)

	fmt.Println(slice2)

}
