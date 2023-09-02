package main

import "fmt"

func main() {

    grades := map[string]int{
        "Lucia": 2,
        "Paul":  1,
        "Merry": 3,
        "Jane":  1,
    }

    g := grades["Lucia"]
    fmt.Println(g)

    g = grades["Peter"]
    fmt.Println(g)

    g, found := grades["Lucia"]
    fmt.Println(g, found)

    g, found = grades["Peter"]
    fmt.Println(g, found)

    if g, found := grades["Jane"]; found {
        fmt.Println(g)
    }
}
