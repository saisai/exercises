package main

import "fmt"

func main() {

	var a = 7
	var p = &a
	var pp = &p

	fmt.Println(a)
	fmt.Println(&a)

	fmt.Println("--------------------")


	fmt.Println(p)
	fmt.Println(&p)

	fmt.Println("--------------------")

	fmt.Println(pp)
	fmt.Println(&pp)

	fmt.Println("--------------------")

	fmt.Println(*pp)
	fmt.Println(**pp)

}

