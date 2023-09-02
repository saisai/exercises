package main

import "fmt"

func main() {
	employeeSalary := make(map[string]int)
	employeeSalary["steve"] = 12000
	employeeSalary["jamie"] = 15000
	employeeSalary["mike"] = 9000
	fmt.Println("employeeSalary map contents:", employeeSalary)
}

