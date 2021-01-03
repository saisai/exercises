package main

import "fmt"

func main() {
    s := []int{2, 3, 5, 7, 11, 13}

    fmt.Println(s[:2])

    s = s[1:6]
    fmt.Println(s)

    s = s[:2]
    fmt.Println(s)

    s = s[1:]
    fmt.Println(s)
}
