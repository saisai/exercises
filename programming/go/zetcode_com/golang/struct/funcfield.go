package main

import "fmt"

type Info func(string, string, int) string

type User struct {
	name		string
	occupation	string
	age		int
	info		Info
}

func main() {

	u := User{
		name:		"John Doe",
		occupation:	"gardner",
		age:		30,
		info:		func(name string, occupation string, age int) string{
			return fmt.Sprintf("%s is %d years old and he is a %s\n", name, age, occupation)
		},
	}
	fmt.Printf(u.info(u.name, u.occupation, u.age))
}

