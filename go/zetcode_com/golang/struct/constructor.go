package main


import "fmt"

type User struct {
	name		string
	occupation	string
	age		int
}

func newUser(name string, occupation string, age int) *User {
	p := User{name, occupation, age}
	return &p
}

func main() {
	u := newUser("Richard Roe", "driver", 44)

	fmt.Printf("%s is %d years old and he is a %s\n", u.name, u.age, u.occupation)
}

