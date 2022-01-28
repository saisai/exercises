package main

import "fmt"

type Address struct {
	city		string
	country		string
}

type User struct {
	name	string
	age	int
	Address
}

func main() {

	p := User{
		name: "John Doe",
		age: 34,
		Address: Address{
			city: "New York",
			country: "USA",
		},
		}

	fmt.Println("Name: ", p.name)
	fmt.Println("Aege: ", p.age)
	fmt.Println("City: ", p.city)
	fmt.Println("Country: ", p.country)
}

