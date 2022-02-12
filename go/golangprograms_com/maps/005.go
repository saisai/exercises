package main

import "fmt"

func main() {

	var employee = map[string]int{"Mark":10, "Sandy":20}
	fmt.Println(employee)

	employee["Rocky"] = 30
	employee["Josef"] = 40

	fmt.Println(employee)
}

