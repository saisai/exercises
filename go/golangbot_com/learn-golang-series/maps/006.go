package main

import (  
    "fmt"
)

func main() {  
    employeeSalary := map[string]int{
        "steve": 12000,
        "jamie": 15000,     
        "mike": 9000,
    }
    fmt.Println("map before deletion", employeeSalary)
    delete(employeeSalary, "steve")
    fmt.Println("map after deletion", employeeSalary)

}

