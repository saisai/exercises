package main

import "fmt"

type User struct {
    name       string
    occupation string
    age        int
}

func main() {

    u := new(User)
    u.name = "Richard Roe"
    u.occupation = "driver"
    u.age = 44

    fmt.Printf("%s is %d years old and he is a %s\n", u.name, u.age, u.occupation)
}
