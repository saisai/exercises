package main

import (  
    "fmt"
)

func main() {  
    num := 99
    if num <= 50 {
        fmt.Println(num, "is less than or equal to 50")
    } else if num >= 51 && num <= 100 {
        fmt.Println(num, "is between 51 and 100")
    } else {
        fmt.Println(num, "is greater than 100")
    }
}

