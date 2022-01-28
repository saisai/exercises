package main

import "fmt"

type User struct {

	name		string
	occupation	string
	age 		int
}

func main() {

	u := User{"John Doe", "gardener", 34}

	fmt.Printf("%s is %d years old and he is a %s\n", u.name, u.age, u.occupation)
}

