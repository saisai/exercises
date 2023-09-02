package main

import "fmt"

func main() {
	employeeSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
	}
	employeeSalary["mike"] = 9000
	fmt.Println("employeeSalary map contents:", employeeSalary)
}

