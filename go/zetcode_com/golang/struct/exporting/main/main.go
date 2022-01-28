package main

import (
	"exporting/model"
	"fmt"
)

func main() {
	u := model.User{Name: "John Doe", Occupation: "gardener"}

	fmt.Printf("%s is a %s\n", u.Name, u.Occupation)
}

