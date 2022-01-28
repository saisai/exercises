package main

import (  
    "fmt"
)

func main() {  
    employeeSalary := map[string]int{
        "steve": 12000,
        "jamie": 15000,
        "mike":  9000,
    }
    fmt.Println("Contents of the map")
    for key, value := range employeeSalary {
	    fmt.Printf("employeeSalary[%s] = %d\n", key, value)
    }
    }

