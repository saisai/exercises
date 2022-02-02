package main

import (
	"fmt"
	"reflect"
)

type User struct {
	name	string
	occupation	string
}

func main() {
	var pu *User = new(User)
	fmt.Println(pu)
	fmt.Println(reflect.TypeOf(pu))

	pu.name = "Robert Roe"
	pu.occupation = "accountant"

	fmt.Println(pu)
}

