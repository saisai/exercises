package main

import "fmt"

type User struct {
	name		string
	occupation	string
	country		string
}

func main() {

	users := []User{

		{"John Doe", "gardener", "USA"},
		{"Roger Roe", "driver", "UK"},
		{"Paul SMithg", "programmer", "Canada"},
		{"Lucia Mala", "teacher", "Slovakia"},
	}

	var programmers []User

	for _, user := range users {

		if isProgrammer(user) {
			programmers =append(programmers, user)
		}
	}

	fmt.Println("Programmers:")
	for _, u := range programmers {
		fmt.Println(u)
	}
}

func isProgrammer(user User) bool {
	return user.occupation == "programmer"
}

