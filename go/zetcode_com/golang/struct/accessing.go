package main


import "fmt"

type User struct {
	name		string
	age		int
}

func main() {

	u := User{}
	u.name = "John Doe"
	u.age = 34

	fmt.Printf("%s is %d years old\n", u.name, u.age)
}

