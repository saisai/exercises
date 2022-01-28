package main

import "fmt"

type User struct {
    name       string
    occupation string
    age        int
}

func main() {

    u1 := User{"John Doe", "gardener", 34}

    u2 := u1

    u2.name = "Richard Roe"
    u2.occupation = "driver"
    u2.age = 44

    fmt.Printf("%s is %d years old and he is a %s\n", u1.name, u1.age, u1.occupation)
    fmt.Printf("%s is %d years old and he is a %s\n", u2.name, u2.age, u2.occupation)
}
