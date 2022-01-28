package main

import "fmt"

func main() {
	u := struct {
		name	string
		age	int
	}{
		name: "John Doe",
		age: 32,
	}

	fmt.Printf("%s is %d years old\n", u.name, u.age)
}

