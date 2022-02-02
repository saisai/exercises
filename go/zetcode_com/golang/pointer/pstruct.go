package main

import "fmt"

type User struct {
	name	string
	occupation string
}

func modify(pu *User) {
	pu.name = "Robert Roe"
	pu.occupation = "driver"
}

func main() {

	u := User{"John Doe", "gardner"}
	fmt.Println(u)

	modify(&u)

	fmt.Println(u)
}

